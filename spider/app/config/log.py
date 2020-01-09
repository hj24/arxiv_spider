import os

from spider.app.config.settings import COMPLEX_FORMAT, SIMPLE_FORMAT
from spider.app.config.settings import LOG_PATH, LOG_NAME, LOG_VERSION
from spider.app.config.settings import LOG_FILE_FORMAT, LOG_CONSOLE_FORMAT
from spider.app.config.settings import FILE_HANDLER, CONSOLE_HANDLER, MODULE_HANDLER
from spider.app.config.settings import LOG_FILE_LEVEL, LOG_CONSOLE_LEVEL, LOG_MODULE_LEVEL


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
log_path = os.path.join(basedir, LOG_PATH)
log_file = os.path.join(log_path, LOG_NAME)

config = {
    'version': LOG_VERSION,
    'formatters': {
        'simple': {
            'format': SIMPLE_FORMAT,
        },
        'complex': {
            'format': COMPLEX_FORMAT,
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': LOG_CONSOLE_LEVEL,
            'formatter': LOG_CONSOLE_FORMAT
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': log_file,
            'level': LOG_FILE_LEVEL,
            'formatter': LOG_FILE_FORMAT
        },
        # 其他的 handler
    },
    'loggers':{
        '': {
            # 既有 console Handler，还有 file Handler
            'handlers': MODULE_HANDLER,
            'level': LOG_MODULE_LEVEL,
        },
        'StreamLogger': {
            'handlers': CONSOLE_HANDLER,
            'level': LOG_CONSOLE_LEVEL,
        },
        'FileLogger': {
            'handlers': FILE_HANDLER,
            'level': LOG_FILE_LEVEL,
        },
    }
}

if __name__ == "__main__":
    pass