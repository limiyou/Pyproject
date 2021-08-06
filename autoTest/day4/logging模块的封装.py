import  logging
def creat_logger():
    """创建一个配置好的日志收集器"""
    logger=logging.getLogger()#1.创建日志收集器

    logger.setLevel("DEBUG")#2.设置级别
    #fileHandler是一个处理程序类，将格式化的日志记录写入磁盘文件
    f=logging.FileHandler("test.log","encoding=utf8") #3.设置日志输出的FileHandler
    #4.获得一个Formatter的对象，Formatter是logging模块中定义的一个用于格式化输出的类
    formatter=logging.Formatter("%(asctime)s--[%(filename)s--%(linename)d]--%(levelname)s - %(message)s")
    f.setFormatter(formatter)
    logger.addHandler(f)
    return logger
