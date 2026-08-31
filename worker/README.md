# 悬浮球问答 · 部署

浏览器 → Cloudflare Worker → 硅基流动。**key 只在 Worker 的 secret 里，永远不进浏览器。**

站是 GitHub Pages 纯静态，key 一旦写进前端，任何人 view-source 就能拿走当免费
API 用，额度会被刷爆。这个 Worker 存在的理由只有这一个。

## 一次性部署（需要你的 Cloudflare 账号，我做不了这步）

```bash
cd worker
npm i -g wrangler        # 装一次就行
wrangler login           # 浏览器 OAuth，只能你本人点
```

### 1. 建限流用的 KV

```bash
wrangler kv namespace create HW_CHAT_KV
```

命令会打印一段 `id = "xxxxx"`，把它填进 `wrangler.toml` 里
`PUT_KV_NAMESPACE_ID_HERE` 那一行。

### 2. 把 key 设成 secret（不要写进任何文件）

```bash
wrangler secret put HW_CHAT_KEY
```

回车后粘贴硅基的 key。它存在 Cloudflare 那边，不进仓库。

### 3. 部署

```bash
wrangler deploy
```

### 4. 挂到 ourword.ai/api/chat

域名已经在 Cloudflare 上（NS 是 `carioca/david.ns.cloudflare.com`）。
到 Cloudflare 控制台 → Workers & Pages → `ourword-chat` → Settings → Domains & Routes
→ Add route，填：

```
ourword.ai/api/chat*
```

同源，前端不用处理 CORS。

**如果这条路由加不上**（比如域名是灰云、没走代理），就用 `wrangler deploy` 输出的
那个 `https://ourword-chat.<你的子域>.workers.dev` 地址，告诉我，我改前端那一行。

### 5. 打开开关

部署好之后把 `scripts/force_chapter_ui.py` 顶部的

```python
HW_CHAT_ENDPOINT = ""
```

改成

```python
HW_CHAT_ENDPOINT = "/api/chat"
```

重跑构建、推送。在此之前这个值是空的，前端 `if (!ENDPOINT) return;` 直接退出，
页面上什么都不会出现——宁可没有这个功能，也不要让人点开一个连不上的窗口。

## 换 key

```bash
cd worker && wrangler secret put HW_CHAT_KEY
```

不用重新部署，改完立刻生效。

## 几个数

| | 值 | 在哪改 |
|---|---|---|
| 每 IP 每天次数 | 5 | `chat.js` 的 `DAILY` |
| 模型 | `deepseek-ai/DeepSeek-V3.2` | `chat.js` 的 `MODEL` |
| 单次问题长度 | 500 字 | `MAX_Q` |
| 喂给模型的资料 | 最多 8 篇 × 700 字 | `MAX_CTX` / `MAX_TXT` |

模型是实测选的：2026-09-01 在硅基上同题三轮，V3.2 中位 10.0s / token 918 /
引用位置正确 14 次，V4-Flash 是 16.2s / 1671 / 10，V4-Pro 是 26.8s / 2089 / 12。
token 少一半直接等于额度翻倍。

## 已知的漏

**限流按 IP，挡不住换 IP、无痕窗口、多设备。** 它挡的是「有人写脚本把它当免费
API 刷」，不是精确计费。KV 是最终一致的，边缘节点之间可能短暂不同步，个位数的
溢出属于设计内。

要更严就得加轻量校验（比如首次提问前过一道人机验证），代价是多一步摩擦。
目前没做。

## 改 prompt 要改两处

`worker/chat.js` 的 `SYSTEM` 与 `scripts/chat_dev_proxy.py` 的 `SYSTEM` 是同一套，
本地 demo 就是照 Worker 的形状写的。改一处不改另一处，线上线下答案就不一致了。
后处理（`tidy()` 与 Python 那段正则）同理。
