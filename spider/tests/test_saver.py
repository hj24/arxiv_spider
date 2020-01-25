import os

import pytest
from sea import create_app


class TestSaver:

    def setup(self):
        self.root_path = os.path.abspath(os.path.dirname(__file__))
        print(self.root_path)

    def test_save_one(self):
        self.setup()
        create_app(self.root_path)

        from app.spider.saver import Saver

        parsed = {
            'title': 'test title 2',
            'arx_url': 'https://arx.com',
            'pdf_url': 'https://pdf.com',
            'author': 'test authors',
            'expr': 'expr ...',
            'content': 'full content ...',
            'subject': 'forestry'
        }

        ret = Saver().save_one(**parsed)
        ret2 = Saver().save_one(**parsed)

        assert type(ret) == int
        assert ret == ret2

        ret3 = Saver().delete_by_id(ret2)

        assert ret3 == 1
