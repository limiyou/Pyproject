# coding:utf8
import logging


def  create_logger():
    """创建一个配置好的日志收集器"""
    logger = logging.getLogger()    # 1. 创建日志收集器
    logger.setLevel('DEBUG')      # 2. 设置收集日志级别
    # 3. 设置日志输出的FileHandler
    # FileHandler是一个处理程序类，它将格式化的日志记录写入磁盘文件。
    f = logging.FileHandler('test.log',encoding='utf8')
    # 4. 获得一个Formatter的对象，Formatter是logging模块中定义的一个用于格式化输出的类。
    formatter = logging.Formatter('%(asctime)s -- [%(filename)s - line:%(lineno)d] -%(levelname)s:%(message)s')
    f.setFormatter(formatter)
    logger.addHandler(f)
    return logger
