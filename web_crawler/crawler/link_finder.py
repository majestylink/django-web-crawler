from html.parser import HTMLParser
from urllib.parse import urljoin


class LinkFinder(HTMLParser):

    def __init__(self, base_url):
        super().__init__()
        self.base = base_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = urljoin(self.base, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
