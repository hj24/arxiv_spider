# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import spidermanager_pb2 as spidermanager__pb2


class SpiderStub(object):
  """The spider service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SpiderConn = channel.unary_unary(
        '/spider.Spider/SpiderConn',
        request_serializer=spidermanager__pb2.ConnRequest.SerializeToString,
        response_deserializer=spidermanager__pb2.ConnReply.FromString,
        )
    self.Report = channel.unary_unary(
        '/spider.Spider/Report',
        request_serializer=spidermanager__pb2.ReportRequest.SerializeToString,
        response_deserializer=spidermanager__pb2.ReportReply.FromString,
        )


class SpiderServicer(object):
  """The spider service definition.
  """

  def SpiderConn(self, request, context):
    """Control the start and stop of the spider
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Report(self, request, context):
    """Show apscheduler jobs and control them
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SpiderServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SpiderConn': grpc.unary_unary_rpc_method_handler(
          servicer.SpiderConn,
          request_deserializer=spidermanager__pb2.ConnRequest.FromString,
          response_serializer=spidermanager__pb2.ConnReply.SerializeToString,
      ),
      'Report': grpc.unary_unary_rpc_method_handler(
          servicer.Report,
          request_deserializer=spidermanager__pb2.ReportRequest.FromString,
          response_serializer=spidermanager__pb2.ReportReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'spider.Spider', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
