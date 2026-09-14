from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

OLD_TO_NEW = {
    "photo-1773946836315-bd8269b62b93": "assets/images/food-products-desktop.webp",
    "photo-1713900105420-67ae6dbf3595": "assets/images/plastic-products-desktop.webp",
    "photo-1759167632930-298bca6b4268": "assets/images/sweets-snacks-desktop.webp",
    "photo-1645736315000-6f788915923b": "assets/images/warehouse-desktop.webp",
}


def replace_images(html: str) -> str:
    for old, new in OLD_TO_NEW.items():
        html = re.sub(
            rf"https://images\.unsplash\.com/{re.escape(old)}\?[^\"'\s>)]+",
            new,
            html,
        )
    return html


def main() -> None:
    html = INDEX.read_text(encoding="utf-8")
    html = replace_images(html)
    if "images.unsplash.com" in html:
        raise RuntimeError("Remote image references remain in index.html")
    INDEX.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
