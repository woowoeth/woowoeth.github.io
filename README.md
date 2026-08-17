# 人类世界生存法则 · Human World

一个关于「世界到底怎么运转」的知识库：战略、财富、权力、人性、创业，取自 **89 位人物与典籍**，跨越 2600 年。

线上： https://ourword.ai/

每一条都写清楚四件事：这个人真正留下的那一个想法、背后的故事、拆开的分则与例子、以及今天怎么用。部分条目另有「败局时刻」与「失败教训」。

## 七大分类

| 分类 | 条数 |
|---|---|
| 战略·博弈 | 14 |
| 心智·哲学 | 13 |
| 财富·投资 | 13 |
| 权力·治理 | 13 |
| 创业·产品 | 12 |
| 处世·人性 | 12 |
| 典籍·洞见 | 12 |

## 结构

单文件应用。所有数据在 `index.html` 的 `const D=[...]` 数组里，每条包含：

`c` 分类 · `n` 名字 · `e` 朝代年份 · `w` 压缩关键词 · `y` 排序年份 · `d` 简介 · `story` 经典一幕 · `f` 核心框架（含 `n`/`d`/`eg`）· `q` 金句 · `apply` 现代应用 · `l` 关联 · `contrast` 对照阅读（含 `n`/`why`），部分含 `fail` 败局与 `lesson` 教训。

关联与对照只需单向手写，`relOf` / `contrastOf` 在渲染期自动补齐反向边并去重，新增条目自动双向可达。

## 抓取层

单文件应用对不执行 JavaScript 的爬虫是一张空页面，所以 `seo/build_seo.py` 从 `D` 数组生成静态层：每条一个 `/i/<名字>/` 页面、分类聚合页 `/t/`、`/all/`、`sitemap.xml`、`feed.xml`、`llms.txt`、`llms-full.txt`，并回写首页的 JSON-LD 与 GEO 区块。

```bash
python seo/build_seo.py     # 从仓库根目录运行
```

只写入字节真正变化的文件，空跑不产生提交。GitHub Actions 在每次 push 和每日定时自动执行。

站点基址在 `seo/geo_kit.py` 的 `SITE` 与 `seo/build_seo.py` 的 `path` 两处，改完重新构建即可整体迁移。

## 供 AI 引用

- https://ourword.ai/llms.txt
- https://ourword.ai/llms-full.txt
