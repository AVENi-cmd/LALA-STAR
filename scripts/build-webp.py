from pathlib import Path
from PIL import Image, ImageOps
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "assets" / "optimized"
OUTPUT_DIR = ROOT / "assets" / "images"
INDEX = ROOT / "index.html"
SOURCES = {n: SOURCE_DIR / f"{n if n != 'warehouse' else 'warehouse-hero'}-1600.webp" for n in ("warehouse", "food-products", "plastic-products", "sweets-snacks")}
VARIANTS = {"desktop": (1920, 1080), "tablet": (1024, 1024), "mobile": (750, 1000)}
QUALITY = 88
SEO_MARKER = '<meta name="lalastar-seo-v1" content="managed-by-build-webp">'
SEO_BLOCK = '''<meta name="lalastar-seo-v1" content="managed-by-build-webp"><meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="https://aveni-cmd.github.io/LALA-STAR/"><meta property="og:type" content="website"><meta property="og:locale" content="ar_SA"><meta property="og:site_name" content="شركة لألأة النجوم التجارية | LALA STAR TRADING CO."><meta property="og:title" content="شركة لألأة النجوم التجارية | LALA STAR TRADING CO."><meta property="og:description" content="شركة لألأة النجوم التجارية — بيع المواد الغذائية بالجملة منذ 1993، مع أنشطة البلاستيك والحلويات والوجبات الخفيفة في الدمام والأحساء."><meta property="og:url" content="https://aveni-cmd.github.io/LALA-STAR/"><meta property="og:image" content="https://aveni-cmd.github.io/LALA-STAR/assets/images/warehouse-desktop.webp"><meta property="og:image:type" content="image/webp"><meta property="og:image:width" content="1920"><meta property="og:image:height" content="1080"><meta property="og:image:alt" content="مستودع تجاري للمواد والسلع بالجملة"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="شركة لألأة النجوم التجارية | LALA STAR TRADING CO."><meta name="twitter:description" content="بيع المواد الغذائية بالجملة منذ 1993، مع أنشطة البلاستيك والحلويات والوجبات الخفيفة."><meta name="twitter:image" content="https://aveni-cmd.github.io/LALA-STAR/assets/images/warehouse-desktop.webp"><script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"شركة لألأة النجوم التجارية","alternateName":"LALA STAR TRADING CO.","description":"شركة لبيع المواد الغذائية بالجملة، مع أنشطة مستقلة في المنتجات البلاستيكية والحلويات والوجبات الخفيفة.","foundingDate":"1993","telephone":"0138562508","email":"starcoldstore@yahoo.com","url":"https://aveni-cmd.github.io/LALA-STAR/","logo":"https://aveni-cmd.github.io/LALA-STAR/assets/lala-star-logo.png","address":{"@type":"PostalAddress","addressLocality":"Dammam","addressCountry":"SA"},"areaServed":"SA"}</script>'''
MENU_SCRIPT = '''<script>(()=>{const menu=document.querySelector('.menu'),nav=document.querySelector('.links');if(!menu||!nav)return;const close=()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','فتح القائمة')};menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';nav.classList.toggle('open',open);menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'إغلاق القائمة':'فتح القائمة')});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){close();menu.focus()}});window.addEventListener('resize',()=>{if(window.innerWidth>850)close()})})();</script>'''

def source_for(name, preferred):
    if preferred.exists(): return preferred
    matches = sorted(SOURCE_DIR.glob(f"{name}*.webp"))
    if not matches: raise FileNotFoundError(f"No WebP source for {name}")
    return matches[-1]

def build(source, output, size):
    with Image.open(source) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        ImageOps.fit(im, size, method=Image.Resampling.LANCZOS).save(output, "WEBP", quality=QUALITY, method=6)
    data = output.read_bytes()
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP": raise RuntimeError(f"Invalid WebP: {output}")
    with Image.open(output) as check:
        if check.size != size or check.format != "WEBP": raise RuntimeError(f"Invalid metadata: {output}")

