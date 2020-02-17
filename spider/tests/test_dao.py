import pickle

import pytest

from sea import create_app


def count_update_nums(articles):
    false_cnt = true_cnt = 0
    for a in articles:
        if not a["tag"]:
            false_cnt += 1
        else:
            true_cnt += 1
    return false_cnt, true_cnt

def test_redis_articles():
    import os
    root_path = os.path.abspath(os.path.dirname(__file__))
    create_app(root_path)
    from app.extensions import spredis
    from app.dao import RedisDao

    _dao = RedisDao()
    new_articles = ["1ad", "2bc", "3er"]
    _dao.update_articles(new_articles)
    first = _dao.get_newest_articles()
    assert len(first) == 3

    new_articles_2 = ["1ad", "2bc", "3er", "4th"]
    _dao.update_articles(new_articles_2)
    second = _dao.get_newest_articles()
    assert len(second) == 1

    no_articles = []
    _dao.update_articles(no_articles)
    third = _dao.get_newest_articles()
    assert len(third) == 0

    if spredis.exists("articles") != 0:
        spredis.delete("articles")
    
    assert spredis.exists("articles") == 0

def test_spider_proxy():
    import os

    root_path = os.path.abspath(os.path.dirname(__file__))
    create_app(root_path)

    from app.dao import SpiderProxy

    proxies = []
    cnt = SpiderProxy.count()

    assert type(cnt) == int

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

        assert len(proxies) == 1
