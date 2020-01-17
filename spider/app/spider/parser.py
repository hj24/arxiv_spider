import re

from bs4 import BeautifulSoup

from app.spider.utils import (TITLE, ARXURL, PDFURL)


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
                'title': self._parse_title(str_tag),
                'arxurl': self._parse_arxurl(str_tag),
                'pdfurl': self._parse_pdfurl(str_tag),
                'author': self._parse_authors(str_tag),
                'expr': self._parse_expr(str_tag),
                'content': self._parse_content(str_tag),
                'subject': self._subj
            }
            yield parsed

    def _parse_title(self, content):
        pass

    def _parse_arxurl(self, content):
        pass

    def _parse_pdfurl(self, content):
        pass

    def _parse_authors(self, content):
        pass

    def _parse_expr(self, content):
        pass

    def _parse_content(self, content):
        pass


