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


def rewrite_index() -> None:
    if not INDEX.exists():
        raise FileNotFoundError("index.html not found")

    html = INDEX.read_text(encoding="utf-8")
    original = html

    remote_map = {
        "https://images.unsplash.com/photo-1645736315000-6f788915923b?auto=format&fit=crop&fm=jpg&q=88&w=2400": "assets/images/warehouse-desktop.webp",
        "https://images.unsplash.com/photo-1773946836315-bd8269b62b93?auto=format&fit=crop&fm=jpg&q=88&w=640": "assets/images/food-products-mobile.webp",
        "https://images.unsplash.com/photo-1773946836315-bd8269b62b93?auto=format&fit=crop&fm=jpg&q=88&w=1280": "assets/images/food-products-tablet.webp",
        "https://images.unsplash.com/photo-1773946836315-bd8269b62b93?auto=format&fit=crop&fm=jpg&q=88&w=2400": "assets/images/food-products-desktop.webp",
        "https://images.unsplash.com/photo-1713900105420-67ae6dbf3595?auto=format&fit=crop&fm=jpg&q=60&w=640": "assets/images/plastic-products-mobile.webp",
        "https://images.unsplash.com/photo-1713900105420-67ae6dbf3595?auto=format&fit=crop&fm=jpg&q=60&w=1280": "assets/images/plastic-products-tablet.webp",
        "https://images.unsplash.com/photo-1713900105420-67ae6dbf3595?auto=format&fit=crop&fm=jpg&q=60&w=2400": "assets/images/plastic-products-desktop.webp",
        "https://images.unsplash.com/photo-1759167632930-298bca6b4268?auto=format&fit=crop&fm=jpg&q=60&w=640": "assets/images/sweets-snacks-mobile.webp",
        "https://images.unsplash.com/photo-1759167632930-298bca6b4268?auto=format&fit=crop&fm=jpg&q=60&w=1280": "assets/images/sweets-snacks-tablet.webp",
        "https://images.unsplash.com/photo-1759167632930-298bca6b4268?auto=format&fit=crop&fm=jpg&q=60&w=2400": "assets/images/sweets-snacks-desktop.webp",
    }
    for remote, local in remote_map.items():
        html = html.replace(remote, local)

    # Replace activity <picture> srcsets with the three generated local variants.
    patterns = {
        "food-products": r'(<article class="business">.*?)(<source type="image/webp" srcset=")[^"]*(" sizes="[^"]*")',
        "plastic-products": r'(<article class="business">.*?)(<source type="image/webp" srcset=")[^"]*(" sizes="[^"]*")',
        "sweets-snacks": r'(<article class="business">.*?)(<source type="image/webp" srcset=")[^"]*(" sizes="[^"]*")',
    }
    # The global URL replacements above already make each srcset local and responsive.
    # This guard verifies the expected local variants are present.
    for name in patterns:
        if f"assets/images/{name}-desktop.webp" not in html:
            raise RuntimeError(f"Responsive desktop asset is not referenced for {name}")
        if f"assets/images/{name}-tablet.webp" not in html:
            raise RuntimeError(f"Responsive tablet asset is not referenced for {name}")
        if f"assets/images/{name}-mobile.webp" not in html:
            raise RuntimeError(f"Responsive mobile asset is not referenced for {name}")

    if "images.unsplash.com" in html:
        raise RuntimeError("Remote Unsplash image references remain in index.html")

    if html != original:
        INDEX.write_text(html, encoding="utf-8")
        print("Updated index.html to use local responsive WebP assets")
    else:
        print("index.html already uses local image assets")


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
