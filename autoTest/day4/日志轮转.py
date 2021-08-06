# coding:utf8

import logging
import time
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler

# RotatingFileHandler是记录到一组文件的处理程序，当当前文件达到一定大小时，
# 该处理程序将从一个文件切换到下一个文件。

# 实现日志  写在多个文件中
logger = logging.getLogger()
logger.setLevel('DEBUG')
# f = RotatingFileHandler('wuji.log',encoding='utf8',maxBytes=1024,backupCount=3)  # 按大小轮转
f = TimedRotatingFileHandler(filename='miyou_0507',when='D',interval=1,backupCount=3)  # 按时间
f.setLevel('DEBUG')
f.setLevel('DEBUG')
formatter = logging.Formatter('%(asctime)s -- [%(filename)s - line:%(lineno)d] -%(levelname)s:%(message)s')
f.setFormatter(formatter)
logger.addHandler(f)


for i in range(20):

    logger.info('---miyou i love you！----')
    logger.info('--forever！')
    time.sleep(0.5)

# error  一个文件  ，info一个文件  是怎么做到的？
# logger_error  logger_info  两个  日志收集器
# logger_error.error()
# logger_info.info()