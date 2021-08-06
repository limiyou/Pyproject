# coding:utf8

from autoTest.day4.common.mylogger2 import create_logger


error_logger1 = create_logger("ERROR",'error')
critical_logger2=create_logger('CRITICAL','critical')
error_logger1.error('这个是用的我自己的配置的error的log')
critical_logger2.critical("这个是我配置的critiacal的log")