# 人类世界生存法则 · Human World

一个关于「世界到底怎么运转」的知识库：战略、财富、权力、人性、创业，取自 **100 位人物与典籍**，跨越 2600 年。

线上： https://ourword.ai/

每一条都写清楚四件事：这个人真正留下的那一个想法、背后的故事、拆开的分则与例子、以及今天怎么用。其中 23 条另有「败局时刻」与「失败教训」。

## 七大分类

| 分类 | 条数 |
|---|---|
| 权力·治理 | 15 |
| 创业·产品 | 15 |
| 战略·博弈 | 14 |
| 心智·哲学 | 14 |
| 处世·人性 | 14 |
| 财富·投资 | 14 |
| 典籍·洞见 | 14 |

条目数与分类数由 `seo/build_seo.py` 每次构建回写进首页的 `<b id="st">` 和 `<b id="cat-count">`；这张表是手写的，加条目时记得跟着改。

## 结构

单文件应用。所有数据在 `index.html` 的 `const D=[...]` 数组里，每条包含：

`c` 分类 · `n` 名字 · `e` 朝代年份 · `w` 压缩关键词 · `y` 排序年份 · `d` 简介 · `story` 经典一幕 · `f` 核心框架（含 `n`/`d`/`eg`）· `q` 金句 · `apply` 现代应用 · `l` 关联 · `contrast` 对照阅读（含 `n`/`why`），部分含 `fail` 败局与 `lesson` 教训。

关联与对照只需单向手写，`relOf` / `contrastOf` 在渲染期自动补齐反向边并去重，新增条目自动双向可达。

## 深度阅读（章节层）

比条目长的单篇文章，挂在某个人物页下面，**不进 `D[]`**，数据在 `seo/hw_chapters.py` 的 `CHAPTERS` 里。目前 4 篇，都在毛泽东名下：

| 篇目 | 路径 |
|---|---|
| 矛盾论 | `/i/mao/on-contradiction/` |
| 实践论 | `/i/mao/on-practice/` |
| 论持久战 | `/i/mao/on-protracted-war/` |
| 中国革命战争的战略问题 | `/i/mao/strategy-of-the-revolution/` |

正文里 `==这样==` 包起来的片段渲染成红色下划线重点。父页面上的目录由 `PARENTS` 控制，`ready: False` 的不显示。章节页由 `write_chapters()` 生成，再由 `write_indexes()` 折进 sitemap / llms.txt / llms-full.txt / feed.xml——geo_kit 只认识 `D[]`，少了这一步章节页对爬虫等于不存在。

## 抓取层

单文件应用对不执行 JavaScript 的爬虫是一张空页面，所以 `seo/build_seo.py` 从 `D` 数组生成静态层：每条一个 `/i/<slug>/` 页面、聚合页 `/t/`（7 分类 + 6 时代）、`/all/`、`sitemap.xml`、`feed.xml`、`llms.txt`、`llms-full.txt`，并回写首页的 JSON-LD 与 GEO 区块。

只写入字节真正变化的文件，空跑不产生提交。GitHub Actions 在每次 push 和每日 03:40 自动执行。

站点基址在 `seo/geo_kit.py` 的 `SITE` 与 `seo/build_seo.py` 的 `path` 两处，改完重新构建即可整体迁移。

## 构建顺序

CI（`.github/workflows/seo.yml`）严格按这个顺序跑：

```bash
python scripts/patch_geo_seo.py     # 在 stock geo_kit 上叠 GEO 增强，幂等
python scripts/apply_redesign.py    # 注入本周新条目、样式覆盖、slug 映射
python seo/build_seo.py             # 生成全部静态页与索引产物
python scripts/force_chapter_ui.py  # 给已生成 HTML 补重点样式（跳过跳转桩）
```

然后校验（无冲突标记、无重复 canonical）、有 diff 才提交、`scripts/ping_index.py` 通知搜索引擎。

三条硬规矩：

- **不要直接改 `geo_kit.py`**——CI 会从固定 commit 把它拉回来覆盖掉。所有改动写进 `scripts/patch_geo_seo.py`。
- **不要从 `hw_theme.py` 的模板里删 `%s`**——参数元组不会跟着变，构建会以 `not all arguments converted` 崩掉。要去掉输出里的某一行，用 `seo/strip_cite.py` 那种针对产物的做法。
- **错字改源头**（`scripts/inject_week.py` 的 BATCH、`seo/hw_chapters.py`），不要在生成好的 `index.html` 上打补丁——补丁规则会悄悄失效，而源头的坏数据还在。

## 供 AI 引用

- https://ourword.ai/llms.txt
- https://ourword.ai/llms-full.txt
