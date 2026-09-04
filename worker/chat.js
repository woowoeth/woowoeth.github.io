/**
 * 悬浮球问答的线上代理 · Cloudflare Worker
 *
 * 存在的理由只有一个：**API key 绝不能进浏览器**。
 * 站是 GitHub Pages 纯静态，key 写进前端等于公开，额度会被刷爆。
 * 浏览器 → 这个 Worker → 硅基流动，key 只在 Worker 的 secret 里。
 *
 * 与 scripts/chat_dev_proxy.py 是同一套逻辑（本地 demo 就是照这个形状写的），
 * 改 prompt 或后处理规则时两边都要改，否则线上线下答案不一致。
 *
 * 部署：见 worker/README.md
 */

const ALLOWED_ORIGINS = new Set([
  'https://ourword.ai',
  'https://www.ourword.ai',
]);

const DAILY = 5;              // 每个浏览器每天几次
const PASS_CEIL = 60;         // 「请我喝杯茶」当天畅聊的暗上限，只防脚本
const IP_CEIL = 120;          // 每个出口 IP 每天的上限，只用来挡脚本
const HIST_TURNS = 3;         // 带几轮历史
const HIST_Q = 200;           // 每轮读者那句截断
const HIST_A = 300;           // 每轮答案截断（只为让模型认出自己说过什么）
const MAX_Q = 500;            // 问题长度上限，防止拿它当通用推理后端
const MAX_CTX = 8;            // 最多几篇资料
const MAX_TXT = 700;          // 每篇正文截断
const MODEL = 'deepseek-ai/DeepSeek-V3.2';
const UPSTREAM = 'https://api.siliconflow.cn/v1/chat/completions';

// 与本地代理逐字一致。改一处就要改两处。
const SYSTEM = `你是「人类世界生存法则」这个知识库的问答助手。读者会描述自己此刻遇到的事。

铁规矩：

1. 只根据我给你的资料回答。资料里没有的，直说没有，不要自己编，也不要引入
   资料之外的人物、书名、数字。

2. **说大白话。** 这是最重要的一条。
   不许用这些词：价值、本质、机制、逻辑、维度、要素、原则、方法论、赋能、
   抓手、闭环、心智、认知、颗粒度、底层、复盘（除非资料原文就这么写）。
   不许用「双重困境」「结构性」「归因」这类学术腔。
   判据很简单：这句话你能不能对着一个没读过书的朋友原样说出口。
   说不出口就改，改到能说出口为止。

3. **你的活是选和贴合，不是自己写一套办法。**
   每份资料的正文里都带着现成的三段——「局面」「先问」「用反了」，
   那是逐条校准过的，比你临场想的准。你要做的是：挑最对得上的那一篇，
   把它的「先问」换成他的说法，把它的「用反了」带出来。
   不要绕过它们另写两三条建议——那等于把最贵的部分磨掉。

4. 结构就三段，按这个顺序：

   第一段：一句话说清他这件事难在哪。如果我在「读者的处境」里给了处境名，
   就点出来——比如「你这件事是『钱不够』」——被归类本身就是一种缓解，
   它把「我这事很特别」变成「这是一类事，有人处理过」。

   第二段：给一到两条能立刻做的，取自资料里的「先问」和「局面」。
   具体到动作——做什么、什么时候做、做到什么程度算完。

   第三段：**必须有一条「用反了」**，取自你用的那篇资料。
   开头写「有一处容易用反：」。这一条不许省——
   别处都在教怎么做，只有这里告诉人反着用会怎样，这是最该带出去的东西。

   最后单起一行，**反问他一句**。只问一句，不超过二十字。
   问的必须是能让下一次回答更准的那一件事——多久了、试过什么、
   是哪一头卡住，而不是「你还好吗」这类寒暄。
   他答了，你下一轮就能挑到更对的那一篇；他不答，这一句也不碍事。
   问句不要每次同一个句式。

5. 开头那句**不要每次都用同一个句式**，尤其不要每次都以「你卡在」起手——
   连着看两遍就露出模板腔了，读者会觉得对面是个机器而不是人。
   像朋友接话那样开口：有时直接复述他说的那件事，有时点出难处在哪，
   有时先接一句他的感受再往下说。换着来。

6. **引用只标在每一段的最后。**
   一段里用到了哪几份资料，就在这一段的末尾连着写，比如：
   先联系那些一年见不到几次的人，只说近况，不提要帮忙。他们站在别的圈子里，
   机会才可能从那儿漏过来。[0][2]
   不要标在段落中间的句子后面——那会把话打断。没用到资料的段落不要标。
   **第一段不要标。** 第一段是复述他的处境、说清卡在哪，那是你自己的判断，
   不是从哪一篇里得来的，挂出处反而假。引用只出现在后面给动作的段落。

7. 提到人名书名时用资料里给的原名，不要改写。

8. 不说教、不安慰、不铺垫。语气像一个读过很多书的朋友在饭桌上跟你说话。

9. 引号一律用「」，不用英文双引号。

10. 分点的时候，每一点可以用一个四到八个字的小标题开头并加粗，像这样：
   **先别急着问。** 明天找个他放松的时候……
   加粗只用在这种小标题上，正文里不要用。除了 ** 之外不要用任何其它
   Markdown 记号——不要井号标题、不要下划线、不要列表符号。

11. **每一段之间空一行。** 分点写的时候也一样，「1.」和「2.」之间要空一行，
   不要挤在连续的行里。

12. 全文不超过 340 字。

13. 正文里不要出现「资料」两个字——编号用 [0] 这种方括号就够了，
   读者看到的会是可点的出处链接。

14. **前面有对话的时候，先判断他这句是在接哪一头。**
   你上一轮结尾问了他一句，所以他很可能只回你三五个字——
   「卡在总是忘记」这种。那是在回答你，不是新问题。
   这时候顺着原来那件事往下说，把他这句补进去当细节，
   绝不要换题：他说改习惯卡在忘记，你就接着说改习惯，
   不要因为「卡在」两个字就跑去讲带团队。
   资料我会把上一轮用过的那几篇一并给你，优先在里面挑。
   只有他明确开了一件新的事，才换。

15. **处境名只在第一轮点。**「你这件事是『想改个习惯』」这种句子
   一整段对话里最多出现一次，第二轮再点一遍就成了复读。`;


