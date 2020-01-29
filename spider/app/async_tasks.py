from app.extensions import async_task, spredis
from app.spider.main import Engine


@async_task.task
def set_spider(signal):
    spredis.set('sp', signal)

@async_task.task
def run_spider():
    flag = spredis.get('sp').decode('utf-8')
    if flag == 'run':
        Engine().loop()
    elif flag == 'stop':
        pass
    else:
        pass
