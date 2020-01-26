import threading
from random import randint
from functools import wraps

import pendulum


# 系统中的时区
spider_target_tz = 'US/Eastern'
spider_local_tz = 'Asia/Shanghai'

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

def random_date(base=pendulum.now(), night=False, _range=7):
    """
    根据基准日期中的时区，生成_range范围内的随机的日期
    根据night的bool值可选是否只生成晚上的时间
    _range以天为单位
    """
    left = base
    right = base.add(days=_range)
    choice = [d for d in pendulum.period(left, right)]
    _date = choice[randint(0, len(choice))]
    if not night:
        return _date
    _hour = _date.hour
    if _hour >= 6 and _hour <= 19:
        _min = 19 - _hour
        _max = 24
        _add = randint(_min, _max) % 24
        return _date.add(hours=_add)
    return _date

if __name__ == '__main__':
    print(pendulum.now(spider_local_tz))
    print(pendulum.now().year)
    print(pendulum.now().month)
    print(pendulum.now().day)
    print(pendulum.now().hour)
    print(pendulum.now().minute)
    print(random_date(night=True))
