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


def rewrite_index() -> None:
    if not INDEX.exists():
        raise FileNotFoundError("index.html not found")

    html = INDEX.read_text(encoding="utf-8")
    html = replace_unsplash_urls(html)

    if "images.unsplash.com" in html:
        raise RuntimeError("Remote Unsplash image references remain in index.html")

    for name in ("food-products", "plastic-products", "sweets-snacks"):
        for variant in VARIANTS:
            if f"assets/images/{name}-{variant}.webp" not in html:
                raise RuntimeError(f"Responsive {variant} asset is not referenced for {name}")
    if "assets/images/warehouse-desktop.webp" not in html:
        raise RuntimeError("Warehouse WebP asset is not referenced")

    INDEX.write_text(html, encoding="utf-8")
    print("Updated index.html to use local responsive WebP assets")


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
