from .async_task import *


TESTING = False
DEBUG = True

PW_DB_URL = 'postgresql://postgres:180234sss@localhost:5432/forest'

MIDDLEWARES = [
    'sea.middleware.ServiceLogMiddleware',
    'sea.middleware.RpcErrorMiddleware',
    'peeweext.sea.PeeweextMiddleware',
]