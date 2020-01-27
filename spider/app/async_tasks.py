from app.extensions import async_task

from sea.contrib.extensions.celery import cmd
@async_task.task
def test():
    print('task: xixixixi')
