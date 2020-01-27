from sea import current_app
from app.extensions import spredis
from sea import create_app



if __name__ == '__main__':
    import os

    print(os.environ.get('SEA_ENV'))

    root_path = os.path.abspath(os.path.dirname(__file__))
    create_app(root_path)

    from app.spider.main import Engine

    from app.extensions import tasker
    from app.utils import spider_local_tz

    def p():
        print('*******')

    import pendulum
    from datetime import datetime

    tasker.add_job(job_id='p', desc='ppp', func=p, args=[], date=datetime(year=2020, month=1, day=27, hour=17, minute=34))
    tasker.start()
    import time
    time.sleep(600)
