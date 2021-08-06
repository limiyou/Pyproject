#coding:utf8
import json
#创建一个字典对象
mysql={
    "user":"root",
'password':'123456',
    'db':'lemon',
    'port':3308

}
json.dump(obj=mysql,fp=open("mysql.json",'w'))