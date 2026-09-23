# 把 ourword 的处境内容接进别的地方

两件东西，各干各的：

| | 是什么 | 谁会用到 |
|---|---|---|
| `mcp/ourword_mcp.py` | **接口** —— 让任何 MCP 客户端能按处境检索、取原文 | 配置过 MCP 的人（Claude Desktop、Cursor…） |
| `skill/ourword/SKILL.md` | **说明书** —— 告诉模型什么时候用、怎么答、不许干什么 | 用 Claude 的人 |
| `skill/ourword-en/SKILL.md` | 英文那份说明书 | 英文用户 |

两者是一对：MCP 管「能查到」，Skill 管「查到之后怎么用」。只装 MCP，模型会拿它当搜索引擎；
只装 Skill，模型没有检索、只能瞎背。

## MCP

无第三方依赖，Python 3.8+，一个文件。数据从线上取，本地缓存一天，不用克隆这个仓库。

装法（发了 PyPI 之后是第一行；现在可以用第二行，直接从仓库装，一样是一条命令）：

```bash
claude mcp add ourword -- uvx ourword-mcp
claude mcp add ourword -- uvx --from git+https://github.com/woowoeth/ourword-mcp ourword-mcp
claude mcp add ourword -- python3 /绝对路径/tools/mcp/ourword_mcp.py
```

第二行走的是镜像仓 `woowoeth/ourword-mcp`（实测 7 秒装完）。

```jsonc
// Claude Desktop 的 claude_desktop_config.json
{
  "mcpServers": {
    "ourword": {
      "command": "python3",
      "args": ["/绝对路径/tools/mcp/ourword_mcp.py"]
    }
  }
}
```

三个工具：

- `browse()` —— 列出 112 个**处境归类**；`browse(group="做不完")` 列出该组的具体说法和对应章节
- `read_chapter(url)` —— 取某一篇全文
- `search(query)` —— 字面检索，**兜底用**

**为什么主入口是 browse 而不是 search**：处境是语义的。用户说「领导总改优先级」，
库里对得上的那条是「全都重要，我砍哪个都疼」—— 两句一个共同字都没有。
字面匹配抓不到，而调用方的模型一眼就看得出。所以这里不造半吊子检索器，
只把 112 个归类摆出来让模型自己挑。

（这不是拍脑袋定的：第一版就是做的字面检索，实测「领导总改优先级」命中 0 条，
最高分 0.11。打分函数换了两次分母才对 —— 见 `ourword_mcp.py` 里 `_dice` 的注释。）

自己验一下：

```bash
printf '%s\n' \
 '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' \
 '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"browse","arguments":{"group":"做不完"}}}' \
 | python3 tools/mcp/ourword_mcp.py
```

## 取数走 jsDelivr，为的是能数出「还有多少人在用」

`CDN` 指向 jsDelivr 的 GitHub 直连，取不到才回落 `ourword.ai`。这不是为了快：

- GitHub Pages **不给访问日志**，代码里那个 `User-Agent: ourword-mcp/x.y.z` 原本指着一堵墙。
- 自己往 Worker 打一次 ping 能拿到数，但**那是静默遥测** —— 一个 10KB、宣称零依赖、
  把「不编、每条带 URL」写死在工具描述里的东西，身上装一个关不掉的回传，
  正好打掉它唯一的差异化。有人会逐行读它。
- jsDelivr 的 `/v1/stats` 是公开的，而站上的聊天走相对路径**不经它**
  （`assets/hw-chat.js:560`），所以那条统计里每一次命中都是 MCP 取数，归因干净。
  加上本地缓存一天，**每日 hits ≈ 每日还在用的安装数**。

代价说清楚：`@main` 约 12 小时缓存（本地缓存本来 24 小时，在噪声里）、
只有按日总数没有 UA/IP 维度、数字公开谁都看得见。
**回落保证它不在数据通路上** —— jsDelivr 挂了没有一个用户受影响。

