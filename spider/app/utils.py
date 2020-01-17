import threading
from functools import wraps


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

def clear_str(strings):
    """
    删除字符串的多余换行，制表符，空格
    """
    remove_n = strings.replace('\n', '')
    remove_r = remove_n.replace('\r', '')
    remove_t = remove_r.replace('\t', '')
    return remove_t.strip()
