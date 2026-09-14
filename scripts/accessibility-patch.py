from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


def patch(html: str) -> str:
    # Keyboard-accessible skip link and a stable main landmark.
    if 'class="skip-link"' not in html:
        html = html.replace('<body>', '<body><a class="skip-link" href="#main-content">تخطي إلى المحتوى الرئيسي</a>', 1)
    html = html.replace('<main>', '<main id="main-content">', 1)

    # Give the primary navigation an explicit accessible name.
    html = html.replace('<nav class="links">', '<nav class="links" id="site-nav" aria-label="التنقل الرئيسي">', 1)

    # Make the mobile menu button stateful and programmatically associated with the nav.
    html = html.replace('<button class="menu" aria-label="القائمة">', '<button class="menu" type="button" aria-label="فتح القائمة" aria-controls="site-nav" aria-expanded="false">', 1)
    html = html.replace('<button class="lang" id="langBtn">EN</button>', '<button class="lang" id="langBtn" type="button" aria-label="تغيير اللغة">EN</button>', 1)

    # Visible keyboard focus without changing the normal visual design.
    focus_css = '.skip-link{position:fixed;top:-100px;right:16px;z-index:1000;background:var(--navy);color:#fff;padding:10px 16px;border-radius:7px;font-weight:700}.skip-link:focus{top:16px}.links a:focus-visible,.lang:focus-visible,.menu:focus-visible,.btn:focus-visible,.map:focus-visible,.brand:focus-visible{outline:3px solid var(--red);outline-offset:3px;border-radius:5px}'
    if '.skip-link{' not in html:
        html = html.replace('</style>', focus_css + '</style>', 1)

    # Respect users who request reduced motion.
    motion_css = '@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*:before,*:after{scroll-behavior:auto!important;transition-duration:.01ms!important;animation-duration:.01ms!important;animation-iteration-count:1!important}}'
    if 'prefers-reduced-motion:reduce' not in html:
        html = html.replace('</style>', motion_css + '</style>', 1)

    return html


def validate(html: str) -> None:
    required = (
        'class="skip-link"',
        'id="main-content"',
        'id="site-nav"',
        'aria-label="التنقل الرئيسي"',
        'aria-label="فتح القائمة"',
        'aria-controls="site-nav"',
        'aria-expanded="false"',
        'aria-label="تغيير اللغة"',
        '.skip-link:focus',
        ':focus-visible',
        'prefers-reduced-motion:reduce',
    )
    missing = [x for x in required if x not in html]
    if missing:
        raise RuntimeError("Accessibility requirements missing: " + ", ".join(missing))


html = patch(INDEX.read_text(encoding="utf-8"))
validate(html)
INDEX.write_text(html, encoding="utf-8")
print("Accessibility patch applied and validated")
