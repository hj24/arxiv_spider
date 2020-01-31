from app.extensions import spredis
from sea import create_app


if __name__ == '__main__':
    import os
    print('start test')
    print('SEA_ENV: ', os.environ.get('SEA_ENV'))
    os.environ['SEA_ENV'] = 'production'

    root_path = os.path.abspath(os.path.dirname(__file__))
    create_app(root_path)
    from app.spider.main import Engine
    #Engine().loop()
    from app.extensions import async_task
    from app.model import Article
    print('celery time: ', async_task.now())

    spredis.set('hj', 'revoke')
    print(spredis.get('hj'))

    print(spredis.get('sp'))
    #spredis.
    print(Article.select().where(Article.id == 1).get())
