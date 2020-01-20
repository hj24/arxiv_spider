import gevent
from gevent import monkey
monkey.patch_all()

from random import randint

from gevent.queue import JoinableQueue

from app.spider.crawler import SpiderMan
from app.spider.parser import PageParser
from app.spider.saver import Saver
from app.settings import SpiderConfig


class Engine:
    """
    爬虫主调度器
    """
    def __init__(self):
        self.spider_que = JoinableQueue()
        self.parser_que = JoinableQueue()

    @staticmethod
    def make_spider_config():
        try:
            cnt = SpiderConfig.count()
            _configs = []

            for i in range(1, cnt + 1):
                spc = SpiderConfig(i)
                cfg = {
                    'sleep': spc.sleep,
                    'interval': spc.interval,
                    'timeout': spc.timeout,
                    'headers': spc.headers
                }
                _configs.append(cfg)
        except Exception:
            return []
        else:
            return _configs

    def _load_random_item(self, item_list):
        idx = randint(0, len(item_list) - 1)
        return item_list[idx]

    def spider_producer(self):
        urls = SpiderMan.generate_url()
        proxies = SpiderMan.make_porxies()
        cfgs = Engine.make_spider_config()

        _cfgs = cfgs if cfgs else None

        for url in urls:
            if proxies:
                _proxy = self._load_random_item(proxies)
                if not _cfgs:
                    status, item = SpiderMan(url).download_page(_proxy)
                else:
                    _cfg = self._load_random_item(_cfgs)
                    status, item = SpiderMan(url).download_page(_proxy, headers=_cfg['headers'],
                                                                timeout=_cfg['timeout'])
                    gevent.sleep(_cfg['sleep'])
                if status:
                    self.spider_que.put(item)

    def spider_consumer(self):
        while True:
            item = self.spider_que.get()
            try:
                p = PageParser(item['content'], item['subject'])
                for res in p.parser_page():
                    self.parser_que.put(res)
            finally:
                self.spider_que.task_done()

    def parser_consumer(self):
        while True:
            item = self.parser_que.get()
            try:
                Saver().save_one(**item)
            finally:
                self.parser_que.task_done()

    def loop(self):
        try:
            sp = gevent.spawn(self.spider_producer)
            sc = gevent.spawn(self.spider_consumer)
            pc = gevent.spawn(self.parser_consumer)
            gevent.joinall([sp, sc, pc])
        except Exception:
            return False
        else:
            return True
