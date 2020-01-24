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

    def _single_soup(self, content):
        """
        把全文分成一块一块的标签，针对单个标签生成的soup对象
        """
        return BeautifulSoup(content, "html.parser")

    def _parse_tag_by_class(self, tag_name, tag_class):
        try:
            self._tags = [tag for tag in self._soup.find_all(tag_name, class_=tag_class)]
        except Exception:
            self._tags = []

    def parser_page(self):
        self._parse_tag_by_class('li', 'arxiv-result')
        for tag in self._tags:
            str_tag = str(tag)
            _full_content = self.parse_content(str_tag)
            parsed = {
                'title': self.parse_title(str_tag),
                'arx_url': self.parse_arxurl(str_tag),
                'pdf_url': self.parse_pdfurl(str_tag),
                'author': self.parse_authors(str_tag),
                'expr': self.parse_expr(0.5, _full_content),
                'content': _full_content,
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

    def parse_authors(self, tag):
        try:
            author_soup = self._single_soup(tag)
            authors = author_soup.find('p', class_='authors')
            author_list = []
            for ch in authors.children:
                author_list.append(clear_str(ch.string))
            str_author = clear_str(' '.join(author_list))
        except Exception:
            return None
        else:
            return str_author

    def parse_expr(self, percent, full):
        nums = int(len(full) * percent)
        if not full:
            return None
        else:
            return full[:nums]

    def parse_content(self, tag):
        try:
            cont_soup = self._single_soup(tag)
            contents = cont_soup.find('p', class_='abstract mathjax')
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
    """
    simple test
    """
    from tests.common import read_html
    html_path = '/Users/macbook/PycharmProjects/arxiv_spider/spider/tests/arxiv.html'
    html = read_html(html_path)
    parser = PageParser(html, 'forestry')

    for tag in parser.parser_page():
        print(tag)