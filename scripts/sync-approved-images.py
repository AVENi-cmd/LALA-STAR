from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "images"
PAIRS = {
    "warehouse": "warehouse-desktop.webp",
    "food-products": "food-products-desktop.webp",
    "plastic-products": "plastic-products-desktop.webp",
    "sweets-snacks": "sweets-snacks-desktop.webp",
}

for stem, desktop in PAIRS.items():
    source = IMG / desktop
    if not source.exists():
        raise SystemExit(f"Missing approved desktop image: {source}")
    for variant in ("mobile", "tablet"):
        target = IMG / f"{stem}-{variant}.webp"
        shutil.copyfile(source, target)
        print(f"Synced {target.name} from {source.name}")
