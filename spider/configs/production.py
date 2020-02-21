# from configs.default import *
# import os
#
# DEBUG = False
#
# ASYNC_TASK_BROKER_URL = os.environ['ASYNC_TASK_BROKER_URL']
from configs.default import *
from celery.schedules import crontab

TIMEZONE = 'Asia/Shanghai'

GRPC_LOG_LEVEL = 'INFO'
DEBUG = True
GRPC_PORT = 9001

# Redis相关配置
REDIS_HOST = '116.62.125.253'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = '180234sss'

# Apscheduler配置
#APS_SCHEDULER = 'blocking'

# # 异步任务
ASYNC_TASK_BROKER_URL = 'redis://:180234sss@116.62.125.253:6379/1'
ASYNC_TASK_RESULT_BACKEND = 'redis://:180234sss@116.62.125.253:6379/2'
ASYNC_TASK_IMPORTS = ['app.async_tasks']
ASYNC_TASK_TIMEZONE = TIMEZONE

ASYNC_TASK_BEAT_SCHEDULE = {
    'execute_per_week': {
        'task': 'app.async_tasks.run_spider',
        'schedule': crontab(day_of_week=0, hour=7, minute=30),
        #'args': (1, 2, 3)
    }
}

# consul 配置
CONSUL_SERVER_NAME = 'spider'
CONSUL_SERVER_HOST = '116.62.125.253'
CONSUL_REGISTER_IP = '116.62.125.253'
CONSUL_REGISTER_PORT = GRPC_PORT
