import pickle

from app.extensions import spredis
from sea import create_app


if __name__ == '__main__':
    import os
    print('start test')
    print('SEA_ENV: ', os.environ.get('SEA_ENV'))
    os.environ['SEA_ENV'] = 'development'

    root_path = os.path.abspath(os.path.dirname(__file__))
    create_app(root_path)
    from app.spider.main import Engine
    from app.extensions import async_task
    from app.model import Article
    from app.dao import RedisDao
    #Engine().loop()
    _dao = RedisDao()
    print(_dao.get_counter())
    for a in _dao.get_newest_articles():
        print(a)

    spredis.delete("articles")
    spredis.delete("counter")
    from sea import current_app
    c = current_app.config.get_namespace("CONSUL_")
    print(c)
    
    
    