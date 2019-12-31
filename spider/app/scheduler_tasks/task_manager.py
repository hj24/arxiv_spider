from gevent import monkey
monkey.patch_all()

from apscheduler.schedulers.gevent import GeventScheduler

from app.utils import singleton


@singleton
class Manager:
    """
    desc: 定时任务管理模块，单例模式
    """

    def __init__(self):
        self._scheduler = GeventScheduler()
        self._job_list = []

    def add_interval_job(self, job_id, desc, func, args, interval):
        try:
            self._scheduler.add_job(func=func, trigger='interval', id=job_id,
                                    name=desc, args=args, seconds=interval)
        except Exception as e:
            pass
        else:
            pass
        finally:
            pass

    def run(self):
        self._scheduler.start()




if __name__ == '__main__':
    import time
    m = Manager()
    def t():
        print('1234')
        time.sleep(1)
    m.add_interval_job('t', 'test t', t, args=[], interval=10)
    m.run()
    time.sleep(100)