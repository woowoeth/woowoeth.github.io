# -*- coding: utf-8 -*-
"""在真实页面上跑多轮对话——这才是能抓到那个 bug 的测法。

前一个脚本用 curl 直接打 worker，两轮都手动喂同一批章节，
于是「检索把六个字匹配到带团队」那一半根本没被复现。
必须走浏览器：首页点「问」，然后在面板里真敲一句短回复，
让前端自己去检索、自己决定发什么 ctx。
"""
import asyncio, json, sys, time
from playwright.async_api import async_playwright

FOLLOWS = ["卡在总是忘记", "就是坚持不下来", "不知道"]
DRIFT = ["团队","队伍","下属","带人","员工","汇报","部门","合伙人","伴侣","孩子","父母","仓位","客户","招人"]

async def run(pg, follow, sent):
    await pg.click('#hwx-ago2')
    for _ in range(90):
        t = await pg.evaluate("(document.querySelectorAll('#hwq-log .hwq-ai')[0]||{}).innerText||''")
        if t and '在翻书' not in t: break
        await pg.wait_for_timeout(1000)
    a1 = await pg.evaluate("(document.querySelectorAll('#hwq-log .hwq-ai')[0]||{}).innerText||''")
    await pg.fill('#hwq-in', follow)
    await pg.click('#hwq-send')
    for _ in range(90):
        n = await pg.evaluate("document.querySelectorAll('#hwq-log .hwq-ai').length")
        t = await pg.evaluate("(document.querySelectorAll('#hwq-log .hwq-ai')[1]||{}).innerText||''")
        if n > 1 and t and '在翻书' not in t: break
        await pg.wait_for_timeout(1000)
    a2 = await pg.evaluate("(document.querySelectorAll('#hwq-log .hwq-ai')[1]||{}).innerText||''")
    return a1, a2

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        bad = 0
        for follow in FOLLOWS:
            ctx = await b.new_context(viewport={"width":430,"height":900})   # 新 context = 新 cid
            pg = await ctx.new_page(); sent = []
            async def cap(rt):
                if "workers.dev" in rt.request.url and rt.request.method == "POST":
                    sent.append(json.loads(rt.request.post_data))
                await rt.continue_()
            await pg.route("**/*", cap)
            await pg.goto("https://ourword.ai/?cb=" + str(int(time.time())), wait_until="networkidle")
            await pg.wait_for_timeout(700)
            a1, a2 = await run(pg, follow, sent)
            r1, r2 = sent[0], sent[1]
            c1 = [c["u"] for c in r1["ctx"][:3]]
            c2 = [c["u"] for c in r2["ctx"][:3]]
            head = a2.strip().split("\n")[0]
            drift = [w for w in DRIFT if w in a2]
            ok = (not drift) and bool(set(c1) & set(c2))
            if not ok: bad += 1
            print("① 读者:", (await pg.evaluate("(document.querySelectorAll('#hwq-log .hwq-me')[0]||{}).innerText||''"))[:34])
            print("   答尾句:", a1.strip().split("\n")[-1][:38])
            print("② 读者:", follow)
            print("   前端这轮检索到:", [x.split('/')[2] for x in c2])
            print("   带了几轮历史:", len(r2.get("history") or []))
            print("   答首句:", head[:50])
            print("   判定:", "✅ 接住了" if ok else ("❌ 飞了" + ("，冒出 " + ",".join(drift) if drift else "，章节完全不沾")))
            print()
            await ctx.close()
        print("=== %d/%d 处飞了 ===" % (bad, len(FOLLOWS)))
        await b.close()
asyncio.run(main())
