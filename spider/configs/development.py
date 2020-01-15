from configs.default import *

GRPC_LOG_LEVEL = 'INFO'

# Redis相关配置
REDIS_HOST = 'localhost'
REDIS_PORT = 6699
REDIS_DB = 0

# Apscheduler配置
APS_SCHEDULER = 'gevent'

# # 异步任务
# ASYNC_TASK_BROKER_URL = 'redis://redis:6699/0'
# ASYNC_TASK_IMPORTS = ['app.tasks']
#
# # bus 消息
# BUS_BROKER_URL = 'redis://redis:6699/0'
# BUS_IMPORTS = ['app.buses']