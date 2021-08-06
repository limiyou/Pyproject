#coding:utf8
import json
#读取文件
f=open("mysql.json",mode='r')
mysql=json.load(fp=f)
#修改，:把端口3306修改为3307
print(mysql)
mysql['port']=3309
#写入
json.dump(obj=mysql,fp=open("mysql.json",mode='w'))
