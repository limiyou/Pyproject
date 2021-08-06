#coding=utf8
#什么是json:文本、字符串、有固定的格式
import json
#load 可以把类文件对象转化成Python对象
import jsonpath as jsonpath

f=open(file='swagger.json') #创建一个文件对象
swagger=json.load(f)     #返回值是一个python对象，把返回值赋值给一个对象swagger
#print(type(swagger))
print(swagger['info'])
print(swagger['info']['description'])
print(jsonpath.jsonpath(swagger,"$.info.description")[0])