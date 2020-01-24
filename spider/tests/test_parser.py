import os

import pytest

from app.utils import clear_str
from app.spider.parser import PageParser
from tests.common import read_html, single_tag


html_path = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'arxiv.html')

class TestParser:
    """
    爬虫解析模块的单元测试
    """
    def setup(self):
        try:
            full_html = read_html(html_path)
        except Exception:
            path = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'tests/arxiv.html')
            full_html = read_html(path)
        self.parser = PageParser(full_html, 'forestry')

    def test_parse_authors(self):
        str_author = 'Authors:  Mahdi Teimouri , Jeffrey W. Doser , Andrew O. Finley'
        assert str_author == self.parser.parse_authors(single_tag)

    def test_parse_title(self):
        target_title = 'ForestFit : An R package for modeling tree diameter distributions'
        parsed_title = clear_str(self.parser.parse_title(single_tag))
        assert target_title == parsed_title

    def test_parse_page(self):
        cnt = 0
        for p in self.parser.parser_page():
            cnt += 1
            assert type(p) == dict
        assert cnt == 49

    def test_parse_arxurl(self):
        target_url = 'https://arxiv.org/abs/1911.11002'
        parsed_url = clear_str(self.parser.parse_arxurl(single_tag))
        assert target_url == parsed_url

    def test_parse_pdfurl(self):
        target_url = 'https://arxiv.org/pdf/1911.11002'
        parsed_url = clear_str(self.parser.parse_pdfurl(single_tag))
        assert target_url == parsed_url

    def test_parse_content_and_expr(self):
        content = self.parser.parse_content(single_tag)
        expr = self.parser.parse_expr(0.5, content)

        assert len(expr) / len(content) < 0.5
        assert len(expr) / len(content) > 0.49

        expr = self.parser.parse_expr(0.3, content)

        assert len(expr) / len(content) < 0.3
        assert len(expr) / len(content) > 0.29