```bash
curl -s "https://data.jsdelivr.com/v1/stats/packages/gh/woowoeth/woowoeth.github.io?period=month"
```

## 两个镜像仓

目录站和爬虫（Glama、PulseMCP、skill 的几家目录）收录的单位是**一个仓库**。
埋在这个 230 MB 网站仓子目录里的东西，它们认不出来，用户点进去看到的也是网站源码。
所以各开一个小仓，只放该放的：

| 镜像仓 | 放什么 |
|---|---|
| [woowoeth/ourword-mcp](https://github.com/woowoeth/ourword-mcp) | `tools/mcp/` 的六个文件 |
| [woowoeth/ourword-skills](https://github.com/woowoeth/ourword-skills) | 两份 `SKILL.md` |

**真源永远是这里。** 两个小仓各有一个 workflow 按小时来拉，
走 GitHub API 不走 raw（raw 有约五分钟 CDN 缓存，主仓刚推完就跑会把旧那份
当成新的提交上来**并且显示成功** —— FAILURES #43）。

`check_tools` 会逐个文件比对镜像和主仓 `origin/main`，不一样就红并告诉你跑哪句：

```bash
gh workflow run sync.yml -R woowoeth/ourword-mcp
gh workflow run sync.yml -R woowoeth/ourword-skills
```

## 发版

打 tag `mcp-v*`，`.github/workflows/mcp-release.yml` 自动发 PyPI + 官方 MCP registry。
两处都走 OIDC，**仓库里不存任何密钥**。PyPI 那边要站主先在 pypi.org 上建一次
Trusted Publisher（owner=woowoeth · repo=woowoeth.github.io · workflow=mcp-release.yml），
建完以后每次发版都不用人再碰凭据。

版本号的真源只有一个：`ourword_mcp.py` 里的 `VERSION`。`pyproject.toml` 和 `server.json`
必须跟着它，对不上 `check_tools` 会红。

## Skill

```bash
npx skills add woowoeth/ourword-skills
```

短地址就够了，不用写到具体那一份 —— CLI 会把仓里三层以内的 SKILL.md 都找出来。
**skills.sh 没有提交入口**，目录是靠 `npx skills add` 的安装遥测填的
（vercel-labs/skills issue #880 底下的官方答案）。所以这一行就是收录的唯一通路。
发之前先自己验一遍：`npx skills add woowoeth/ourword-skills --list` ——
它只克隆和列出、不安装，能当场看出 frontmatter 解析没解析得了。

或者手拷到 `~/.claude/skills/ourword/`（用户级）或项目的 `.claude/skills/ourword/`。
手拷的话，**目录名必须等于 frontmatter 里的 `name`**。

它写死了几条边界，这几条比用法重要：只用库里真有的、每条都要能指回原文、
检索不到就说没有（**不要用常识补一段**）、不做医疗法律金融的个人建议、
危机情况直接给紧急求助方式。

**英文那份是单独写的，不是译文**（`skill/ourword-en/`）。同一批 403 篇章节，
两套不一样的门：中文 112 组处境 / 655 条说法，英文 121 组 / 629 条 ——
英文用户半夜对自己说的那句话，不是中文那句的翻译。`check_tools` 有一条：
英文 SKILL.md 里**一个汉字都不许有**，直译提交会红。

## 还没做的

- **产物**：现在答完就散。真要过我们自己那关（「产物是个东西」），
  应该落下一张可分享的卡片 —— SKILL.md 里已经写了卡片的格式，但那是靠模型自觉，
  没有任何东西保证它真的给。
- **HTTP/SSE 版 MCP**：现在只有 stdio，用户得在本机跑。挂到 Cloudflare Worker 上
  才能一个链接接入，那是下一步。到那时候服务端本来就是我们的，计数是天然的、
  用户也预期得到，jsDelivr 这条就可以退役。
- **Dockerfile 只为过 Glama 的收录检查**，没在生产里跑过。

MIT（见 `LICENSE`）。英文说明在 `mcp/README.md`。
