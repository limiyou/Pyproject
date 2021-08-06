#encoding=utf8
import logging
# 1.  Logger  :  日志收集器
# 2. 日志输出类（ 文件FileHandler、流StreamHandler、多文件按时间TimedRotatingFileHandler，多文件按大小RotatingFileHandler）

from logging import Logger
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
from logging import FileHandler
# logging.error('error...')
# logger = logging.getLogger('wuji')   # getLogger返回具有指定名称的记录器，并在必要时创建它。
# logger1 = Logger(name='log1', level=logging.DEBUG)
logger1 = logging.getLogger("wuji")
# 把控制台输出添加到logger对象中
stream = logging.StreamHandler()  # StreamHandler是一个处理程序类，它将适当格式的日志记录写入流中
# stream.setFormatter(formatter)
# stream.setLevel(logging.DEBUG)
logger1.addHandler(stream)
logger1.setLevel(logging.DEBUG)
logger1.error('error')
logger1.info('info')
# 定制自己的logger的时候，一定要有logger1.addHandler()这个语句