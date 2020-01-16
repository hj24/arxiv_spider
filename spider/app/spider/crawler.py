from gevent import monkey
monkey.patch_all()

import requests
from app.model import Api

from app.spider.utils import PAGNUMPAT


class SpiderMan:

    def __init__(self):
        pass


    @staticmethod
    def _try_get_page_nums(url, headers=None):
        """
        根据数据库中母url获取页面的总数
        总数一半在页面的最前面，所以截取获取的前10000个字符，提高正则匹配效率
        """
        try:
            resp = requests.get(url, headers=headers)
            result = PAGNUMPAT.search(resp.text[:10000])
            per, tot = result.groups()
        except Exception:
            return 1, 1
        else:
            return per, tot

    @staticmethod
    def _gen_api(url, subj, per, tot):
        tot_sub = tot // per if tot % per == 0 else tot // per + 1
        urls = []
        for subfix in range(tot_sub):
            urls.append({'subject': subj,
                         'url': url + '&start=' + str(subfix * per)})
        return urls

    @staticmethod
    def generate_url():
        try:
            generated = []
            for api in Api.select().where(Api.deleted == False):
                per, tot = SpiderMan._try_get_page_nums(api.url, api.headers)
                generated.extend(SpiderMan._gen_api(api.url, api.subject,
                                                    int(per), int(tot)))
        except Exception:
            return []
        else:
            return generated


if __name__ == '__main__':
    pass