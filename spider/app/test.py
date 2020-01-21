from sea import current_app
from app.extensions import spredis
from sea import create_app



if __name__ == '__main__':
    import os

    print(os.environ.get('SEA_ENV'))

    root_path = os.path.abspath(os.path.dirname(__file__))
    create_app(root_path)

    from app.spider.main import Engine

    Engine().loop()
