
from .async_task import *





TESTING = False
DEBUG = True

MIDDLEWARES = [
    'sea.middleware.ServiceLogMiddleware',
    'sea.middleware.RpcErrorMiddleware',
    
]