#coding:utf8
import configparser
config=configparser.ConfigParser() #创建一个解析器
config.read("conf.ini")
print(config)
print(config['mysql']['host'])#->str
print(config["mysql"]['user'])#->str
print(config["mysql"]['port']) #int
print(config['DIRS']['dir1'])#->str
