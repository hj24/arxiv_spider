from sea import current_app
from app.extensions import spredis
from sea import create_app

from sea.contrib.extensions.celery import cmd

if __name__ == '__main__':
    import os

    print(os.environ.get('SEA_ENV'))

    root_path = os.path.abspath(os.path.dirname(__file__))
    create_app(root_path)

    from app.async_tasks import test

    def add_t():
        r = test.delay(4, 4)
        print(r.status)
        print(r.result)

    r = test.delay(6, 4)
    import time
    import threading
    t = threading.Thread(target=add_t)
    t.start()
    time.sleep(5)

    print(r.status)
    print(r.result)
    spredis.set('hj', '24')
    print(spredis.get('hj'))
