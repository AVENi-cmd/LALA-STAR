from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "images"

SOURCES = {
    "warehouse": ROOT / "assets" / "warehouse-hero.jpg",
    "food-products": ROOT / "assets" / "food-products.jpg",
    "plastic-products": ROOT / "assets" / "plastic-products.jpg",
    "sweets-snacks": ROOT / "assets" / "sweets-snacks.jpg",
}

VARIANTS = {
    "desktop": (1920, 1080),
    "tablet": (1024, 1024),
    "mobile": (750, 1000),
}

QUALITY = 88


def build_one(source: Path, output: Path, size: tuple[int, int]) -> None:
    if not source.exists():
        raise FileNotFoundError(f"Missing source image: {source}")

    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        rendered = ImageOps.fit(
            image,
            size,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
        output.parent.mkdir(parents=True, exist_ok=True)
        rendered.save(
            output,
            format="WEBP",
            quality=QUALITY,
            method=6,
        )

        with Image.open(output) as check:
            if check.format != "WEBP":
                raise RuntimeError(f"Output is not WebP: {output}")
            if check.size != size:
                raise RuntimeError(
                    f"Unexpected dimensions for {output}: {check.size}; expected {size}"
                )

    data = output.read_bytes()
    if len(data) < 12 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise RuntimeError(f"Invalid RIFF/WEBP header: {output}")
    if len(data) == 0:
        raise RuntimeError(f"Empty output: {output}")

    print(f"OK {output} | {size[0]}x{size[1]} | {len(data)} bytes")


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)

    for name, source in SOURCES.items():
        for variant, size in VARIANTS.items():
            output = OUTPUT / f"{name}-{variant}.webp"
            build_one(source, output, size)


if __name__ == "__main__":
    main()
