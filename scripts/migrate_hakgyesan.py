from pathlib import Path
import shutil, re, json, xml.etree.ElementTree as ET

SITE = "https://reridy.github.io"
PROJ = f"{SITE}/hakgyesan"
DATE = "2026-09-10"
PAGES = [
    "index.html",
    "grade-5.html",
    "rank-cut.html",
    "grade-boundary.html",
    "rank-percentile.html",
    "target-rank.html",
    "exam-target.html",
    "midterm-target.html",
    "performance-target.html",
    "weighted-score.html",
    "score-contribution.html",
    "target-average.html",
    "subject-weighted-average.html",
    "five-grade-guide.html",
    "about.html",
    "privacy.html",
    "contact.html",
]
LEGACY = PAGES[1:]

out = Path("hakgyesan")
if out.exists():
    shutil.rmtree(out)
out.mkdir()
shutil.copytree("assets", out / "assets")
shutil.copy2("favicon.ico", out / "favicon.ico")

collection_ld = json.dumps({
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "학계산",
    "headline": "학계산 — 내신 5등급·시험 목표점수 계산기",
    "url": PROJ + "/",
    "inLanguage": "ko-KR",
    "description": "한국 학생을 위한 내신·시험·석차 계산 도구",
    "isPartOf": {"@type": "WebSite", "name": "Reridy", "url": SITE + "/"},
}, ensure_ascii=False, separators=(",", ":"))

for name in PAGES:
    t = Path(name).read_text(encoding="utf-8")
    t = t.replace(SITE + "/", PROJ + "/")
    t = re.sub(r'(href|src)="/', r'\1="/hakgyesan/', t)
    t = t.replace('property="og:site_name" content="학계산"', 'property="og:site_name" content="Reridy"')
    if 'property="og:site_name"' not in t:
        t = re.sub(r'(<meta property="og:url"[^>]*>)', r'\1<meta property="og:site_name" content="Reridy">', t, count=1)
    t = t.replace(
        '"@type":"WebSite","name":"학계산","url":"https://reridy.github.io/hakgyesan/"',
        '"@type":"WebSite","name":"Reridy","url":"https://reridy.github.io/"',
    )
    if name == "index.html":
        t = re.sub(
            r'<script type="application/ld\+json">.*?</script>',
            '<script type="application/ld+json">' + collection_ld + '</script>',
            t,
            count=1,
            flags=re.S,
        )
    if 'rel="icon"' not in t:
        t = t.replace("</head>", '<link rel="icon" href="/hakgyesan/favicon.ico"></head>', 1)
    if "Reridy 프로젝트" not in t:
        t = t.replace(
            '<a href="/hakgyesan/contact.html">문의</a>',
            '<a href="/hakgyesan/contact.html">문의</a><a href="/">Reridy 프로젝트</a>',
        )
    (out / name).write_text(t, encoding="utf-8")

hub = """<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Reridy — Projects & Tools</title><meta name="description" content="Reridy가 만드는 웹 도구와 프로젝트를 한곳에서 확인하세요. 학계산과 Paradox Doctor를 제공합니다."><meta name="robots" content="index,follow"><link rel="canonical" href="https://reridy.github.io/"><meta property="og:type" content="website"><meta property="og:locale" content="ko_KR"><meta property="og:title" content="Reridy — Projects & Tools"><meta property="og:description" content="Tools, games and projects by Reridy."><meta property="og:url" content="https://reridy.github.io/"><meta property="og:site_name" content="Reridy"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#111827"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"Reridy","alternateName":["Reridy Projects","reridy.github.io"],"url":"https://reridy.github.io/"}</script><style>:root{--bg:#f7f8fb;--card:#fff;--text:#111827;--muted:#667085;--line:#e5e7eb;--accent:#4f46e5}*{box-sizing:border-box}body{margin:0;font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans KR",sans-serif;background:var(--bg);color:var(--text)}a{color:inherit;text-decoration:none}.wrap{width:min(100% - 32px,960px);margin:auto}.top{padding:26px 0;border-bottom:1px solid var(--line);background:#fff}.brand{font-size:22px;font-weight:900}.hero{padding:76px 0 34px}.hero h1{font-size:clamp(44px,9vw,76px);letter-spacing:-.06em;line-height:1;margin:0 0 18px}.hero p{font-size:18px;color:var(--muted)}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;padding:18px 0 80px}.card{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:26px;box-shadow:0 12px 30px rgba(15,23,42,.06)}.card h2{font-size:25px;margin:0 0 8px}.card p{margin:0 0 18px;color:var(--muted);line-height:1.65}.go{font-weight:800;color:var(--accent)}footer{border-top:1px solid var(--line);padding:28px 0 44px;color:var(--muted);font-size:13px}@media(max-width:700px){.grid{grid-template-columns:1fr}.hero{padding-top:52px}}</style></head><body><header class="top"><div class="wrap"><a class="brand" href="/">Reridy</a></div></header><main><section class="hero"><div class="wrap"><h1>Reridy</h1><p>Tools, games and projects. 필요한 프로젝트를 선택하세요.</p></div></section><section class="wrap grid"><a class="card" href="/hakgyesan/"><h2>학계산</h2><p>한국 학생을 위한 내신 5등급, 시험 목표점수, 수행평가·석차·가중평균 계산 도구.</p><span class="go">학계산 열기 →</span></a><a class="card" href="/paradox-doctor/"><h2>Paradox Doctor</h2><p>HOI4와 Victoria 3 모딩 오류를 분석하고 진단하는 도구.</p><span class="go">Paradox Doctor 열기 →</span></a></section></main><footer><div class="wrap">© 2026 Reridy</div></footer></body></html>"""
Path("index.html").write_text(hub, encoding="utf-8")

