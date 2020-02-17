import spidermanager_pb2
import spidermanager_pb2_grpc

from sea.servicer import ServicerMeta
from app.async_tasks import set_spider
from app.dao import RedisDao


class SpiderManagerServicer(spidermanager_pb2_grpc.SpiderServicer,
                            metaclass=ServicerMeta):
    """
    对外提供的爬虫管理服务，定义在spidermanager.proto文件中
    定义规范参考Protobuf
    """
    def SpiderConn(self, request, context):
        try:
            if request.keyswitch == 'on':
                r = set_spider.delay('run')
            elif request.keyswitch == 'off':
                r = set_spider.delay('stop')
            else:
                return spidermanager_pb2.ConnReply(status='unknow', message=request.keyswitch)
            _status = str(r.status)
        except Exception as e:
            print(e)
            return spidermanager_pb2.ConnReply(status='failed', message=request.keyswitch)
        else:
            return spidermanager_pb2.ConnReply(status=_status, message=request.keyswitch)

    def Report(self, request, context):
        try:
            _dao = RedisDao()
            counter = _dao.get_counter()
            val = [str(v) for v in counter.values()]
            str_cnt = '-'.join(val)
            replay_body = spidermanager_pb2.ReportReply()
            replay_body.status = str_cnt
            if request.query == 'lists':
                articles = _dao.get_newest_articles()
                for a in articles:
                    replay_body.detail.append(a)
            else:
                raise Exception('unkonw args')
        except Exception:
            _replay_body = spidermanager_pb2.ReportReply()
            _replay_body.status = 'failed'
            return _replay_body
        else:
            return replay_body
