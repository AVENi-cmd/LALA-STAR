from pathlib import Path
import re
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "assets" / "images"
INDEX = ROOT / "index.html"
ASSET_VERSION = "20260914"
EXPECTED = [
    "warehouse-desktop.webp", "warehouse-tablet.webp", "warehouse-mobile.webp",
    "food-products-desktop.webp", "food-products-tablet.webp", "food-products-mobile.webp",
    "plastic-products-desktop.webp", "plastic-products-tablet.webp", "plastic-products-mobile.webp",
    "sweets-snacks-desktop.webp", "sweets-snacks-tablet.webp", "sweets-snacks-mobile.webp",
]
SEO_MARKER = '<meta name="lalastar-seo-v1" content="managed-by-build-webp">'

def validate_assets():
    for name in EXPECTED:
        p = OUTPUT_DIR / name
        if not p.exists() or p.stat().st_size == 0:
            raise RuntimeError(f"Missing image asset: {p}")
        data = p.read_bytes()
        if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
            raise RuntimeError(f"Invalid WebP signature: {p}")
        with Image.open(p) as im:
            if im.format != "WEBP":
                raise RuntimeError(f"Invalid WebP format: {p}")

def version_assets(html):
    pattern = r'assets/images/(warehouse(?:-desktop|-mobile|-tablet)|food-products(?:-desktop|-mobile|-tablet)|plastic-products(?:-desktop|-mobile|-tablet)|sweets-snacks(?:-desktop|-mobile|-tablet))\.webp(?:\?v=[^\s\"\']+)?'
    return re.sub(pattern, rf'assets/images/\1.webp?v={ASSET_VERSION}', html)

def inject_i18n(html):
    html = re.sub(r'<script[^>]*src=["\']assets/i18n\.js[^>]*></script>', '', html)
    return html.replace('</body>', '<script src="assets/i18n.js" defer></script></body>', 1)

def clean_duplicate_preloads(html):
    preload = '<link rel="preload" as="image" href="assets/images/warehouse-desktop.webp?v=20260914" fetchpriority="high" media="(min-width:851px)"><link rel="preload" as="image" href="assets/images/warehouse-mobile.webp?v=20260914" fetchpriority="high" media="(max-width:850px)">'
    html = re.sub(r'(?:<link rel="preload" as="image" href="assets/images/warehouse-desktop\.webp\?v=20260914"[^>]*>\s*){2,}', preload, html)
    html = re.sub(r'(?:<link rel="preload" as="image" href="assets/images/warehouse-mobile\.webp\?v=20260914"[^>]*>\s*){2,}', '', html)
    return html

def main():
    validate_assets()
    html = INDEX.read_text(encoding="utf-8")
    if "images.unsplash.com" in html:
        raise RuntimeError("Remote Unsplash references remain in index.html")
    html = version_assets(html)
    html = clean_duplicate_preloads(html)
    html = inject_i18n(html)
    if 'assets/i18n.js' not in html:
        raise RuntimeError("i18n script was not wired into index.html")
    if SEO_MARKER not in html:
        raise RuntimeError("SEO marker missing")
    INDEX.write_text(html, encoding="utf-8")

if __name__ == "__main__": main()
