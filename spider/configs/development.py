from configs.default import *
from celery.schedules import crontab

TIMEZONE = 'Asia/Shanghai'

GRPC_LOG_LEVEL = 'INFO'
DEBUG = True
GRPC_PORT = 9001

# Redis相关配置
REDIS_HOST = 'localhost'
REDIS_PORT = 6699
REDIS_DB = 0

# Apscheduler配置
#APS_SCHEDULER = 'blocking'

# # 异步任务
ASYNC_TASK_BROKER_URL = 'redis://localhost:6699/1'
ASYNC_TASK_RESULT_BACKEND = 'redis://localhost:6699/2'
ASYNC_TASK_IMPORTS = ['app.async_tasks']
ASYNC_TASK_TIMEZONE = TIMEZONE

ASYNC_TASK_BEAT_SCHEDULE = {
    'execute_per_week': {
        'task': 'app.async_tasks.run_spider',
        'schedule': crontab(day_of_week=1, hour=14, minute=59),
        #'args': (1, 2, 3)
    }
}

# bus 消息
# BUS_BROKER_URL = 'redis://redis:6699/0'
# BUS_IMPORTS = ['app.buses']