nf = """<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>페이지를 찾을 수 없습니다 | Reridy</title><meta name="robots" content="noindex,follow"><meta property="og:site_name" content="Reridy"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><style>body{font-family:system-ui,"Noto Sans KR",sans-serif;background:#f7f8fb;color:#111827}.box{max-width:680px;margin:12vh auto;padding:28px;background:#fff;border:1px solid #e5e7eb;border-radius:20px}a{color:#4f46e5;font-weight:700;margin-right:14px}</style></head><body><main class="box"><h1>404</h1><p>페이지를 찾을 수 없습니다.</p><a href="/">Reridy 홈</a><a href="/hakgyesan/">학계산</a><a href="/paradox-doctor/">Paradox Doctor</a></main></body></html>"""
Path("404.html").write_text(nf, encoding="utf-8")

def stub(name):
    p = f"/hakgyesan/{name}"
    u = f"{PROJ}/{name}"
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>페이지가 이동했습니다 | Reridy</title><meta name="robots" content="index,follow"><link rel="canonical" href="{u}"><meta http-equiv="refresh" content="0; url={p}"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><script>location.replace({json.dumps(p)});</script></head><body><p>학계산 페이지가 이동했습니다. <a href="{p}">새 주소로 이동하기</a></p></body></html>'''

for name in LEGACY:
    Path(name).write_text(stub(name), encoding="utf-8")

Path("favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#111827"/><path fill="#fff" d="M18 14h17c9.5 0 15 4.8 15 12.5 0 5.7-3.1 9.8-8.6 11.5L52 50H40.5l-9-10.8H28V50H18V14Zm10 8v9h6.5c3.7 0 5.5-1.5 5.5-4.5S38.2 22 34.5 22H28Z"/></svg>', encoding="utf-8")
Path("favicon.ico").unlink(missing_ok=True)

urls = [SITE + "/", PROJ + "/"] + [f"{PROJ}/{x}" for x in LEGACY] + [SITE + "/paradox-doctor/"]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    lm = "" if u.endswith("/paradox-doctor/") else f"<lastmod>{DATE}</lastmod>"
    sm.append(f"  <url><loc>{u}</loc>{lm}</url>")
sm.append("</urlset>")
Path("sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")

w = Path(".github/workflows/indexnow.yml").read_text(encoding="utf-8")
w = w.replace(
    'elif any(path.startswith("assets/") or path == "sitemap.xml" for _, path in changed):',
    'elif any(path.startswith("assets/") or path.startswith("hakgyesan/assets/") or path == "hakgyesan/favicon.ico" or path == "favicon.svg" or path == "sitemap.xml" for _, path in changed):',
)
w = w.replace(
'''                      if path == "index.html":
                          urls.add(base + "/")
                      else:
                          urls.add(base + "/" + path)''',
'''                      if path == "index.html":
                          candidate = base + "/"
                      elif path == "hakgyesan/index.html":
                          candidate = base + "/hakgyesan/"
                      else:
                          candidate = base + "/" + path
                      if candidate in all_sitemap_urls():
                          urls.add(candidate)''')
Path(".github/workflows/indexnow.yml").write_text(w, encoding="utf-8")

Path("README.md").write_text(
    "# Reridy.github.io\n\nReridy project hub.\n\n- `/hakgyesan/` — 학계산\n- `/paradox-doctor/` — Paradox Doctor\n\nLegacy root-level 학계산 URLs are kept as one-to-one migration pages.\n",
    encoding="utf-8",
)

assert Path("google1d299fe25c6bb58d.html").exists()
assert Path("7621ed28513dd4db0fe8526c91f86918.txt").exists()
assert '"@type":"WebSite","name":"Reridy"' in Path("index.html").read_text(encoding="utf-8")
assert "G-WJ5VS87EKY" not in Path("index.html").read_text(encoding="utf-8")
assert Path("hakgyesan/favicon.ico").exists() and not Path("favicon.ico").exists()

for name in PAGES:
    t = (out / name).read_text(encoding="utf-8")
    c = PROJ + "/" if name == "index.html" else f"{PROJ}/{name}"
    assert f'rel="canonical" href="{c}"' in t, (name, "canonical")
    assert f'property="og:url" content="{c}"' in t, (name, "og")
    assert 'property="og:site_name" content="Reridy"' in t, (name, "site_name")
    assert 'href="/assets/' not in t and 'src="/assets/' not in t, (name, "assets")
    for old in LEGACY:
        assert f'href="/{old}"' not in t, (name, old)

assert '"@type":"CollectionPage"' in (out / "index.html").read_text(encoding="utf-8")
for name in LEGACY:
    t = Path(name).read_text(encoding="utf-8")
    assert f'url=/hakgyesan/{name}' in t and f'{PROJ}/{name}' in t
    assert "G-WJ5VS87EKY" not in t

ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
got = {x.text for x in ET.parse("sitemap.xml").getroot().findall("s:url/s:loc", ns)}
assert got == set(urls)

print("migration prepared:", len(PAGES), "project pages,", len(LEGACY), "legacy stubs,", len(urls), "sitemap URLs")