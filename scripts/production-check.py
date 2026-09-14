from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.hrefs = []
        self.srcs = []
        self.tags = []
        self.meta = []
        self.title = False
        self.html_attrs = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if tag == "html":
            self.html_attrs = attrs
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if "href" in attrs:
            self.hrefs.append(attrs["href"])
        if "src" in attrs:
            self.srcs.append(attrs["src"])
        if tag == "meta":
            self.meta.append(attrs)
        if tag == "title":
            self.title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.title = False


def fail(errors):
    if errors:
        print("Production checks failed:")
        print("\n".join(f"- {e}" for e in errors))
        raise SystemExit(1)

html = INDEX.read_text(encoding="utf-8")
parser = AuditParser()
parser.feed(html)
errors = []

# Basic document contract.
if parser.html_attrs.get("lang") != "ar":
    errors.append("HTML lang must be ar")
if parser.html_attrs.get("dir") != "rtl":
    errors.append("HTML dir must be rtl")
if "<title>" not in html or "</title>" not in html:
    errors.append("Missing title element")
if 'name="description"' not in html:
    errors.append("Missing meta description")
if 'rel="canonical"' not in html:
    errors.append("Missing canonical link")
if 'name="viewport"' not in html:
    errors.append("Missing viewport meta")

# Duplicate IDs are a real navigation/accessibility defect.
duplicates = sorted({x for x in parser.ids if parser.ids.count(x) > 1})
if duplicates:
    errors.append("Duplicate IDs: " + ", ".join(duplicates))

# Every same-page anchor must have a target.
ids = set(parser.ids)
for href in parser.hrefs:
    if href.startswith("#") and len(href) > 1 and href[1:] not in ids:
        errors.append(f"Broken same-page anchor: {href}")

# Local asset references must exist; remote image hosting is forbidden.
refs = sorted(set(re.findall(r"assets/[A-Za-z0-9_./-]+\\.(?:webp|jpg|jpeg|png)", html)))
for ref in refs:
    if not (ROOT / ref).is_file():
        errors.append(f"Missing local asset: {ref}")
if "images.unsplash.com" in html:
    errors.append("Remote Unsplash image reference remains")

# External resource URLs must use HTTPS.
for url in re.findall(r"(?:href|src)=[\"'](https?://[^\"']+)", html, flags=re.I):
    if not url.lower().startswith("https://"):
        errors.append(f"Insecure external resource: {url}")

# Lightweight secret scan for accidental credentials in tracked text.
secret_patterns = [
    r"(?i)(api[_-]?key|secret[_-]?key|access[_-]?token)\\s*[:=]\\s*[A-Za-z0-9_\\-]{16,}",
    r"(?i)-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
]
for pattern in secret_patterns:
    if re.search(pattern, html):
        errors.append("Possible credential/private key detected in index.html")

fail(errors)
print(f"Production checks passed: {len(refs)} local image references, {len(parser.ids)} IDs, and all same-page anchors verified.")
