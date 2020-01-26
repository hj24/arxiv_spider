import redis
#from apscheduler.schedulers.gevent import GeventScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from peeweext.sea import Peeweext
# from sea.contrib.extensions.celery import AsyncTask


config2scheduler = {
    #'gevent': GeventScheduler,
    'blocking': BlockingScheduler,
    'background': BackgroundScheduler,
}

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
# class TasksManager:
#
#     def __init__(self):
#         self._scheduler = None
#         self._job_list = []
#
#     def init_app(self, app):
#         opts = app.config.get_namespace('APS_')
#         sch = opts.get('scheduler', 'gevent')
#         self._scheduler = config2scheduler[sch]()
#
#     def __getattr__(self, item):
#         return getattr(self._scheduler, item)
#
#     def add_cron_job_per_week(self, job_id, desc, func, args, d_of_w, hour, min):
#         """
#         添加corn类型的定时任务
#         """
#         try:
#             self._scheduler.add_job(func=func, trigger='cron', id=job_id,
#                                     name=desc, args=args, day_of_week=d_of_w,
#                                     hour=hour, minute=min)
#         except Exception as e:
#             raise e
#         else:
#             self._job_list.append({'job_id': job_id, 'desc': desc})
#
#     def add_job(self, job_id, desc, func, date, args):
#         """
#         添加一次性的定时任务，在run_date指定的时间运行
#         """
#         try:
#             self._scheduler.add_job(func=func, trigger='date', id=job_id,
#                                     name=desc, args=args, run_date=date,
#                                     replace_existing=True)
#         except Exception as e:
#             raise e
#         else:
#             self._job_list.append({'job_id': job_id, 'desc': desc})
#
#     def stop_job(self, job_id):
#         """
#         通过job id来关闭某个定时任务
#         """
#         try:
#             for job in self._job_list:
#                 if job['job_id'] == job_id:
#                     self._scheduler.remove_job(job_id)
#                     self._job_list.remove(job)
#                     break
#         except Exception as e:
#             raise e
#
#     def existed_job(self, job_id):
#         try:
#             for job in self._job_list:
#                 if job['job_id'] == job_id:
#                     return True
#             return False
#         except Exception as e:
#             raise e
#
#     def get_jobs(self):
#         return self._job_list


# 使用扩展
## sea内置的celery异步任务扩展
# async_task = AsyncTask()
# bus = Bus()

## peewee插件
pwdb = Peeweext(ns='PW_')

## redis插件
spredis = Redis()

## 定时任务扩展
#tasker = TasksManager()
