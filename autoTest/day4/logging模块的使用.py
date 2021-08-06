import logging
#如何获得一个日志对象(日志收集器)
logger=logging.getLogger() #1、TODO：日志收集器，只会收集默认级别日志及其以上的日志
print(logger.level) #2.查看当前默认级别  warning
logger.setLevel('INFO') #3. 修改日志级别

#4. 常见的日志级别
logging.debug('debug.....')
logging.info('info')
logging.warning("warning.....")
logging.error('error....')
logging.critical("critical....")

#5.在开发中，什么情况下会使用到logging.error()
try:
    int(input("请输入一个数字"))
except ValueError as e:
    logging.error("输入了一个非法类型的数字")
else:
    print("输入成功")
finally:
    print(5)


#记录用户行为，常常使用info
logging.info("用户【用户889】与2021-5-6 15:44登录系统")
logging.critical("用户【876】与2021-0506-15:56登录系统")

#6.如何把日志写到文件中  --配置
logger2=logging.getLogger()                              #6.1创建日志收集器
f=logging.FileHandler('2021-05-06.log',encoding='utf-8') #6.2 创建日志文件读写对象
formatter=logging.Formatter("%(asctime)s - %(name)s- %(levelname)s - %(message)s")
#print % 格式化的一种用法
#print("%(asctime)s - %(name)s- %(levelname)s - %(message)s" %{'asctime':'2021-05-06','name':'bbbb','levelname':'debug','message':"xxx出错了"})
f.setFormatter(formatter)                                #6.3 绑定日志输出格式
logger2.addHandler(f)                                    #6.4绑定日志文件读写对象 到 日志收集器对象
logger2.error('第34行出现的错误')