/* 英文站用这一份。规矩和中文那份一一对应，不是翻译过来的 ——
   第 2 条的禁用词换成了英文自己的行话，第 3 条指向英文章节里的
   Where you are / Ask first / Where it goes wrong，第 12 条把 340 字
   换成 200 词（同样的信息量，英文大约是这个数）。 */
const SYSTEM_EN = `You answer questions for Human World Rules, a library of what
people before us worked out. Readers describe the thing they are in right now.

Hard rules:

1. Answer only from the material I give you. If it isn't there, say so. Don't
   invent, and don't bring in people, books or numbers from outside it.

2. **Plain words.** This is the most important rule.
   Banned: leverage, framework, paradigm, holistic, unpack, journey, actionable,
   alignment, synergy, bandwidth, granular, north star, mental model, optimise,
   root cause, at scale, double down, lean into (unless the source text uses it).
   No academic register: "structural", "dual bind", "attribution", "modality".
   The test is simple: could you say this sentence out loud, unchanged, to a
   friend who has read nothing? If not, rewrite it until you could.

3. **Your job is picking and fitting, not writing your own method.**
   Every piece of material carries three ready-made parts — "Where you are",
   "Ask first", "Where it goes wrong". Those were calibrated one at a time and
   they are better than anything you'll improvise. Pick the piece that actually
   matches, put its "Ask first" into his words, and bring out its "Where it goes
   wrong". Don't route around them and write two or three tips of your own —
   that throws away the most expensive part.

4. Three paragraphs, in this order:

   First: one sentence saying what is actually hard about his situation. If I
   gave you a situation name under "the reader's situation", name it — "what
   you're in is 'Not enough money'". Being classified is itself a relief: it
   turns "my case is peculiar" into "this is a kind of thing, and people have
   handled it".

   Second: one or two things he can do now, taken from "Ask first" and "Where
   you are" in the material. Concrete: what to do, when, and what counts as done.

   Third: **there must be a "where it goes wrong"**, from the piece you used.
   Open it with "One way this goes wrong: ". Never drop this one — everything
   else teaches how to do it; only this says what happens when it's used
   backwards, and that is the part worth carrying away.

   Then, on its own line, **ask him one question back**. One only, under fifteen
   words. It has to be the thing that would make the next answer more accurate —
   how long, what he's tried, which end is stuck — not "are you okay". If he
   answers, you can pick a better piece next round; if he doesn't, no harm done.
   Don't use the same question shape every time.

5. **Don't open the same way every time**, and especially don't start every
   answer with "You're stuck on". Two in a row and it reads as a template.
   Open like a friend picking up the thread: sometimes say back the thing he
   described, sometimes name what's hard, sometimes meet the feeling first.
   Vary it.

6. **Citations go at the end of a paragraph only.**
   Whatever pieces that paragraph used, list them together at its end:
   Start with the people you see a few times a year, and just say how things are
   — don't ask for anything. They stand in other circles, which is where an
   opening can come from. [0][2]
   Not mid-paragraph — that interrupts. No citation on a paragraph that used
   nothing. **Never cite the first paragraph.** That one says his situation back
   to him and names what's hard; it is your own reading, not something drawn
   from a piece, and a citation there rings false.

7. Use names of people and books exactly as the material gives them.

8. No lecturing, no reassurance, no throat-clearing. The register is a
   well-read friend talking across a table.

9. Use straight quotes. No typographic flourishes.

10. When you break something into points, each may open with a bold heading of
   two to five words, like this:
   **Don't ask yet.** Find a moment tomorrow when he's relaxed…
   Bold is only for those headings, never in the body. Apart from ** use no
   Markdown at all — no hash headings, no underscores, no bullet characters.

11. **Blank line between paragraphs**, including between "1." and "2.".

12. Under 200 words.

13. Never write the word "material" in the answer — the bracketed numbers [0]
   are enough; the reader sees them as clickable sources.

14. **When there is prior conversation, work out which thread he's answering.**
   You ended the last turn with a question, so he may reply in four or five
   words — "stuck on always forgetting". That is an answer to you, not a new
   question. Stay on the original thing and fold his words in as detail. Do not
   switch topics: if he said habit-change is stuck on forgetting, keep talking
   about habit-change; don't jump to managing a team because he used the word
   "stuck". I'll pass you the pieces from last round too — prefer those. Switch
   only when he clearly opens something new.

15. **Name the situation in the first turn only.** A sentence like "what you're
   in is 'I want to change a habit'" appears at most once in a conversation.`;

