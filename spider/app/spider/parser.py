import re

from bs4 import BeautifulSoup

from app.spider.utils import (TITLE, ARXURL, PDFURL)


class PageParser:
    """
    解析arxiv的每一页
    """
    def __init__(self, html):
        self._soup = BeautifulSoup(html, "html.parser")
        self._tags = None

    def _parse_tag_by_class(self, tag_name, tag_class):
        try:
            self._tags = [tag for tag in self._soup.find_all(tag_name, class_=tag_class)]
        except Exception:
            self._tags = []

    def parser_page(self):
        try:
            self._parse_tag_by_class('li', 'arxiv-result')
        except Exception:
            pass
        else:
            pass


