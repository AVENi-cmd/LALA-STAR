from pathlib import Path
import re

html = Path(__file__).resolve().parents[1] / "index.html"
s = html.read_text(encoding="utf-8")
checks = {
    "skip-link": 'class="skip-link"' in s,
    "main-target": 'id="main-content"' in s,
    "menu-button": 'aria-label="فتح القائمة"' in s and 'aria-expanded="false"' in s,
    "menu-controls": 'aria-controls="site-nav"' in s,
    "nav-label": 'aria-label="التنقل الرئيسي"' in s,
    "focus-visible": ":focus-visible" in s,
    "reduced-motion": "prefers-reduced-motion" in s,
    "lang-button-label": 'aria-label="تغيير اللغة"' in s,
}
failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise SystemExit("Missing accessibility requirements: " + ", ".join(failed))
print("Accessibility checks passed")
