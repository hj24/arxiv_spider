import asyncio
from asyncio import Queue
from random import randint

from app.spider.crawler import SpiderMan
from app.spider.parser import PageParser
from app.spider.saver import Saver
from app.settings import SpiderConfig


class Engine:
    """
    爬虫主调度器, 生产者消费者模型
    """
    def __init__(self):
        self.que = Queue()

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

    async def producer(self):
        print('start producer')
        proxies = SpiderMan.make_porxies()
        _proxy = self._load_random_item(proxies)
        print('proxies loaded: \n',proxies)

        urls = await SpiderMan.generate_url(_proxy)
        print('target urls loaded: \n', urls)
        cfgs = Engine.make_spider_config()
        _cfgs = cfgs if cfgs else None

        for url in urls:
            print('start to fetch the page: ', url)
            if proxies:
                _proxy = self._load_random_item(proxies)
                if not _cfgs:
                    status, item = await SpiderMan(url).download_page(_proxy)
                else:
                    _cfg = self._load_random_item(_cfgs)
                    status, item = await SpiderMan(url).download_page(_proxy, headers=_cfg['headers'],
                                                                timeout=_cfg['timeout'])
                    await asyncio.sleep(_cfg['sleep'])
                await self.que.put(item)
        await self.que.put('end')

    async def consumer(self, loop):
        # 消费者：从队列中取出item，是一个dict
        while True:
            try:
                item = await self.que.get()
                print('consumer get: ', item)
                if isinstance(item, str):
                    if item == 'end':
                        break
                if not item:
                    continue
                p = PageParser(item['content'], item['subject'])
                for res in p.parser_page():
                    print('consumer: ', res)
                    _saver = Saver()
                    await loop.run_in_executor(None, _saver.save_one, res)
                    #Saver().save_one(**res)
            except Exception as e:
                print('consumer', e)
            finally:
                self.que.task_done()

    async def main(self, loop):
        _producer = [self.producer()]
        _consumer = [asyncio.ensure_future(self.consumer(loop))]
        tasks = _producer + _consumer

        await asyncio.gather(*tasks, return_exceptions=True)
        #await self.que.join()

        for c in _consumer:
            c.cancel()

    def loop(self):
        try:
            _loop = asyncio.get_event_loop()
            _loop.run_until_complete(self.main(_loop))
            _loop.close()
        except Exception as e:
            print(e)
            return False
        else:
            return True
