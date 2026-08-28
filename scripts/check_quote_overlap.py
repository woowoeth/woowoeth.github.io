import os, re, sys
STRIP = "「」“”‘’。，、！？；：—…《》 .,!?;:\"'"
bare = lambda t: "".join(c for c in re.sub(r"<[^>]+>", "", t) if c not in STRIP)

def lcs(a, b):
    best = ""
    for i in range(len(a)):
        for j in range(i + len(best) + 1, len(a) + 1):
            if a[i:j] in b:
                best = a[i:j]
            else:
                break
    return best

MIN = int(sys.argv[2]) if len(sys.argv) > 2 else 10
root = sys.argv[1] if len(sys.argv) > 1 else "."
hits = []
for dp, dn, fn in os.walk(os.path.join(root, "i")):
    if "index.html" not in fn: continue
    path = os.path.join(dp, "index.html")
    s = open(path, encoding="utf-8").read()
    if 'http-equiv="refresh"' in s or "<article>" not in s: continue
    b = s[s.index("<article>"):s.index("</article>")]
    foot = re.search(r'<section class="quotes".*?</section>', b, re.S)
    quotes = re.findall(r'<blockquote><p>(.*?)</p>', foot.group(0), re.S) if foot else []
    body = b if not foot else b.replace(foot.group(0), "")
    body = re.sub(r'<blockquote class="say">.*?</blockquote>', "", body, flags=re.S)
    bb = bare(body)
    for q in quotes:
        ov = lcs(bare(q), bb)
        if len(ov) >= MIN:
            hits.append((re.sub(r"^\./?i/", "", path).replace("/index.html", ""),
                         len(ov), ov, bare(q)[:40]))
print("文末金句与正文有 %d 字以上重叠：%d 处" % (MIN, len(hits)))
for p, n, ov, q in sorted(hits, key=lambda x: -x[1])[:14]:
    print("   %-34s %2d字重叠  「%s」" % (p, n, ov[:34]))
