from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
ASSET_DIR = ROOT / "assets" / "optimized"
ASSET_VERSION = "20260915-13"
SEO_MARKER = '<meta name="lalastar-seo-v1" content="managed-by-build-webp">'

APPROVED = {
    "food-ahsa-640": ASSET_DIR / "food-products-ahsa-640.webp",
    "food-ahsa-1280": ASSET_DIR / "food-products-ahsa-1280.webp",
    "food-dammam-640": ASSET_DIR / "food-products-dammam-640.webp",
    "food-dammam-1280": ASSET_DIR / "food-products-dammam-1280.webp",
    "plastic-640": ASSET_DIR / "plastic-products-640.webp",
    "plastic-1280": ASSET_DIR / "plastic-products-1280.webp",
    "sweets-640": ASSET_DIR / "sweets-snacks-640.webp",
    "sweets-1280": ASSET_DIR / "sweets-snacks-1280.webp",
    "warehouse-640": ASSET_DIR / "wholesale-warehouse-ahsa-640.webp",
    "warehouse-1280": ASSET_DIR / "wholesale-warehouse-ahsa-1280.webp",
    "warehouse-1920": ASSET_DIR / "wholesale-warehouse-ahsa-1920.webp",
}


def validate_approved_assets():
    from PIL import Image
    for name, path in APPROVED.items():
        if not path.is_file() or path.stat().st_size < 5000:
            raise RuntimeError(f"Missing or suspiciously small approved image: {name} -> {path}")
        data = path.read_bytes()
        if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
            raise RuntimeError(f"Invalid WebP signature: {path}")
        with Image.open(path) as im:
            if im.format != "WEBP":
                raise RuntimeError(f"Invalid WebP format: {path}")


def replace_image_refs(html):
    replacements = {
        r"assets/optimized/warehouse-hero-1600\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/wholesale-warehouse-ahsa-1920.webp?v={ASSET_VERSION}",
        r"assets/optimized/warehouse-hero-1280\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/wholesale-warehouse-ahsa-1280.webp?v={ASSET_VERSION}",
        r"assets/optimized/warehouse-hero-640\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/wholesale-warehouse-ahsa-640.webp?v={ASSET_VERSION}",
        r"assets/images/warehouse-(?:desktop|tablet|mobile)\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/wholesale-warehouse-ahsa-1920.webp?v={ASSET_VERSION}",
        r"assets/optimized/food-products-1600\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/food-products-ahsa-1280.webp?v={ASSET_VERSION}",
        r"assets/optimized/food-products-1280\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/food-products-ahsa-1280.webp?v={ASSET_VERSION}",
        r"assets/optimized/food-products-640\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/food-products-ahsa-640.webp?v={ASSET_VERSION}",
        r"assets/optimized/plastic-products-1600\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/plastic-products-1280.webp?v={ASSET_VERSION}",
        r"assets/optimized/plastic-products-1280\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/plastic-products-1280.webp?v={ASSET_VERSION}",
        r"assets/optimized/plastic-products-640\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/plastic-products-640.webp?v={ASSET_VERSION}",
        r"assets/optimized/sweets-snacks-1600\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/sweets-snacks-1280.webp?v={ASSET_VERSION}",
        r"assets/optimized/sweets-snacks-1280\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/sweets-snacks-1280.webp?v={ASSET_VERSION}",
        r"assets/optimized/sweets-snacks-640\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/sweets-snacks-640.webp?v={ASSET_VERSION}",
        r"assets/images/food-products-(?:desktop|tablet)\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/food-products-ahsa-1280.webp?v={ASSET_VERSION}",
        r"assets/images/food-products-mobile\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/food-products-ahsa-640.webp?v={ASSET_VERSION}",
        r"assets/images/plastic-products-(?:desktop|tablet)\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/plastic-products-1280.webp?v={ASSET_VERSION}",
        r"assets/images/plastic-products-mobile\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/plastic-products-640.webp?v={ASSET_VERSION}",
        r"assets/images/sweets-snacks-(?:desktop|tablet)\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/sweets-snacks-1280.webp?v={ASSET_VERSION}",
        r"assets/images/sweets-snacks-mobile\.webp(?:\?v=[^\"'\s)]+)?": f"assets/optimized/sweets-snacks-640.webp?v={ASSET_VERSION}",
    }
    for pattern, new in replacements.items():
        html = re.sub(pattern, new, html)
    return html


def inject_i18n(html):
    html = re.sub(r'<script[^>]*src=["\']assets/i18n\.js[^>]*></script>', '', html)
    html = re.sub(r'<script[^>]*>.*?document\.getElementById\(["\']langBtn["\']\).*?</script>', '', html, flags=re.DOTALL)
    return html.replace('</body>', '<script src="assets/i18n.js" defer></script></body>', 1)


def clean_preloads(html):
    html = re.sub(r'<link rel="preload" as="image" href="assets/(?:images|optimized)/warehouse[^>]*>', '', html)
    pre = (
        f'<link rel="preload" as="image" href="assets/optimized/wholesale-warehouse-ahsa-1920.webp?v={ASSET_VERSION}" fetchpriority="high" media="(min-width:851px)">'
        f'<link rel="preload" as="image" href="assets/optimized/wholesale-warehouse-ahsa-640.webp?v={ASSET_VERSION}" fetchpriority="high" media="(max-width:850px)">'
    )
    return html.replace('<meta name="viewport"', pre + '<meta name="viewport"', 1)


def ensure_title(html):
    if '<title>' in html and '</title>' in html:
        return html
    return html.replace('</head>', '<title>شركة لألأة النجوم التجارية | LALA STAR TRADING CO.</title></head>', 1)


def main():
    validate_approved_assets()
    html = INDEX.read_text(encoding="utf-8")
    html = replace_image_refs(html)
    if 'images.unsplash.com' in html:
        raise RuntimeError('Remote image references remain in index.html')
    html = clean_preloads(html)
    html = ensure_title(html)
    html = inject_i18n(html)
    if 'assets/i18n.js' not in html:
        raise RuntimeError('i18n script was not wired into index.html')
    if SEO_MARKER not in html:
        raise RuntimeError('SEO marker missing')
    INDEX.write_text(html, encoding='utf-8')


if __name__ == '__main__':
    main()
