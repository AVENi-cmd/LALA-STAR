from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
ASSET_DIR = ROOT / "assets" / "optimized"
ASSET_VERSION = "20260915-12"
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
        "assets/optimized/warehouse-hero-1600.webp": f"assets/optimized/wholesale-warehouse-ahsa-1920.webp?v={ASSET_VERSION}",
        "assets/optimized/warehouse-hero-1280.webp": f"assets/optimized/wholesale-warehouse-ahsa-1280.webp?v={ASSET_VERSION}",
        "assets/optimized/warehouse-hero-640.webp": f"assets/optimized/wholesale-warehouse-ahsa-640.webp?v={ASSET_VERSION}",
        "assets/images/warehouse-desktop.webp": f"assets/optimized/wholesale-warehouse-ahsa-1920.webp?v={ASSET_VERSION}",
        "assets/images/warehouse-tablet.webp": f"assets/optimized/wholesale-warehouse-ahsa-1280.webp?v={ASSET_VERSION}",
        "assets/images/warehouse-mobile.webp": f"assets/optimized/wholesale-warehouse-ahsa-640.webp?v={ASSET_VERSION}",
        "assets/optimized/food-products-1600.webp": f"assets/optimized/food-products-ahsa-1280.webp?v={ASSET_VERSION}",
        "assets/optimized/food-products-1280.webp": f"assets/optimized/food-products-ahsa-1280.webp?v={ASSET_VERSION}",
        "assets/optimized/food-products-640.webp": f"assets/optimized/food-products-ahsa-640.webp?v={ASSET_VERSION}",
        "assets/optimized/plastic-products-1600.webp": f"assets/optimized/plastic-products-1280.webp?v={ASSET_VERSION}",
        "assets/optimized/plastic-products-1280.webp": f"assets/optimized/plastic-products-1280.webp?v={ASSET_VERSION}",
        "assets/optimized/plastic-products-640.webp": f"assets/optimized/plastic-products-640.webp?v={ASSET_VERSION}",
        "assets/optimized/sweets-snacks-1600.webp": f"assets/optimized/sweets-snacks-1280.webp?v={ASSET_VERSION}",
        "assets/optimized/sweets-snacks-1280.webp": f"assets/optimized/sweets-snacks-1280.webp?v={ASSET_VERSION}",
        "assets/optimized/sweets-snacks-640.webp": f"assets/optimized/sweets-snacks-640.webp?v={ASSET_VERSION}",
    }
    for old, new in replacements.items():
        html = html.replace(old, new)
    for old, new in {
        "assets/images/food-products-desktop.webp": "assets/optimized/food-products-ahsa-1280.webp",
        "assets/images/food-products-tablet.webp": "assets/optimized/food-products-ahsa-1280.webp",
        "assets/images/food-products-mobile.webp": "assets/optimized/food-products-ahsa-640.webp",
        "assets/images/plastic-products-desktop.webp": "assets/optimized/plastic-products-1280.webp",
        "assets/images/plastic-products-tablet.webp": "assets/optimized/plastic-products-1280.webp",
        "assets/images/plastic-products-mobile.webp": "assets/optimized/plastic-products-640.webp",
        "assets/images/sweets-snacks-desktop.webp": "assets/optimized/sweets-snacks-1280.webp",
        "assets/images/sweets-snacks-tablet.webp": "assets/optimized/sweets-snacks-1280.webp",
        "assets/images/sweets-snacks-mobile.webp": "assets/optimized/sweets-snacks-640.webp",
    }.items():
        html = html.replace(old, new)
    html = re.sub(r'https://images\\.unsplash\\.com/photo-[^\"\'\\s>)]+', 'BLOCKED_REMOTE_IMAGE_REFERENCE', html)
    return html


def inject_i18n(html):
    html = re.sub(r'<script[^>]*src=["\']assets/i18n\\.js[^>]*></script>', '', html)
    html = re.sub(r'<script[^>]*>.*?document\\.getElementById\\(["\']langBtn["\']\\).*?</script>', '', html, flags=re.DOTALL)
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
    if 'images.unsplash.com' in html or 'BLOCKED_REMOTE_IMAGE_REFERENCE' in html:
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
