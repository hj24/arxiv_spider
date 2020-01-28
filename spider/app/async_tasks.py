from app.extensions import async_task
from app.extensions import spredis


@async_task.task
def test(x, y):
    return x+y

@async_task.task(bind=True)
def test2(self, x, y, z):
    with open('a.text', 'w') as fw:
        fw.write(str(x + y + z))
    spredis.set('sp', self.request.id)

@async_task.task
def contorl_test2():
    import time
    time.sleep(180)
    idx = spredis.get('sp')
    from celery.app.control import Control
    c = Control(async_task)
    c.revoke(idx, terminate=True)