def replace_remote(html):
    ids = {"1645736315000-6f788915923b":"warehouse","1773946836315-bd8269b62b93":"food-products","1713900105420-67ae6dbf3595":"plastic-products","1759167632930-298bca6b4268":"sweets-snacks"}
    pattern = re.compile(r"https://images\.unsplash\.com/photo-([0-9]+-[a-z0-9]+)\?[^\"'\s>)]+")
    def repl(m):
        name = ids.get(m.group(1))
        if not name: return m.group(0)
        if name == "warehouse": return "assets/images/warehouse-desktop.webp"
        width = int(re.search(r"[?&]w=(\d+)", m.group(0)).group(1)) if re.search(r"[?&]w=(\d+)", m.group(0)) else 2400
        variant = "mobile" if width <= 640 else "tablet" if width <= 1280 else "desktop"
        return f"assets/images/{name}-{variant}.webp"
    return pattern.sub(repl, html)

def optimize(html):
    for variant, width in (("mobile", 750), ("tablet", 1024), ("desktop", 1920)):
        html = re.sub(rf'(assets/images/(?:food-products|plastic-products|sweets-snacks)-{variant}\.webp)\s+\d+w', rf'\1 {width}w', html)
    html = re.sub(r"\s+onerror=\"this\.onerror=null;this\.src='assets/images/(?:food-products|plastic-products|sweets-snacks)-desktop\.webp'\"", "", html)
    html = re.sub(r'(assets/images/(?:food-products|plastic-products|sweets-snacks)-desktop\.webp"[^>]*?)width="1280" height="720"', r'\1width="1920" height="1080"', html)
    preload = '<link rel="preload" as="image" href="assets/images/warehouse-desktop.webp" fetchpriority="high" media="(min-width:851px)"><link rel="preload" as="image" href="assets/images/warehouse-mobile.webp" fetchpriority="high" media="(max-width:850px)">'
    if 'warehouse-desktop.webp" fetchpriority="high"' not in html: html = html.replace('<meta name="viewport"', preload + '<meta name="viewport"', 1)
    mobile = "@media(max-width:850px){.hero{background-image:linear-gradient(90deg,rgba(4,20,42,.88),rgba(7,26,54,.6) 48%,rgba(7,26,54,.18)),url('assets/images/warehouse-mobile.webp')}}"
    if mobile not in html: html = html.replace('</style>', mobile + '</style>', 1)
    return html

def seo(html):
    html = re.sub(r'<meta name="lalastar-seo-v1"[^>]*>.*?</script>', '', html, count=1, flags=re.DOTALL)
    return html.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + SEO_BLOCK, 1)

def inject_menu_script(html):
    html = re.sub(r'<script>\(\(\)=>\{const menu=document\.querySelector\(\'\.menu\'\).*?</script>', '', html, count=1, flags=re.DOTALL)
    return html.replace('</body>', MENU_SCRIPT + '</body>', 1) if '</body>' in html else html + MENU_SCRIPT

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, preferred in SOURCES.items():
        src = source_for(name, preferred)
        for variant, size in VARIANTS.items(): build(src, OUTPUT_DIR / f"{name}-{variant}.webp", size)
    html = inject_menu_script(seo(optimize(replace_remote(INDEX.read_text(encoding="utf-8")))))
    if "images.unsplash.com" in html: raise RuntimeError("Remote Unsplash references remain")
    for name in ("food-products", "plastic-products", "sweets-snacks"):
        for variant in VARIANTS:
            if f"assets/images/{name}-{variant}.webp" not in html: raise RuntimeError(f"Missing {name}-{variant}")
    if "warehouse-desktop.webp" not in html or "warehouse-mobile.webp" not in html: raise RuntimeError("Missing warehouse responsive references")
    if "querySelector('.menu')" not in html or "aria-expanded" not in html: raise RuntimeError("Missing mobile menu behavior")
    for required in (SEO_MARKER, 'rel="canonical"', 'property="og:title"', 'name="twitter:card"', 'application/ld+json', 'food-products-mobile.webp 750w', 'food-products-tablet.webp 1024w', 'food-products-desktop.webp 1920w'):
        if required not in html: raise RuntimeError(f"Missing required markup: {required}")
    INDEX.write_text(html, encoding="utf-8")

if __name__ == "__main__": main()
