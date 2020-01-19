import pytest

from app.utils import clear_str
from app.spider.parser import PageParser
from tests.common import full_html, parsed_content


class TestParser:
    """
    爬虫解析模块的单元测试
    """
    def setup(self):
        self.parser = PageParser(full_html, 'forestry')

    def test_parse_authors(self):
        str_author = 'Authors:  Mahdi Teimouri , Jeffrey W. Doser , Andrew O. Finley'
        assert str_author == self.parser.parse_authors()

    def test_parse_content(self):
        format_ans = clear_str(parsed_content)
        format_parsed = clear_str(self.parser.parse_content())
        assert format_ans == format_parsed

    def test_parse_expr(self):
        _percent = 0.5
        _full = self.parser.parse_content()
        _expr = self.parser.parse_expr(_percent)
        p2n = len(_full) * int(_percent)
        assert _expr == _full[:p2n]