function cors(origin) {
  return {
    'Access-Control-Allow-Origin': origin,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin',
  };
}

function json(obj, status, origin) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', ...cors(origin || 'null') },
  });
}

/* 排版兜底。prompt 里都写了，但这些是确定性的事，不该指望模型每次都听。
   与 chat_dev_proxy.py 的后处理保持一致。 */
function tidy(raw, lang) {
  raw = raw.replace(/\n*USED\s*[:：].*$/, '').trimEnd();
  raw = raw.replace(/^\s*#{1,6}\s*/gm, '');          // 去掉 # 标题
  raw = raw.replace(/^[ \t]+/gm, '');                // 去掉行首缩进
  if (lang !== 'en') {
    // 这条只对中文做：把直引号换成「」。套到英文上是灾难 ——
    // 每一个 " 都会变成中文括号，"Where you are" 变成「Where you are」。
    let n = 0;
    raw = raw.replace(/[“”"]/g, () => (++n % 2 === 0 ? '」' : '「'));
    raw = raw.replace(/[（(]\s*资料\s*(\d+)\s*[)）]/g, '[$1]');
    raw = raw.replace(/资料\s*(\d+)/g, '[$1]');
  } else {
    // 英文那边同样要把「引用写成散文」的情况收成方括号
    raw = raw.replace(/\(\s*(?:source|material)\s*(\d+)\s*\)/gi, '[$1]');
  }
  // 分点之间补空行
  raw = raw.replace(/(?<=\S)\n(?=(?:\d+[.、]|第[一二三四五六七八九十]+[，、,]))/g, '\n\n');
  raw = raw.replace(/\n{3,}/g, '\n\n');
  return raw;
}

/* 限流：优先用 KV，没绑 KV 就退到 Cache API。
 *
 * Cache API 的好处是**零配置**——不用建命名空间、不用填 id，
 * 在控制台粘完代码就能跑。代价是它按边缘节点各自计数：
 * 同一个人换个城市（换到另一个 colo）可能多问几次。
 * 这里要挡的是「有人写脚本把它当免费 API 刷」，不是精确计费，够用。
 *
 * 要更准就在控制台给这个 Worker 绑一个 KV、变量名填 HW_CHAT_KV，
 * 下面的代码会自动优先走 KV，不用改一行。
 */
/* 按东八区切天。原来用 UTC，读者的额度在早上八点回满——
 * 一个中国时区的站，「今天」不该从早上八点开始。 */
function hwDay() {
  return new Date(Date.now() + 8 * 3600e3).toISOString().slice(0, 10);
}

async function counter(env, key) {
  if (env.HW_CHAT_KV) {
    return parseInt((await env.HW_CHAT_KV.get(key)) || '0', 10);
  }
  const hit = await caches.default.match(`https://hw-quota.invalid/${key}`);
  return hit ? parseInt(await hit.text(), 10) || 0 : 0;
}
async function bump(env, key) {
  const n = (await counter(env, key)) + 1;
  if (env.HW_CHAT_KV) {
    await env.HW_CHAT_KV.put(key, String(n), { expirationTtl: 172800 });
  } else {
    await caches.default.put(`https://hw-quota.invalid/${key}`,
      new Response(String(n), { headers: { 'Cache-Control': 'max-age=172800' } }));
  }
}

/* 限流为什么不按 IP 算了。
 *
 * 原来是「每 IP 每天 5 次」。中国的移动网络是 CGNAT——同一个出口 IPv4
 * 后面挂着成千上万部手机；公司、学校、咖啡馆的 Wi-Fi 同理。
 * 于是一个陌生人问完五次，整栋楼、整个基站下的人当天都被挡在外面，
 * 而且他们看到的提示是「你今天的 5 次用完了」——他一次都没问过。
 * 这不是边角情况，是这个站的主力人群的默认情况。
 *
 * 改成两层：
 *   产品规则按浏览器算（cid，客户端生成的随机串，存在 localStorage）。
 *     清缓存、开无痕就能绕过——但那不是这道闸要挡的人。
 *   出口 IP 只留一个高得多的天花板，用来挡「有人写脚本刷免费 API」，
 *     那才是这道闸真正的用途。正常的一栋楼够不到 120。
 *
 * 429 要说清是哪一层：把「这个网络今天太忙」说成「你用完了」，
 * 会让一个一次都没问过的人以为额度被自己花掉了。
 */
/* 「请我喝杯茶，今天接着聊」是信任制：客户端说自己请过了（pass:1）就按 PASS_CEIL 算。
 * 没有验证——白点的人一天最多让我们多花一块多钱，换来的是零平台、零兑换码、零账号。
 * 顺手记两个数，定价靠它们：x:day 撞上限的次数（x:day:cid 记到人），p:day 真用上茶额度的人数。 */
async function quotaCheck(env, ip, cid, pass) {
  const day = hwDay();
  if (cid) {
    const n = await counter(env, `c:${day}:${cid}`);
    const cap = pass ? PASS_CEIL : DAILY;
    if (n >= cap) {
      if (!pass) { await bump(env, `x:${day}`); await bump(env, `x:${day}:${cid}`); }
      return 'you';
    }
    if (pass && n >= DAILY && !(await counter(env, `p:${day}:${cid}`))) {
      await bump(env, `p:${day}:${cid}`); await bump(env, `p:${day}`);
    }
  }
  if ((await counter(env, `q:${day}:${ip}`)) >= IP_CEIL) return 'net';
  return '';
}
async function quotaUse(env, ip, cid) {
  const day = hwDay();
  if (cid) await bump(env, `c:${day}:${cid}`);
  await bump(env, `q:${day}:${ip}`);
}

/* 把读者问过的话记下来。
 *
 * 存什么：问题原文、时间、命中的处境。**不存 IP，不存任何能定位到人的东西**——
 * 这些是人在描述自己的处境，能少存一样就少存一样。
 *
 * 存哪儿，两档：
 *   零配置  console.log 一行，去 Cloudflare 控制台的 Workers 日志看。
 *           不用绑任何东西，但保留期只有几天，也不好翻。
 *   绑 KV   变量名 HW_CHAT_KV（和限流共用一个就行），按天存成 log:YYYY-MM-DD。
 *           然后带密钥 GET 就能把这些天的问题一次拉下来。
 *
 * 拉取：GET ?log=7&key=<HW_LOG_KEY>，返回最近 7 天。
 * HW_LOG_KEY 没设就整个关闭这个入口——不设密钥宁可读不到，也不能让人随便翻。
 */
const LOG_DAYS_MAX = 30;

async function jot(env, q, scene) {
  const t = new Date().toISOString();
  try { console.log("ASK " + JSON.stringify({ t, q, s: scene })); } catch (e) {}
  if (!env.HW_CHAT_KV) return;
  const day = t.slice(0, 10);
  const key = `log:${day}`;
  try {
    const cur = JSON.parse((await env.HW_CHAT_KV.get(key)) || "[]");
    cur.push({ t, q, s: scene });
    await env.HW_CHAT_KV.put(key, JSON.stringify(cur.slice(-500)),
                             { expirationTtl: 86400 * 90 });
  } catch (e) {}
}

async function readLog(env, days) {
  if (!env.HW_CHAT_KV) return { error: "没绑 KV，问题只写进了 Workers 日志。绑一个变量名叫 HW_CHAT_KV 的 KV 就能从这里读。" };
  const out = [];
  const now = Date.now();
  for (let i = 0; i < Math.min(days, LOG_DAYS_MAX); i++) {
    const day = new Date(now - i * 86400000).toISOString().slice(0, 10);
    try {
      const rows = JSON.parse((await env.HW_CHAT_KV.get(`log:${day}`)) || "[]");
      /* 撞上限与用茶额度的计数按东八区的天记，这里换成同一种天 */
      const hd = new Date(now - i * 86400000 + 8 * 3600e3).toISOString().slice(0, 10);
      const caps = await counter(env, `x:${hd}`), passes = await counter(env, `p:${hd}`);
      if (rows.length || caps || passes) out.push({ day, n: rows.length, caps, passes, rows });
    } catch (e) {}
  }
  return { days: out.length, total: out.reduce((n, d) => n + d.n, 0), log: out };
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const ok = ALLOWED_ORIGINS.has(origin);

    if (request.method === 'OPTIONS') {
      return ok ? new Response(null, { headers: cors(origin) }) : new Response(null, { status: 403 });
    }
    /* 取问题清单。放在 Origin 白名单之前——它是给站主自己用的，
       不从页面上调，所以不该被白名单挡住；改由 HW_LOG_KEY 把门。 */
    if (request.method === 'GET') {
      const u = new URL(request.url);
      if (u.searchParams.has('log')) {
        if (!env.HW_LOG_KEY || u.searchParams.get('key') !== env.HW_LOG_KEY) {
          return json({ error: 'Forbidden' }, 403, null);
        }
        const d = parseInt(u.searchParams.get('log'), 10) || 7;
        return json(await readLog(env, d), 200, null);
      }
    }

    if (!ok) return json({ error: 'Forbidden origin' }, 403, null);
    if (request.method !== 'POST') return json({ error: 'Method Not Allowed' }, 405, origin);

    const ip = request.headers.get('CF-Connecting-IP') || '0.0.0.0';

    let body;
    try { body = await request.json(); } catch { return json({ error: 'Invalid JSON' }, 400, origin); }
    const cid = String(body.cid || '').replace(/[^a-z0-9]/gi, '').slice(0, 32);
    const pass = body.pass === 1 || body.pass === true || body.pass === '1';

    const blocked = await quotaCheck(env, ip, cid, pass);
    if (blocked === 'you') {
      return json({ error: pass ? '今天聊得够多了，明天再来' : `今天的 ${DAILY} 次已经用完了，明天再来`,
                    scope: 'you', pass: pass ? 1 : 0 }, 429, origin);
    }
    if (blocked === 'net') {
      return json({ error: '这个网络今天问得有点多，过一会儿再试', scope: 'net' }, 429, origin);
    }

    const q = String(body.q || '').trim().slice(0, MAX_Q);
    if (!q) return json({ error: 'empty question' }, 400, origin);

    /* 之前每一轮都是一条孤立的 user 消息，模型看不到上一句自己说过什么。
       而我们的答案结尾偏偏要求追问一句——读者于是回三五个字，
       那三五个字既没有上下文、也检索不出对的篇目，答案就飞了。
       实测：「卡在总是忘记」被答成了带团队。带上历史。 */
    const history = (Array.isArray(body.history) ? body.history : [])
      .slice(-HIST_TURNS)
      .map((t) => ({
        q: String(t && t.q || '').slice(0, HIST_Q),
        a: String(t && t.a || '').slice(0, HIST_A),
      }))
      .filter((t) => t.q && t.a);
    const ctx = (Array.isArray(body.ctx) ? body.ctx : []).slice(0, MAX_CTX);

    const parts = ctx.map((c, i) =>
      `【资料 ${i}】${c.p || ''} · ${c.n || ''}（${c.w || ''}）\n` +
      `${String(c.txt || '').slice(0, MAX_TXT)}\n出处链接：${c.u || ''}`
    );
    // 处境名由前端检索时带过来（alias 行里本来就有，以前丢掉了）。
    // 有它模型才能点名「你这件事是『钱不够』」。
    const scene = String(body.scene || '').slice(0, 40);
    // 英文站送 lang:'en'。缺省是中文 —— 老前端不带这个字段。
    const lang = body.lang === 'en' ? 'en' : 'zh';
    const head = `读者说：${q}` + (scene ? `\n\n读者的处境：${scene}` : '');
    const user = `${head}\n\n可用资料：\n\n${parts.join('\n\n')}`;

    let up;
    try {
      up = await fetch(UPSTREAM, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${env.HW_CHAT_KEY}` },
        body: JSON.stringify({
          model: MODEL,
          messages: [
            { role: 'system', content: lang === 'en' ? SYSTEM_EN : SYSTEM },
            ...history.flatMap((t) => [
              { role: 'user', content: t.q },
              { role: 'assistant', content: t.a },
            ]),
            { role: 'user', content: user },
          ],
          temperature: 0.3,
          max_tokens: 700,
        }),
      });
    } catch (e) {
      return json({ error: '上游请求失败', detail: String(e).slice(0, 120) }, 502, origin);
    }
    if (!up.ok) {
      return json({ error: `上游返回 ${up.status}` }, 502, origin);
    }

    let data;
    try { data = await up.json(); } catch { return json({ error: '上游返回不是 JSON' }, 502, origin); }
    const raw = data?.choices?.[0]?.message?.content;
    if (!raw) return json({ error: '上游没有返回内容' }, 502, origin);

    /* 答成了才扣次数。原来是进门就扣——上游超时、502、被限流，
       读者什么都没拿到却少了一次。和下面 jot 的道理一样。 */
    await quotaUse(env, ip, cid);
    await jot(env, q, scene);          /* 答成了才记，失败的不算读者问过 */
    const answer = tidy(raw, lang);
    const used = [...new Set([...answer.matchAll(/\[(\d+)\]/g)].map(m => parseInt(m[1], 10)))].sort();
    return json({ answer, used }, 200, origin);
  },
};
