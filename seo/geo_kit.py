#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""geo_kit — shared SEO + GEO generator for ourword.ai."""
import html as _html
import json
import os
import re
import unicodedata
from urllib.parse import quote

SITE = "https://ourword.ai"

SITES = [
    ("", "Human World", "人类世界生存法则"),
    ("site", "OurWord AI", "OurWord AI 导航"),
    ("idea", "Idea", "灵感看板"),
    ("skill", "Skill Store", "Skill 商店"),
    ("ai", "AI Bubble Monitor", "AI 泡沫检测仪"),
    ("pixel", "PixelPad", "像素板"),
    ("zouni", "Zouni", "走你"),
]

AI_AGENTS = [
    "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-Web", "anthropic-ai",
    "PerplexityBot", "Perplexity-User", "Google-Extended", "Googlebot", "Googlebot-Image",
    "Bingbot", "Applebot", "Applebot-Extended", "CCBot", "Amazonbot", "Bytespider",
    "YouBot", "cohere-ai", "Meta-ExternalAgent", "DuckAssistBot", "MistralAI-User",
    "Diffbot", "omgili", "Timpibot", "PetalBot", "Baiduspider", "Sogou web spider",
    "YisouSpider", "360Spider", "HaosouSpider", "Sogou inst spider", "YandexBot",
    "DuckDuckBot", "ia_archiver", "SemrushBot",
]
