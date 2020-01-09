import threading
import logging.config
from functools import wraps

from spider.app.config import log


logging.config.dictConfig(log.config)

def singleton(cls):
    _instance = {}
    _lock = threading.Lock()
    @wraps(cls)
    def instance(*args, **kwargs):
        if cls not in _instance:
            with _lock:
                if cls not in _instance:
                    _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return instance

def get_logger(name):
    if isinstance(name, str):
        return logging.getLogger(name)
    else:
        raise TypeError