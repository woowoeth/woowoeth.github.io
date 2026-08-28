import os, re, sys
def check(root="."):
    hits, total = [], 0
    for dp, dn, fn in os.walk(os.path.join(root, "i")):
        if "index.html" not in fn: continue
        path = os.path.join(dp, "index.html")
        s = open(path, encoding="utf-8").read()
        if 'http-equiv="refresh"' in s or "<article>" not in s: continue
        b = s[s.index("<article>"):s.index("</article>")]
        txt = lambda x: re.sub(r"<[^>]+>", "", x).strip()
        says = [txt(m.group(1)) for m in
                re.finditer(r'<blockquote class="say"><p>(.*?)</p></blockquote>', b, re.S)]
        total += len(says)
        body = re.sub(r'<blockquote class="say">.*?</blockquote>', "", b, flags=re.S)  # 排除金句自身
        ps = [txt(m.group(1)) for m in re.finditer(r'<p[^>]*>(.*?)</p>', body, re.S)]
        for q in says:
            if q in ps:
                hits.append((path.replace("./i/", "").replace("/index.html", ""), q))
    return hits, total
h, t = check(sys.argv[1] if len(sys.argv) > 1 else ".")
print("金句总数 %d ；与页面上某个完整段落逐字相同：%d 处" % (t, len(h)))
for p, q in h[:10]:
    print("   %-26s %s" % (p, q[:46] + ("…" if len(q) > 46 else "")))
