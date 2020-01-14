from gevent import monkey
monkey.patch_all()
import redis
from apscheduler.schedulers.gevent import GeventScheduler

from peeweext.sea import Peeweext
# from sea.contrib.extensions.celery import AsyncTask


# 编写扩展
## 定义redis插件
class Redis:

    def __init__(self):
        self._client = None

    def init_app(self, app):
        opts = app.config.get_namespace('REDIS_')
        self._pool = redis.ConnectionPool(**opts)
        self._client = redis.StrictRedis(connection_pool=self._pool)

    def __getattr__(self, name):
        return getattr(self._client, name)

## 定义apscheduler扩展
class Apscheduler:
    """
    desc: 定时任务管理模块
    """
    def __init__(self):
        self._scheduler = None
        self._job_list = []

    def init_app(self, app):
        self._scheduler = GeventScheduler


# 使用扩展
## sea内置的celery异步任务插件，本项目暂未启用
# async_task = AsyncTask()

## peewee插件
pwdb = Peeweext(ns='PW_')

## redis插件
spredis = Redis()
