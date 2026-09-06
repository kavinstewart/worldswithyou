"""Catch broken local routes, assets, anchors and missing metadata before publishing."""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.links, self.h1 = path, set(), [], 0
        self.description = self.viewport = self.lang = self.title = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'{self.path}: duplicate ID'
            self.ids.add(attrs['id'])
        self.h1 += tag == 'h1'
        self.title |= tag == 'title'
        self.lang |= tag == 'html' and attrs.get('lang') == 'en'
        self.description |= tag == 'meta' and attrs.get('name') == 'description'
        self.viewport |= tag == 'meta' and attrs.get('name') == 'viewport'
        for attr in ('src', 'href'):
            if attrs.get(attr): self.links.append(attrs[attr])
        if tag == 'img':
            assert 'alt' in attrs and 'width' in attrs and 'height' in attrs, f'{self.path}: image metadata'

root = Path(sys.argv[1]).resolve()
pages = {p.resolve(): Page(p) for p in root.rglob('*.html')}
for path, page in pages.items():
    assert page.h1 == 1 and page.title and page.lang and page.description and page.viewport, f'{path}: metadata'
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc: continue
        target = (root / unquote(url.path).lstrip('/') if url.path.startswith('/') else path.parent / unquote(url.path)).resolve() if url.path else path
        if target.is_dir(): target /= 'index.html'
        assert target.is_relative_to(root) and target.is_file(), f'{path}: broken link {link}'
        if url.fragment and target in pages:
            assert unquote(url.fragment) in pages[target].ids, f'{path}: broken anchor {link}'
assert (root / 'CNAME').read_text().strip() == 'worldswithyou.com'
assert (root / 'assets/threshold.webp').stat().st_size < 1_500_000, 'Optimize hero artwork'
assert len(pages) >= 4
print(f'Passed: {len(pages)} pages, metadata, local links, anchors, image dimensions, domain and image budget.')
