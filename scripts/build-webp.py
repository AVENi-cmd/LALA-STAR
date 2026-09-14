from pathlib import Path
from PIL import Image, ImageOps
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "assets" / "optimized"
OUTPUT_DIR = ROOT / "assets" / "images"
INDEX = ROOT / "index.html"

SOURCES = {
    "warehouse": SOURCE_DIR / "warehouse-hero-1600.webp",
    "food-products": SOURCE_DIR / "food-products-1600.webp",
    "plastic-products": SOURCE_DIR / "plastic-products-1600.webp",
    "sweets-snacks": SOURCE_DIR / "sweets-snacks-1600.webp",
}

VARIANTS = {
    "desktop": (1920, 1080),
    "tablet": (1024, 1024),
    "mobile": (750, 1000),
}

QUALITY = 88

SEO_MARKER = '<meta name="lalastar-seo-v1" content="managed-by-build-webp">'
SEO_BLOCK = '''<meta name="lalastar-seo-v1" content="managed-by-build-webp"><meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="https://aveni-cmd.github.io/LALA-STAR/"><meta property="og:type" content="website"><meta property="og:locale" content="ar_SA"><meta property="og:site_name" content="شركة لألأة النجوم التجارية | LALA STAR TRADING CO."><meta property="og:title" content="شركة لألأة النجوم التجارية | LALA STAR TRADING CO."><meta property="og:description" content="شركة لألأة النجوم التجارية — بيع المواد الغذائية بالجملة منذ 1993، مع أنشطة البلاستيك والحلويات والوجبات الخفيفة في الدمام والأحساء."><meta property="og:url" content="https://aveni-cmd.github.io/LALA-STAR/"><meta property="og:image" content="https://aveni-cmd.github.io/LALA-STAR/assets/images/warehouse-desktop.webp"><meta property="og:image:alt" content="مستودع تجاري للمواد والسلع بالجملة"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="شركة لألأة النجوم التجارية | LALA STAR TRADING CO."><meta name="twitter:description" content="بيع المواد الغذائية بالجملة منذ 1993، مع أنشطة البلاستيك والحلويات والوجبات الخفيفة."><meta name="twitter:image" content="https://aveni-cmd.github.io/LALA-STAR/assets/images/warehouse-desktop.webp"><script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"شركة لألأة النجوم التجارية","alternateName":"LALA STAR TRADING CO.","description":"شركة لبيع المواد الغذائية بالجملة، مع أنشطة مستقلة في المنتجات البلاستيكية والحلويات والوجبات الخفيفة.","foundingDate":"1993","telephone":"0138562508","email":"starcoldstore@yahoo.com","url":"https://aveni-cmd.github.io/LALA-STAR/","logo":"https://aveni-cmd.github.io/LALA-STAR/assets/lala-star-logo.png","address":{"@type":"PostalAddress","addressLocality":"Dammam","addressCountry":"SA"},"areaServed":"SA"}</script>'''


def find_source(name: str, preferred: Path) -> Path:
    if preferred.exists():
        return preferred
    candidates = sorted(SOURCE_DIR.glob(f"{name}*.webp"))
    if not candidates:
        raise FileNotFoundError(f"No valid WebP source found for: {name}")
    return candidates[-1]


def build_one(source: Path, output: Path, size: tuple[int, int]) -> None:
    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        rendered = ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
        output.parent.mkdir(parents=True, exist_ok=True)
        rendered.save(output, format="WEBP", quality=QUALITY, method=6)

    data = output.read_bytes()
    if len(data) < 12 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise RuntimeError(f"Invalid RIFF/WEBP output: {output}")
    with Image.open(output) as check:
        if check.format != "WEBP" or check.size != size:
            raise RuntimeError(f"Invalid output metadata: {output}")
    print(f"OK {output} | {size[0]}x{size[1]} | {len(data)} bytes")


def replace_unsplash_urls(html: str) -> str:
    sources = {
        "1645736315000-6f788915923b": "warehouse",
        "1773946836315-bd8269b62b93": "food-products",
        "1713900105420-67ae6dbf3595": "plastic-products",
        "1759167632930-298bca6b4268": "sweets-snacks",
    }

    url_pattern = re.compile(r"https://images\.unsplash\.com/photo-([0-9]+-[a-z0-9]+)\?[^\"'\s>)]+")

    def repl(match: re.Match[str]) -> str:
        photo_id = match.group(1)
        name = sources.get(photo_id)
        if not name:
            return match.group(0)
        full = match.group(0)
        width_match = re.search(r"[?&]w=(\d+)", full)
        width = int(width_match.group(1)) if width_match else 2400
        if name == "warehouse":
            return "assets/images/warehouse-desktop.webp"
        if width <= 640:
            return f"assets/images/{name}-mobile.webp"
        if width <= 1280:
            return f"assets/images/{name}-tablet.webp"
        return f"assets/images/{name}-desktop.webp"

    return url_pattern.sub(repl, html)


def inject_seo(html: str) -> str:
    html = re.sub(r'<meta name="lalastar-seo-v1"[^>]*>.*?</script>', '', html, count=1, flags=re.DOTALL)
    marker = '<meta charset="utf-8">'
    if marker not in html:
        raise RuntimeError("Unable to locate document charset marker for SEO metadata")
    return html.replace(marker, marker + SEO_BLOCK, 1)


def rewrite_index() -> None:
    if not INDEX.exists():
        raise FileNotFoundError("index.html not found")

    html = INDEX.read_text(encoding="utf-8")
    html = replace_unsplash_urls(html)
    html = inject_seo(html)

    if "images.unsplash.com" in html:
        raise RuntimeError("Remote Unsplash image references remain in index.html")

    for name in ("food-products", "plastic-products", "sweets-snacks"):
        for variant in VARIANTS:
            if f"assets/images/{name}-{variant}.webp" not in html:
                raise RuntimeError(f"Responsive {variant} asset is not referenced for {name}")
    if "assets/images/warehouse-desktop.webp" not in html:
        raise RuntimeError("Warehouse WebP asset is not referenced")
    for required in (SEO_MARKER, 'rel="canonical"', 'property="og:title"', 'name="twitter:card"', 'application/ld+json'):
        if required not in html:
            raise RuntimeError(f"SEO metadata missing: {required}")

    INDEX.write_text(html, encoding="utf-8")
    print("Updated index.html to use local responsive WebP assets and managed SEO metadata")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, preferred in SOURCES.items():
        source = find_source(name, preferred)
        print(f"Source: {source}")
        for variant, size in VARIANTS.items():
            build_one(source, OUTPUT_DIR / f"{name}-{variant}.webp", size)
    rewrite_index()


if __name__ == "__main__":
    main()
