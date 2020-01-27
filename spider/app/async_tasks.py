from app.extensions import async_task


@async_task.task
def test(x, y):
    return x+y
