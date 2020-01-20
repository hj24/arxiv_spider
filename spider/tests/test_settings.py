import pytest

from sea import create_app


def test_spider_proxy():
    import os

    root_path = os.path.abspath(os.path.dirname(__file__))
    create_app(root_path)

    from app.settings import SpiderProxy

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