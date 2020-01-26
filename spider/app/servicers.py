import spidermanager_pb2
import spidermanager_pb2_grpc

from sea.servicer import ServicerMeta

# from datetime import datetime
#
# from app.extensions import tasker
# from app.utils import random_date
# from app.spider.main import Engine


class SpiderManagerServicer(spidermanager_pb2_grpc.SpiderServicer,
                            metaclass=ServicerMeta):
    """
    对外提供的爬虫管理服务，定义在spidermanager.proto文件中
    定义规范参考Protobuf
    """
    def SpiderConn(self, request, context):

        # def setup_spider():
        #     _date = random_date()
        #     _year = _date.year
        #     _month = _date.month
        #     _day = _date.day
        #     _hour = _date.hour
        #     _minutes = _date.minute
        #     _engine = Engine()
        #     print('setip spider &&&&&&&&&&&&&&&&&&&&&&&&')
        #     tasker.add_job(job_id='spider', desc='spider task', func=_engine.loop,
        #                    date=datetime(year=2020, month=1,
        #                                  day=26, hour=17, minute=23),
        #                    args=[])

        try:
            print('service ******' + request.keyswitch)
            if request.keyswitch == 'on':
                # tasker.add_cron_job_per_week(job_id='setup', desc='setup a spider job',
                #                              func=setup_spider, args=[], d_of_w='sun',
                #                              hour=0, min=0)
                #Engine().loop()
                print('service ******')
            elif request.keyswitch == 'off':
                # if tasker.existed_job('spider'):
                #     tasker.stop_job('spider')
                pass
            else:
                return spidermanager_pb2.ConnReply(status='unknow', message=request.keyswitch)
        except Exception:
            return spidermanager_pb2.ConnReply(status='failed', message=request.keyswitch)
        else:
            return spidermanager_pb2.ConnReply(status='success', message=request.keyswitch)

    def TasksList(self, request, context):
        # try:
        #     replay_body = spidermanager_pb2.ListReply()
        #     if request.query == 'lists':
        #         job_list = tasker.get_jobs()
        #         for job in job_list:
        #             task = replay_body.JobList.add()
        #             task.jobid = job['job_id']
        #             task.detail = job['details']
        #         replay_body.status = 'success'
        #     else:
        #         raise Exception('unkonw args')
        # except Exception:
        #     _replay_body = spidermanager_pb2.ListReply()
        #     _replay_body.status = 'failed'
        #     _replay_body.JobList.add()
        #     return _replay_body
        # else:
        #     return replay_body
        pass
