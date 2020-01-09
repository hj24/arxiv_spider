import os

# 后台根目录
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

"""
后台版本信息
"""
VERSION = 1

"""
日志相关配置
handler部分:
  提供了两种handler: console, file
  分别是输出到控制台和文件

logger部分:
  提供了三种级别的logger: module/file/stream 
  接收一个列表，表示不同级别的logger对应的handler模式，可多选
  console是输出到控制台，file是输出到日志文件，与handler对应
"""
# 日志路径
LOG_PATH = 'log'
LOG_NAME = 'spider.log'

# 日志版本
LOG_VERSION = 1

# 日志级别
LOG_FILE_LEVEL = 'DEBUG'
LOG_CONSOLE_LEVEL = 'DEBUG'
LOG_MODULE_LEVEL = 'DEBUG'

# 日志输出级别,
CONSOLE_HANDLER = ['console']
FILE_HANDLER = ['console', 'file']
MODULE_HANDLER = ['console', 'file']

# 日志格式
LOG_FILE_FORMAT = 'simple'
LOG_CONSOLE_FORMAT = 'simple'

# 日志内容格式
SIMPLE_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
COMPLEX_FORMAT = ''