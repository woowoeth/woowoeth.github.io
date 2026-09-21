# 把 ourword 的处境内容接进别的地方

两件东西，各干各的：

| | 是什么 | 谁会用到 |
|---|---|---|
| `mcp/ourword_mcp.py` | **接口** —— 让任何 MCP 客户端能按处境检索、取原文 | 配置过 MCP 的人（Claude Desktop、Cursor…） |
| `skill/ourword/SKILL.md` | **说明书** —— 告诉模型什么时候用、怎么答、不许干什么 | 用 Claude 的人 |

两者是一对：MCP 管「能查到」，Skill 管「查到之后怎么用」。只装 MCP，模型会拿它当搜索引擎；
只装 Skill，模型没有检索、只能瞎背。

## MCP

无第三方依赖，Python 3.9+。数据从线上取（`ourword.ai/assets/hw-chat-index*.json`），
本地缓存一天，不用克隆这个仓库。

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

## Skill

拷到 `~/.claude/skills/ourword/`（用户级）或项目的 `.claude/skills/ourword/`。
**目录名必须等于 frontmatter 里的 `name`。**

它写死了几条边界，这几条比用法重要：只用库里真有的、每条都要能指回原文、
检索不到就说没有（**不要用常识补一段**）、不做医疗法律金融的个人建议、
危机情况直接给紧急求助方式。

## 还没做的

- **产物**：现在答完就散。真要过我们自己那关（「产物是个东西」），
  应该落下一张可分享的卡片 —— SKILL.md 里已经写了卡片的格式，但那是靠模型自觉，
  没有任何东西保证它真的给。
- **HTTP/SSE 版 MCP**：现在只有 stdio，用户得在本机跑。挂到 Cloudflare Worker 上
  才能一个链接接入，那是下一步。
