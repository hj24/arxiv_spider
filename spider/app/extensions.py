import redis
from peeweext.sea import Peeweext
from sea.contrib.extensions.celery import AsyncTask


# celery异步任务插件，本项目暂未启用
async_task = AsyncTask()

# peewee插件
pwdb = Peeweext(ns='PW_')

# 定义redis插件
class Redis:

    def __init__(self):
        self._client = None

    def init_app(self, app):
        opts = app.config.get_namespace('REDIS_')
        print(opts)
        self._pool = redis.ConnectionPool(**opts)
        self._client = redis.StrictRedis(connection_pool=self._pool)

    def __getattr__(self, name):
        return getattr(self._client, name)