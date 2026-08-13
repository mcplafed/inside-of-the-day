#!/usr/bin/env python3
"""Render post 15 and fail on canvas/card overflow or unreadable line expansion."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / 'source' / 'infographic.html'
OUT = ROOT / 'assets' / 'infographic.png'
PROBE = ROOT / 'assets' / 'infographic-mobile-probe.png'
OUT.parent.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=3)
    page.goto(HTML.as_uri(), wait_until='load')
    errors = []
    page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' else None)
    data = page.evaluate('''() => {
      const c=document.querySelector('.page').getBoundingClientRect();
      const all=[...document.querySelectorAll('.page *')];
      const bad=all.filter(e=>{const r=e.getBoundingClientRect();return r.right>c.right+.5||r.bottom>c.bottom+.5||r.left<c.left-.5||r.top<c.top-.5}).map(e=>e.className||e.tagName);
      const rows=[...document.querySelectorAll('h1,.dek,.signal,.check h2,.check p,.next p,.commerce,.takeaway,.foot')].map(e=>({text:e.textContent.trim().slice(0,70),lines:Math.round(e.getBoundingClientRect().height/parseFloat(getComputedStyle(e).lineHeight))}));
      return {canvas:[c.width,c.height],bad,rows};
    }''')
    if data['bad']:
        raise SystemExit('layout overflow: ' + ', '.join(data['bad']))
    if any(x['lines'] > 3 for x in data['rows']):
        raise SystemExit('unexpected dense copy: ' + repr([x for x in data['rows'] if x['lines'] > 3]))
    page.screenshot(path=str(OUT), type='png')
    browser.close()

from PIL import Image
with Image.open(OUT) as image:
    image.resize((400, 500), Image.Resampling.LANCZOS).save(PROBE)
print('layout OK: no canvas overflow')
for x in data['rows']:
    print(f"lines[{x['lines']}] {x['text']}")
print(f'wrote {OUT}')
print('render size: 3240x4050')
print(f'wrote {PROBE}')
