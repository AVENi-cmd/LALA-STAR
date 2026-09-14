from pathlib import Path
import re
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "assets" / "optimized"
INDEX = ROOT / "index.html"
ASSET_VERSION = "20260915-5"
SOURCES = {"warehouse":"warehouse-hero","food-products":"food-products","plastic-products":"plastic-products","sweets-snacks":"sweets-snacks"}
SIZES = {"mobile":640,"tablet":1280,"desktop":1600}
SEO_MARKER = '<meta name="lalastar-seo-v1" content="managed-by-build-webp">'

def build_approved_webp():
    for name,base in SOURCES.items():
        source = (ROOT / "assets" / "IMG_3042.jpeg") if name == "warehouse" else (SOURCE_DIR / f"{base}-1600.jpg")
        if not source.is_file() or source.stat().st_size < 30000:
            raise RuntimeError(f"Missing or suspiciously small approved image source: {source}")
        with Image.open(source) as im:
            im = im.convert("RGB")
            for size in sorted(set(SIZES.values())):
                target=(size, round(size*9/16))
                out=ImageOps.fit(im, target, method=Image.Resampling.LANCZOS, centering=(0.5,0.5))
                destination=SOURCE_DIR / f"{base}-{size}.webp"
                out.save(destination, "WEBP", quality=88, method=6)
                if destination.stat().st_size < 30000:
                    raise RuntimeError(f"Generated image is suspiciously small: {destination}")
                with Image.open(destination) as check:
                    if check.format != "WEBP" or check.size != target:
                        raise RuntimeError(f"Generated WebP validation failed: {destination} -> {check.format} {check.size}")

def replace_image_refs(html):
    for name,base in SOURCES.items():
        for variant,size in SIZES.items():
            html=re.sub(rf'assets/(?:images|optimized)/{re.escape(name)}-{variant}\.webp(?:\?v=[^\s\"\']+)?',f'assets/optimized/{base}-{size}.webp?v={ASSET_VERSION}',html)
    html=re.sub(r'https://images\.unsplash\.com/photo-[^\"\'\s>)]+','BLOCKED_REMOTE_IMAGE_REFERENCE',html)
    return html

def inject_i18n(html):
    html=re.sub(r'<script[^>]*src=["\']assets/i18n\.js[^>]*></script>','',html)
    html=re.sub(r'<script>const btn=document\.getElementById\(["\']langBtn["\']\).*?</script>','',html,flags=re.DOTALL)
    return html.replace('</body>','<script src="assets/i18n.js" defer></script></body>',1)

def clean_preloads(html):
    html=re.sub(r'<link rel="preload" as="image" href="assets/(?:images|optimized)/warehouse[^>]*>','',html)
    pre=f'<link rel="preload" as="image" href="assets/optimized/warehouse-hero-1600.webp?v={ASSET_VERSION}" fetchpriority="high" media="(min-width:851px)"><link rel="preload" as="image" href="assets/optimized/warehouse-hero-640.webp?v={ASSET_VERSION}" fetchpriority="high" media="(max-width:850px)">'
    return html.replace('<meta name="viewport"',pre+'<meta name="viewport"',1)

def main():
    build_approved_webp()
    html=INDEX.read_text(encoding="utf-8")
    html=replace_image_refs(html)
    if 'images.unsplash.com' in html or 'BLOCKED_REMOTE_IMAGE_REFERENCE' in html: raise RuntimeError('Remote image references remain in index.html')
    html=clean_preloads(html)
    html=inject_i18n(html)
    if 'assets/i18n.js' not in html: raise RuntimeError('i18n script was not wired into index.html')
    if 'const btn=document.getElementById("langBtn")' in html or "const btn=document.getElementById('langBtn')" in html: raise RuntimeError('Legacy language handler remains in index.html')
    if SEO_MARKER not in html: raise RuntimeError('SEO marker missing')
    INDEX.write_text(html,encoding='utf-8')

if __name__=='__main__': main()
