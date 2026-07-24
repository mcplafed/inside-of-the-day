from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent
html = root / "infographic.html"
assets = root.parent / "assets"
assets.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=3)
    errors = []
    page.on("console", lambda msg: errors.append(f"console {msg.type}: {msg.text}") if msg.type == "error" else None)
    page.goto(html.as_uri(), wait_until="networkidle")
    overflow = page.evaluate("""() => {
      const canvas = document.querySelector('.canvas');
      return {
        scrollWidth: canvas.scrollWidth, clientWidth: canvas.clientWidth,
        scrollHeight: canvas.scrollHeight, clientHeight: canvas.clientHeight
      };
    }""")
    if overflow["scrollWidth"] != overflow["clientWidth"] or overflow["scrollHeight"] != overflow["clientHeight"]:
        raise RuntimeError(f"Canvas overflow: {overflow}")
    if errors:
        raise RuntimeError("\n".join(errors))
    page.locator(".canvas").screenshot(path=str(assets / "infographic.png"))
    page.screenshot(path=str(assets / "mobile-probe.png"), clip={"x": 0, "y": 0, "width": 1080, "height": 1350}, scale="css")
    browser.close()

# The exact production image is 3240x4050. Create a 400x500 nearest full-image probe.
from PIL import Image
with Image.open(assets / "infographic.png") as image:
    if image.size != (3240, 4050):
        raise RuntimeError(f"Unexpected production dimensions: {image.size}")
    image.resize((400, 500), Image.Resampling.LANCZOS).save(assets / "mobile-probe.png")
