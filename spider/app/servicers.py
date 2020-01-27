import spidermanager_pb2
import spidermanager_pb2_grpc

from sea.servicer import ServicerMeta

from datetime import datetime

import threading
from gevent import monkey
monkey.patch_socket()

from app.utils import random_date
from app.spider.main import Engine
from app.async_tasks import test


class SpiderManagerServicer(spidermanager_pb2_grpc.SpiderServicer,
                            metaclass=ServicerMeta):
    """
    对外提供的爬虫管理服务，定义在spidermanager.proto文件中
    定义规范参考Protobuf
    """
    def SpiderConn(self, request, context):
        try:
            print('service ******' + request.keyswitch)
            if request.keyswitch == 'on':

                r = test.delay(2, 4)
                print(r.status)
                print(r.result)
                #Engine().loop()
                print('service ******')
            elif request.keyswitch == 'off':
                # if tasker.existed_job('spider'):
                #     tasker.stop_job('spider')
                pass
            else:
                return spidermanager_pb2.ConnReply(status='unknow', message=request.keyswitch)
        except Exception as e:
            print(e)
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
