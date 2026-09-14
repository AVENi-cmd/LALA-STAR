from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "assets" / "optimized"
OUTPUT_DIR = ROOT / "assets" / "images"

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
        rendered = ImageOps.fit(
            image,
            size,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
        output.parent.mkdir(parents=True, exist_ok=True)
        rendered.save(output, format="WEBP", quality=QUALITY, method=6)

    data = output.read_bytes()
    if len(data) < 12 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise RuntimeError(f"Invalid RIFF/WEBP output: {output}")

    with Image.open(output) as check:
        if check.format != "WEBP" or check.size != size:
            raise RuntimeError(f"Invalid output metadata: {output}")

    print(f"OK {output} | {size[0]}x{size[1]} | {len(data)} bytes")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, preferred in SOURCES.items():
        source = find_source(name, preferred)
        print(f"Source: {source}")
        for variant, size in VARIANTS.items():
            build_one(source, OUTPUT_DIR / f"{name}-{variant}.webp", size)


if __name__ == "__main__":
    main()
