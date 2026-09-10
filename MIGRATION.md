# 학계산 URL migration

Migration date: 2026-09-10

The 학계산 project moved from root-level URLs on `https://reridy.github.io/` to `https://reridy.github.io/hakgyesan/` so the root host can represent the shared `Reridy` project brand.

## URL mapping

| Legacy URL | Canonical URL |
| --- | --- |
| `/grade-5.html` | `/hakgyesan/grade-5.html` |
| `/rank-cut.html` | `/hakgyesan/rank-cut.html` |
| `/grade-boundary.html` | `/hakgyesan/grade-boundary.html` |
| `/rank-percentile.html` | `/hakgyesan/rank-percentile.html` |
| `/target-rank.html` | `/hakgyesan/target-rank.html` |
| `/exam-target.html` | `/hakgyesan/exam-target.html` |
| `/midterm-target.html` | `/hakgyesan/midterm-target.html` |
| `/performance-target.html` | `/hakgyesan/performance-target.html` |
| `/weighted-score.html` | `/hakgyesan/weighted-score.html` |
| `/score-contribution.html` | `/hakgyesan/score-contribution.html` |
| `/target-average.html` | `/hakgyesan/target-average.html` |
| `/subject-weighted-average.html` | `/hakgyesan/subject-weighted-average.html` |
| `/five-grade-guide.html` | `/hakgyesan/five-grade-guide.html` |
| `/about.html` | `/hakgyesan/about.html` |
| `/privacy.html` | `/hakgyesan/privacy.html` |
| `/contact.html` | `/hakgyesan/contact.html` |

The former 학계산 home `/` cannot be redirected because `/` is now the Reridy project hub. The hub links prominently to `/hakgyesan/`.

## Legacy URL retention

Root-level legacy HTML files are intentional one-to-one migration pages using an immediate meta refresh, JavaScript `location.replace`, a canonical pointing to the matching `/hakgyesan/` URL, and a visible fallback link. They are not server-side HTTP 301 redirects.

Keep these legacy migration pages for at least one year after the migration (through 2027-09-10), and preferably longer, so old search results and external links continue to reach the matching page.

## Host-level files

Keep these at the root:

- `robots.txt`
- `sitemap.xml`
- `google1d299fe25c6bb58d.html`
- `7621ed28513dd4db0fe8526c91f86918.txt`
- neutral Reridy favicon

The root sitemap lists canonical project URLs only; legacy migration URLs must not be re-added.
