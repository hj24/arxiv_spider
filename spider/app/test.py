from sea import current_app
from app.extensions import spredis
from sea import create_app



if __name__ == '__main__':
    import os

    print(os.environ.get('SEA_ENV'))

    root_path = os.path.abspath(os.path.dirname(__file__))
    create_app(root_path)

    from app.extensions import pwdb
    from app.model import SpConfiguration as spc

    print(pwdb.database.get_tables())
    r = spc.select().where(spc.interval==1).get()
    current_app.logger.info(r)
    current_app.logger.error(r)

    spredis.set('name', 'hj')

    print(spredis.get('name'))

    from app.settings import SpiderConfig

    print(SpiderConfig.count())

    # from app.spider.crawler import SpiderMan
    #
    # print(SpiderMan.generate_url())
    from app.model import Article

    print(dir(Article))
    print(dir(pwdb))
