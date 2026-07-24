#!/usr/bin/env python3
"""Deterministic render of infographic.html to a 3240x4050 PNG.

Renders the self-contained HTML at the 1080x1350 logical canvas with a
device scale factor of 3, matching the other posts in the series.

Usage: python3 render.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
SRC = HERE / "infographic.html"
OUT = HERE.parent / "assets" / "infographic.png"

WIDTH, HEIGHT, SCALE = 1080, 1350, 3


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
        page.screenshot(path=str(OUT), clip={"x": 0, "y": 0, "width": WIDTH, "height": HEIGHT})
        browser.close()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
