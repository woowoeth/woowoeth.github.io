# 悬浮球问答 · 部署（全程点网页，不用命令行）

浏览器 → Cloudflare Worker → 硅基流动。**key 只在 Cloudflare 那边，永远不进浏览器。**

站是 GitHub Pages 纯静态。key 一旦写进前端，任何人 view-source 就能拿走当免费
API 用，额度会被刷爆。这个 Worker 存在的理由只有这一个。

---

## 四步，大约五分钟

### 1. 新建 Worker

打开 <https://dash.cloudflare.com> → 左边 **Workers & Pages** → **Create** →
**Create Worker**。

名字填 `ourword-chat`，点 **Deploy**（先部署那个默认的 hello world，无所谓）。

### 2. 贴代码

点 **Edit code**（或 **</> Edit code**），把编辑器里的内容**全选删掉**，
把本目录 `chat.js` 的全部内容粘进去，右上角 **Deploy**。

### 3. 加 key

回到这个 Worker 的 **Settings** → **Variables and Secrets** → **Add**：

- Type 选 **Secret**（不是 Text——Text 会明文显示）
- Variable name：`HW_CHAT_KEY`
- Value：硅基的 key

点 **Deploy**。

### 4. 把地址给我

Worker 页面上有个形如

```
https://ourword-chat.<你的子域>.workers.dev
```

的地址，复制给我，我改一行前端配置、推一次，功能就开了。

**在此之前页面上什么都不会出现**——前端 `HW_CHAT_ENDPOINT` 是空字符串，
脚本直接退出。宁可没有这个功能，也不要让人点开一个连不上的窗口。

---

## 就这样，不用做的事

- ❌ 不用装 wrangler、不用 npm
- ❌ 不用 `wrangler login`
- ❌ 不用建 KV 命名空间（限流用 Cache API，零配置）
- ❌ 不用挂域名路由（用 workers.dev 地址就行）

## 可选：想让限流更准

现在用的 Cache API 按**边缘节点各自计数**——同一个人换个城市可能多问几次。
挡「有人写脚本刷额度」够用，精确计费不够。

要更准：Settings → **Bindings** → Add → **KV Namespace**，
新建一个（名字随意），Variable name 填 `HW_CHAT_KV`。
代码会自动优先走 KV，**不用改一行**。

## 换 key

Settings → Variables and Secrets → `HW_CHAT_KEY` → Edit → 填新的 → Deploy。
不用重新贴代码。

## 几个数

| | 值 | 在 `chat.js` 里改 |
|---|---|---|
| 每 IP 每天次数 | 5 | `DAILY` |
| 模型 | `deepseek-ai/DeepSeek-V3.2` | `MODEL` |
| 单次问题长度 | 500 字 | `MAX_Q` |
| 喂给模型的资料 | 最多 8 篇 × 700 字 | `MAX_CTX` / `MAX_TXT` |

模型是实测选的：2026-09-01 在硅基上同题三轮，V3.2 中位 10.0s / token 918 /
引用位置正确 14 次；V4-Flash 是 16.2s / 1671 / 10，V4-Pro 是 26.8s / 2089 / 12。
token 少一半直接等于额度翻倍。

改完代码要回控制台重新粘一遍并 Deploy——这个仓库里的 `chat.js` 不会自动同步到
Cloudflare。

## 已知的漏

**限流按 IP，挡不住换 IP、无痕窗口、多设备。** 要更严就得加人机验证，代价是多一步
摩擦，目前没做。

## 改 prompt 要改两处

`worker/chat.js` 的 `SYSTEM` 与 `scripts/chat_dev_proxy.py` 的 `SYSTEM` 是同一套
（本地 demo 照 Worker 的形状写的）。改一处不改另一处，线上线下答案就不一致了。
后处理（`tidy()` 与 Python 那段正则）同理。
