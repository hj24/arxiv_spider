from configs.default import *


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

# bus 消息
# BUS_BROKER_URL = 'redis://redis:6699/0'
# BUS_IMPORTS = ['app.buses']