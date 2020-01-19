from bs4 import BeautifulSoup

from app.spider.utils import (TITLE, ARXURL, PDFURL)
from app.utils import clear_str


class PageParser:
    """
    解析arxiv的每一页
    """
    def __init__(self, html, subject):
        self._soup = BeautifulSoup(html, "html.parser")
        self._tags = None
        self._content = html
        self._subj = subject

    def _parse_tag_by_class(self, tag_name, tag_class):
        try:
            self._tags = [tag for tag in self._soup.find_all(tag_name, class_=tag_class)]
        except Exception:
            self._tags = []

    def parser_page(self):
        self._parse_tag_by_class('li', 'arxiv-result')
        for tag in self._tags:
            str_tag = str(tag)
            parsed = {
                'title': self.parse_title(str_tag),
                'arxurl': self.parse_arxurl(str_tag),
                'pdfurl': self.parse_pdfurl(str_tag),
                'author': self.parse_authors(),
                'expr': self.parse_expr(0.5),
                'content': self.parse_content(),
                'subject': self._subj
            }
            yield parsed

    def _parse_by_re(self, content, _pattern):
        try:
            res = _pattern.search(content)
            res_tuple = res.groups()
        except Exception:
            return None
        else:
            return res_tuple[0]

    def parse_title(self, content):
        return self._parse_by_re(content, TITLE)

    def parse_arxurl(self, content):
        return self._parse_by_re(content, ARXURL)

    def parse_pdfurl(self, content):
        return self._parse_by_re(content, PDFURL)

    def parse_authors(self):
        try:
            authors = self._soup.find('p', class_='authors')
            author_list = []
            for ch in authors.children:
                author_list.append(clear_str(ch.string))
            str_author = clear_str(' '.join(author_list))
        except Exception:
            return None
        else:
            return str_author

    def parse_expr(self, percent):
        _full = self.parse_content()
        nums = len(_full) * int(percent)
        if not _full:
            return None
        else:
            return self.parse_content()[:nums]

    def parse_content(self):
        try:
            contents = self._soup.find('p', class_='abstract mathjax')
            content_list = []
            for c in contents:
                if not str(c).strip().startswith('<a'):
                    if hasattr(c, 'text'):
                        content_list.append(c.text)
                    else:
                        content_list.append(str(c))
            parsed = ''.join(content_list).strip()
        except Exception:
            return None
        else:
            return parsed


if __name__ == '__main__':
    from tests.test_parser import single_tag
    print(PageParser(single_tag, '').parse_authors())