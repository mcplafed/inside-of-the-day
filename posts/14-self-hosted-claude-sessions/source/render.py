#!/usr/bin/env python3
"""Deterministic render of infographic.html to a 3240x4050 PNG plus a mobile probe.

Renders the self-contained HTML at the 1080x1350 logical canvas with a device
scale factor of 3 (matching the series). Also emits a 400x500 downscaled probe
used to check that the headline + hook question, the eligibility badge, the
mechanism flow (web/mobile/desktop -> your self-hosted runner -> repo/CI/tools/
policies) and the three outcome cards (three label-free full-width rows each:
mechanism / use case / boundary) stay legible at LinkedIn mobile-feed size.

Usage: python3 render.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
SRC = HERE / "infographic.html"
OUT = HERE.parent / "assets" / "infographic.png"
PROBE = HERE.parent / "assets" / "infographic-mobile-probe.png"

WIDTH, HEIGHT, SCALE = 1080, 1350, 3
PROBE_WIDTH, PROBE_HEIGHT = 400, 500

# Panels that clip their own content when it grows: the canvas plus every
# overflow:hidden card. A silent overflow here means unreadable substantive text.
GUARDED = [".canvas", ".card.cA", ".card.cB", ".card.cC"]

# Text that must stay on its intended line count or the layout intent breaks
# (flow chips, runner label, badge, card titles, card body rows, boundary note,
# secrets strip). Card body rows are substantive copy: max 2 rendered lines each.
NOWRAP_CHECK = [".chip", ".runner .t", ".badge", ".card .hd .t", ".card .bd .row", ".split", ".secrets", ".hero"]


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": WIDTH, "height": HEIGHT},
            device_scale_factor=SCALE,
        )
        page.goto(SRC.as_uri())
        page.wait_for_timeout(150)

        overflow = page.evaluate(
            "sels => sels.map(sel => {"
            " const el = document.querySelector(sel);"
            " return [sel, el.scrollHeight - el.clientHeight];"
            "}).filter(([, d]) => d > 0);",
            GUARDED,
        )
        for sel, delta in overflow:
            print(f"WARNING: {sel} content overflows by {delta}px")
        if not overflow:
            print("layout OK: no panel overflows")

        # Report how many rendered lines each measured text block occupies, so a
        # copy edit that silently pushes a line into a second row is visible.
        lines = page.evaluate(
            "sels => sels.flatMap(sel => [...document.querySelectorAll(sel)].map(el => {"
            " const lh = parseFloat(getComputedStyle(el).lineHeight);"
            " const n = Math.round(el.getBoundingClientRect().height / lh);"
            " return [sel, el.textContent.trim().slice(0, 46), n];"
            "}));",
            NOWRAP_CHECK,
        )
        for sel, text, n in lines:
            flag = "" if n <= 2 else "  <-- CHECK"
            print(f"lines[{n}] {sel}: {text}{flag}")

        page.screenshot(path=str(OUT), clip={"x": 0, "y": 0, "width": WIDTH, "height": HEIGHT})
        browser.close()
    print(f"wrote {OUT}")

    # Mobile probe: downscale the full render to the LinkedIn mobile-feed size.
    from PIL import Image

    img = Image.open(OUT)
    print(f"render size: {img.size[0]}x{img.size[1]}")
    probe = img.resize((PROBE_WIDTH, PROBE_HEIGHT), Image.LANCZOS)
    probe.save(PROBE)
    print(f"wrote {PROBE}")


if __name__ == "__main__":
    main()
