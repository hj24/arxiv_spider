import requests_async as requests
from requests.exceptions import ProxyError

from app.model import Api

from app.spider.utils import PAGNUMPAT
from app.settings import SpiderProxy


class SpiderMan:

    def __init__(self, url_item):
        self._sess = requests.Session()
        self._url = url_item['url']
        self._subject = url_item['subject']
        self._headers = url_item['headers']

    async def download_page(self, prxoy, headers=None, timeout=60):
        """
        有代理用代理，没代理用本地ip爬取,有请求头就用，没有就用url_item里的

        :param prxoy: 从make_proxies的结果中随机抽取一个传入
        :return: 状态, 爬取结果
        """
        h = self._headers if not headers else headers
        try:
            async with self._sess as session:
                response = await session.get(self._url, headers=h,
                                             proxies=prxoy, timeout=timeout)
                response.encoding = 'utf-8'
        except Exception as e:
            try:
                print(e)
                async with self._sess as session:
                    response = await session.get(self._url, headers=h,
                                                 timeout=timeout)
                    response.encoding = 'utf-8'
            except Exception as e:
                print(e)
                return False, None
            else:
                if response.status_code == 200:
                    res_dict = {'subject': self._subject, 'content': response.text}
                    return True, res_dict
                else:
                    return False, None
        else:
            if response.status_code == 200:
                res_dict = {'subject': self._subject, 'content': response.text}
                return True, res_dict
            else:
                return False, None

    @staticmethod
    async def _try_get_page_nums(url, headers=None, proxy=None):
        """
        根据数据库中母url获取页面的总数
        总数一半在页面的最前面，所以截取获取的前10000个字符，提高正则匹配效率
        """
        try:
            if not proxy:
                raise Exception('no proxy found')
            resp = await requests.get(url, headers=headers, timeout=180, proxies=proxy)
            result = PAGNUMPAT.search(resp.text[:10000])
            per, tot = result.groups()
        except ProxyError as pe:
            try:
                print('proxy not found or porxy failed: ', pe)
                resp = await requests.get(url, headers=headers, timeout=180)
                result = PAGNUMPAT.search(resp.text[:10000])
                per, tot = result.groups()
            except Exception as e:
                print('try to get page nums failed, return default nums: ', e)
                return 1, 1
            else:
                return per, tot
        except Exception as e:
            print(e)
            return 1, 1
        else:
            return per, tot

    @staticmethod
    def _gen_api(url, subj, per, tot, headers=None):
        tot_sub = tot // per if tot % per == 0 else tot // per + 1
        urls = []
        for subfix in range(tot_sub):
            urls.append({'subject': subj, 'headers': headers,
                         'url': url + '&start=' + str(subfix * per)})
        return urls

    @staticmethod
    async def generate_url(proxy):
        try:
            generated = []
            for api in Api.select().where(Api.deleted == False):
                print('api loaded: \n', api.url)
                per, tot = await SpiderMan._try_get_page_nums(api.url, api.headers, proxy)
                generated.extend(SpiderMan._gen_api(api.url, api.subject, int(per),
                                                    int(tot), headers=api.headers))
        except Exception as e:
            print('generate-url: ', e)
            return []
        else:
            return generated

    @staticmethod
    def make_porxies():
        try:
            proxies = []
            cnt = SpiderProxy.count()
            for i in range(1, cnt + 1):
                proxy = SpiderProxy(i)
                host = proxy.proxy_host
                port = proxy.proxy_port
                user = proxy.proxy_user
                pwd = proxy.proxy_pwd
                proxy_meta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
                    "host": host,
                    "port": port,
                    "user": user,
                    "pass": pwd,
                }
                proxies.append({"http": proxy_meta, "https": proxy_meta})
        except Exception:
            return []
        else:
            return proxies


if __name__ == '__main__':
    pass