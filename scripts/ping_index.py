#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tell search engines the sitemap changed. Safe to run on every deploy."""
import json
import ssl
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

SITE = "https://ourword.ai"
SITEMAP = SITE + "/sitemap.xml"
KEY = "a7f3c91e0b4d62f8e15c9a30d47b6e21"
CTX = ssl.create_default_context()


def get(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "OurWordIndex/1.0"})
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.status, r.read()


def post(url, payload, timeout=20):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data,
        headers={"User-Agent": "OurWordIndex/1.0", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.status, r.read()


def urls_from_sitemap(path="sitemap.xml", limit=80):
    p = Path(path)
    if not p.exists():
        return [SITE + "/", SITE + "/all/"]
    root = ET.parse(p).getroot()
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [el.text.strip() for el in root.findall(".//s:loc", ns) if el.text]
    if not locs:
        locs = [el.text.strip() for el in root.findall(".//{*}loc") if el.text]
    home = [u for u in locs if u.rstrip("/") == SITE]
    rest = [u for u in locs if u.rstrip("/") != SITE]
    return (home + rest)[:limit]


def main():
    urls = urls_from_sitemap()
    print("ping %d urls" % len(urls))
    ok = True
    try:
        status, _ = get(
            "https://www.google.com/ping?sitemap=" + urllib.request.quote(SITEMAP, safe="")
        )
        print("google sitemap ping", status)
    except Exception as e:
        ok = False
        print("google ping failed:", e)
    body = {
        "host": "ourword.ai",
        "key": KEY,
        "keyLocation": SITE + "/%s.txt" % KEY,
        "urlList": urls,
    }
    for endpoint in (
        "https://api.indexnow.org/indexnow",
        "https://www.bing.com/indexnow",
        "https://yandex.com/indexnow",
    ):
        try:
            status, _ = post(endpoint, body)
            print(endpoint, status)
        except urllib.error.HTTPError as e:
            print(endpoint, "http", e.code)
            if e.code >= 500:
                ok = False
        except Exception as e:
            print(endpoint, "failed:", e)
    return 0 if ok else 0


if __name__ == "__main__":
    sys.exit(main())
