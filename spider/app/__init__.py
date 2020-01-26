from sea.app import BaseApp

from app.extensions import tasker


class App(BaseApp):

    def ready(self):
        def p():
            p('***************************')

        tasker.add_cron_job_per_week(job_id='x', desc='xxx',
                                     func=p, args=[], d_of_w='sun',
                                     hour=23, min=55)
        tasker.start()
        print('start task')