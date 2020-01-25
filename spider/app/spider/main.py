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
    爬虫主调度器, 生产者消费者模型
    """
    def __init__(self):
        self.que = JoinableQueue()

    @staticmethod
    def make_spider_config():
        try:
            cnt = SpiderConfig.count()
            _configs = []

            for i in range(1, cnt + 1):
                spc = SpiderConfig(i)
                cfg = {
                    'sleep': spc.sleep,
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

    def producer(self):
        proxies = SpiderMan.make_porxies()
        _proxy = self._load_random_item(proxies)

        urls = SpiderMan.generate_url(_proxy)

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

                self.que.put(item)

    def consumer(self):
        # 消费者：从队列中取出item，是一个dict
        while True:
            item = self.que.get()
            try:
                p = PageParser(item['content'], item['subject'])
                for res in p.parser_page():
                    print('consumer: ', res)
                    Saver().save_one(**res)
            except Exception as e:
                print('consumer', e)
            finally:
                self.que.task_done()

    def loop(self):
        try:
            self.producer()
            pc = gevent.spawn(self.consumer)
            self.que.join()
        except Exception as e:
            print('******', e)
            return False
        else:
            return True
