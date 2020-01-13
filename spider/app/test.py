from app.extensions import Redis

from sea import create_app

if __name__ == '__main__':
    import os

    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    create_app(root_path)

    from app.extensions import pwdb
    from app.model import SpConfiguration as spc

    print(pwdb.database.get_tables())
    r = spc.select().where(spc.interval==1).get()
    print(r)