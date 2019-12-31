import threading
from functools import wraps


def singleton(cls):
    _instance = {}
    _lock = threading.Lock()
    @wraps(cls)
    def instance(*args, **kwargs):
        print(*args, **kwargs)
        if cls not in _instance:
            with _lock:
                if cls not in _instance:
                    _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return instance