import asyncio
from asyncio import Queue
from random import randint

from app.spider.crawler import SpiderMan
from app.spider.parser import PageParser
from app.spider.saver import Saver
from app.dao import SpiderConfig, RedisDao


class Engine:
    """
    爬虫主调度器, 生产者消费者模型
    """
    def __init__(self):
        self.que = Queue()

    @staticmethod
    def make_spider_config():
        """
        从数据库加载爬虫配置
        """
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
        """
        根据给定的列表返回其中一个随机元素
        """
        if len(item_list) == 0:
            return None
        idx = randint(0, len(item_list) - 1)
        return item_list[idx]

    async def producer(self, loop, urls, proxy):
        """
        生产者，根据传进来的url列表进程爬取
        爬取结果存入队列
        """
        print('start producer')
        # 加载爬虫所需的代理，配置和初始化url
        # 从数据库去读取，是阻塞操作
        cfgs = await loop.run_in_executor(None, Engine.make_spider_config)
        _cfg = self._load_random_item(cfgs)
        print('congigs loaded: \n', _cfg)
        print('target urls loaded: \n', urls)

        for url in urls:
            print('start to fetch the page: ', url)
            if not _cfg:
                _, item = await SpiderMan(url).download_page(proxy)
            else:
                _, item = await SpiderMan(url).download_page(proxy, headers=_cfg['headers'], 
                                                                timeout=_cfg['timeout'])
                await asyncio.sleep(_cfg['sleep'])
            await self.que.put(item)

        await self.que.put('end')

    async def consumer(self, loop, signal):
        """消费者：从队列中取出item，是一个dict"""
        # 初始化计数器
        cnt = tot = 0
        end_cnt = 1
        articles = []
        _dao = RedisDao()
        while True:
            try:
                item = await self.que.get()
                print('consumer get: ', item)
                if isinstance(item, str):
                    if item == 'end':
                        if end_cnt == signal:
                            break
                        else:
                            end_cnt += 1
                            continue
                if not item:
                    continue
                p = PageParser(item['content'], item['subject'])
                for res in p.parser_page():
                    print('consumer: ', res)
                    tot += 1
                    articles.append(res['title'])
                    _saver = Saver()
                    await loop.run_in_executor(None, _saver.save_one, res)
                    cnt += 1
                    #Saver().save_one(**res)
            except Exception as e:
                print('consumer', e)
            finally:
                self.que.task_done()
        # 更新计数器
        _dao.save_or_update_counter(cnt, tot)
        # 维护一份更新文章的列表到redis
        _dao.update_articles(articles)

    async def main(self, loop):
        # 生产者
        proxies = await loop.run_in_executor(None, SpiderMan.make_porxies)
        _proxy = self._load_random_item(proxies)
        urls = await SpiderMan.generate_url(_proxy)
        producer_list = SpiderMan.dispatch_url(urls)
        _producer = [self.producer(loop, u, _proxy) for u in producer_list]
        # 消费者
        _consumer = [asyncio.ensure_future(self.consumer(loop, len(producer_list)))]

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
