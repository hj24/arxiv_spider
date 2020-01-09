from gevent import monkey
monkey.patch_all()

from apscheduler.schedulers.gevent import GeventScheduler

from app.utils import singleton, get_logger


logger = get_logger(__name__)

@singleton
class Manager:
    """
    desc: 定时任务管理模块，单例模式
    """

    def __init__(self):
        self._scheduler = GeventScheduler()
        self._job_list = []

    def add_interval_job(self, job_id, desc, func, args, interval):
        """
        添加以时间间隔执行的定时任务

        :param job_id: 定时任务唯一id
        :param desc: job的描述
        :param func: job中待执行的方法
        :param args: 方法的传参
        :param interval: 时间间隔
        :return: 返回True则任务添加成功，否则失败
        """
        flag = False
        try:
            self._scheduler.add_job(func=func, trigger='interval', id=job_id,
                                    name=desc, args=args, seconds=interval)
        except Exception as e:
            logger.error('add job %s failed: %s', str(job_id), e)
        else:
            self._job_list.append(job_id)
            flag = True
        finally:
            return flag

    def add_cron_job_per_week(self, job_id, desc, func, args, d_of_w, hour, min):
        """
        添加corn类型的定时任务
        """
        try:
            self._scheduler.add_job(func=func, trigger='cron', id=job_id,
                                    name=desc, args=args, day_of_week=d_of_w,
                                    hour=hour, minute=min)
        except Exception as e:
            logger.error('add job %s failed: %s', str(job_id), e)
            return False
        else:
            return True

    def stop_job(self, job_id):
        """
        通过job id来关闭某个定时任务

        :param job_id: job id
        :return: 返回True则任务停止成功，否则失败
        """
        try:
            for job in self._job_list:
                if job == job_id:
                    self._scheduler.remove_job(job_id)
                    break
        except Exception as e:
            logger.error('remove job failed, job not found: %s', e)
            return False
        else:
            return True

    def modify_job(self, job_id, **kwargs):
        try:
            self._scheduler.modify_job(job_id=job_id, **kwargs)
        except Exception as e:
            logger.error('modify failed: %s', e)
            return False
        else:
            return True

    def get_jobs(self):
        return self._scheduler.get_jobs()

    def run(self):
        try:
            self._scheduler.start()
        except Exception as e:
            logger.error('jobs start failed: %s', e)
            return False
        else:
            return True

    def close(self, *, wait=False):
        """
        停止所有定时任务

        :param wait: 为True时等待所有定时任务执行结束后关闭，否则强行关闭
        :return: True表示执行成功
        """
        try:
            self._scheduler.shutdown(wait=wait)
        except Exception as e:
            logger.error("close failed, please try system-level kill command: %s", e)
            return False
        else:
            return True

if __name__ == '__main__':
    """
    task manager simple test
    """
    import time
    m = Manager()

    def t():
        print('1234')
        time.sleep(1)

    def t2():
        print('123456')
        time.sleep(1)

    m.add_interval_job('t', 'test t', t, args=[], interval=10)
    m.add_cron_job_per_week('t2', 'test t2', t2, args=[], d_of_w='thu', hour=23, min=12)
    m.modify_job('t', next_run_time=1)
    m.run()

    time.sleep(300)