"""
pymysql  :  用于操作MySQL的Python版的客户端
安装： pip install pymysql
文档：https://pymysql.readthedocs.io/en/latest/
https://www.runoob.com/python3/python3-mysql.html
"""
#1.如何连接数据库
import pymysql
conn=pymysql.connect(host='8.129.91.152',port=3306,user='future',passwd='123456',
                     cursorclass=pymysql.cursors.DictCursor)
#2.获得游标对象
cur=conn.cursor()
result = cur.execute('select * from futureloan.invest')  # 执行语句，返回值是 返回的记录数
print(result) #条数
#使用游标对象获得一条数据
data=cur.fetchone()#获取一条数据
#print(data)
#使用游标对象获得部分数据数据
res=cur.fetchmany(3)
#print(res)
#使用游标对象获得所有数据
res_all=cur.fetchall()