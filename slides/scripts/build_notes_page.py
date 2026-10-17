#!/usr/bin/env python3
"""Build site/public/presenter-notes.html from slides/slides.md (single SSoT).

Extracts per-slide: the `<!-- Slide N: ... -->` title comment, the on-slide
deck title, and the speaker-notes comment block (speech script, pronunciation,
Chinese gist, Q&A memo). Output is a self-contained static page linked from
the report sidebar MATERIALS. Re-run after any speaker-note change:

    python3 slides/scripts/build_notes_page.py
"""
import html
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "slides.md"
OUT = ROOT.parent / "site" / "public" / "presenter-notes.html"

md = SRC.read_text(encoding="utf-8")
raw_slides = re.split(r"\n---\n", md)
# drop YAML headmatter (first chunk starts with '---')
chunks = raw_slides[1:] if raw_slides and raw_slides[0].strip().startswith("---") else raw_slides

slides = []
for chunk in chunks:
    m_title = re.search(r"<!--\s*(Slide [^:>]+?:\s*.+?)\s*-->", chunk)
    title = m_title.group(1) if m_title else "Slide"
    m_dt = re.search(
        r'class="(?:deck-title|cover-title)"[^>]*>\s*(.*?)\s*</div>', chunk, re.S
    )
    on_slide = ""
    if m_dt:
        on_slide = re.sub(r"<br\s*/?>", " / ", m_dt.group(1)).strip()
    m_notes = re.search(r"<!--\s*\n(Notes\b.*?)\n-->", chunk, re.S)
    notes = m_notes.group(1).strip() if m_notes else "(no notes)"
    slides.append((title, on_slide, notes))

cards = []
for i, (title, on_slide, notes) in enumerate(slides, 1):
    cards.append(f"""
    <section class="card">
      <h2><span class="no">{i:02d}</span>{html.escape(title)}</h2>
      {f'<p class="on-slide">{html.escape(on_slide)}</p>' if on_slide else ''}
      <pre>{html.escape(notes)}</pre>
    </section>""")

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Presenter Script — Presentation 2 · ADS401 Group A</title>
<style>
  :root {{ --ink:#172327; --teal:#183f46; --muted:#687780; --line:#ced5d7;
          --accent:#1683a5; --paper:#f8fafc; }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; padding:2.2rem 1.2rem 4rem; background:#fff; color:var(--ink);
         font:16px/1.55 Inter,'Helvetica Neue',Arial,sans-serif; }}
  main {{ max-width: 860px; margin: 0 auto; }}
  h1 {{ font:700 1.9rem/1.25 Newsreader,Georgia,serif; color:var(--teal); margin:0 0 .2rem; }}
  .meta {{ color:var(--muted); font-size:.9rem; margin:0 0 1.6rem; }}
  .card {{ border:1px solid var(--line); border-left:3px solid var(--teal);
          border-radius:0 6px 6px 0; background:var(--paper);
          padding:1rem 1.2rem; margin:0 0 1.1rem; }}
  h2 {{ font-size:1rem; margin:0 0 .5rem; color:var(--teal); }}
  .no {{ color:var(--accent); font-weight:800; margin-right:.55rem; }}
  .on-slide {{ margin:0 0 .55rem; font-size:.82rem; color:var(--muted); font-style:italic; }}
  pre {{ margin:0; white-space:pre-wrap; word-break:break-word; font:500 .86rem/1.62
        ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; color:var(--ink); }}
  @media print {{ body {{ padding:0; }} .card {{ break-inside:avoid; }} }}
</style>
</head>
<body>
<main>
  <h1>Presenter Script — Presentation 2</h1>
  <p class="meta">Speaker: Haode SHEN · 19 October 2026 · target 170–180 s ·
     derived from <code>slides/slides.md</code> notes · regenerate:
     <code>slides/scripts/build_notes_page.py</code></p>
  {''.join(cards)}
</main>
</body>
</html>
"""

OUT.write_text(page, encoding="utf-8")
print(f"wrote {OUT} ({len(slides)} slides)")
