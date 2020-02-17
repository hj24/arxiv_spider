import pickle

from app.model import SpConfiguration as spc
from app.model import ProxyConfiguration as proxyc
from app.extensions import spredis


# 爬虫相关的配置，从数据库读取
class SpiderProxy:

    def __init__(self, idx):
        """
        从数据库根据 id 动态读取proxy
        """
        self.proxy_item = proxyc.select().where(proxyc.id == idx,
                                                proxyc.deleted == False).get()

    @property
    def proxy_host(self):
        return self.proxy_item.host

    @property
    def proxy_port(self):
        return self.proxy_item.port

    @property
    def proxy_user(self):
        return self.proxy_item.puser

    @property
    def proxy_pwd(self):
        return self.proxy_item.pwd

    @classmethod
    def count(cls):
        return proxyc.select().count()

class SpiderConfig:

    def __init__(self, idx):
        self.sp_item = spc.select().where(spc.id == idx,
                                          spc.deleted == False).get()

    @property
    def headers(self):
        return self.sp_item.headers

    @property
    def sleep(self):
        return self.sp_item.sleep

    @property
    def timeout(self):
        return self.sp_item.timeout

    @classmethod
    def count(cls):
        return spc.select().count()

class RedisDao:
    
    def save_or_update_counter(self, cnt, tot):
        """
        更新计数器
        """
        hash_counter = {"tot": tot, "success": cnt}
        return spredis.hmset("counter", hash_counter)

    def get_counter(self):
        """
        将byte类型的计数器转为python的字典
        """
        byte_val = spredis.hgetall("counter")
        res = {}
        for k, v in byte_val.items():
            res[k.decode("utf-8")] = int(v.decode("utf-8"))
        return res

    def update_articles(self, articles):
        """
        取出序列化的列表 -> [{"name": ..., "tag": ...}, {...}]
        反序列化后去重，重新序列化之后存储
        """
        # 如果redis里不存在这个键，则创建
        if not spredis.exists("articles"):
            ans = []
            for i in articles:
                ans.append({"name": i, "tag": True})
            spredis.setnx("articles", pickle.dumps(ans))
        else:
            # 取出的列表里存dict
            saved = spredis.get("articles")
            decoded_saved = pickle.loads(saved)
            # 旧的文章tag打成False
            saved_names = []
            for old in decoded_saved:
                saved_names.append(old["name"])
                old["tag"] = False 
            # 求出更新的文章
            to_update = set(articles) - set(saved_names)
            new = []
            for i in to_update:
                new.append({"name": i, "tag": True})
            decoded_saved.extend(new)
            # 旧的键删除，重新存
            spredis.delete("articles")
            spredis.setnx("articles", pickle.dumps(decoded_saved))   

    def get_newest_articles(self):
        saved = spredis.get("articles")
        decoded = pickle.loads(saved)
        newest = [a["name"] for a in decoded if a["tag"]]
        return newest
