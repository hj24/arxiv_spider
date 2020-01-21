from app.model import SpConfiguration as spc
from app.model import ProxyConfiguration as proxyc


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
