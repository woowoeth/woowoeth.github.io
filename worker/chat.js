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
const IP_CEIL = 120;          // 每个出口 IP 每天的上限，只用来挡脚本
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
   读者看到的会是可点的出处链接。`;

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
function tidy(raw) {
  raw = raw.replace(/\n*USED\s*[:：].*$/, '').trimEnd();
  raw = raw.replace(/^\s*#{1,6}\s*/gm, '');          // 去掉 # 标题
  raw = raw.replace(/^[ \t]+/gm, '');                // 去掉行首缩进
  let n = 0;
  raw = raw.replace(/[“”"]/g, () => (++n % 2 === 0 ? '」' : '「'));
  raw = raw.replace(/[（(]\s*资料\s*(\d+)\s*[)）]/g, '[$1]');
  raw = raw.replace(/资料\s*(\d+)/g, '[$1]');
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
async function quotaCheck(env, ip, cid) {
  const day = hwDay();
  if (cid && (await counter(env, `c:${day}:${cid}`)) >= DAILY) return 'you';
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
      if (rows.length) out.push({ day, n: rows.length, rows });
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

    const blocked = await quotaCheck(env, ip, cid);
    if (blocked === 'you') {
      return json({ error: `今天的 ${DAILY} 次已经用完了，明天再来`, scope: 'you' }, 429, origin);
    }
    if (blocked === 'net') {
      return json({ error: '这个网络今天问得有点多，过一会儿再试', scope: 'net' }, 429, origin);
    }

    const q = String(body.q || '').trim().slice(0, MAX_Q);
    if (!q) return json({ error: 'empty question' }, 400, origin);
    const ctx = (Array.isArray(body.ctx) ? body.ctx : []).slice(0, MAX_CTX);

    const parts = ctx.map((c, i) =>
      `【资料 ${i}】${c.p || ''} · ${c.n || ''}（${c.w || ''}）\n` +
      `${String(c.txt || '').slice(0, MAX_TXT)}\n出处链接：${c.u || ''}`
    );
    // 处境名由前端检索时带过来（alias 行里本来就有，以前丢掉了）。
    // 有它模型才能点名「你这件事是『钱不够』」。
    const scene = String(body.scene || '').slice(0, 40);
    const head = `读者说：${q}` + (scene ? `\n\n读者的处境：${scene}` : '');
    const user = `${head}\n\n可用资料：\n\n${parts.join('\n\n')}`;

    let up;
    try {
      up = await fetch(UPSTREAM, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${env.HW_CHAT_KEY}` },
        body: JSON.stringify({
          model: MODEL,
          messages: [{ role: 'system', content: SYSTEM }, { role: 'user', content: user }],
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
    const answer = tidy(raw);
    const used = [...new Set([...answer.matchAll(/\[(\d+)\]/g)].map(m => parseInt(m[1], 10)))].sort();
    return json({ answer, used }, 200, origin);
  },
};
