"""
对数据变更（修改、增加、删除 ）的事务，必须提交事务。
"""



# 1. 连接数据库
# cursorclass=pymysql.cursors.DictCursor  : 游标将结果作为字典返回
import pymysql
# 1. 创建连接对象
conn = pymysql.connect(host='8.129.91.152', port=3306, user='future', password='123456',
                       cursorclass=pymysql.cursors.DictCursor)
#2. 获得游标对象
cur=conn.cursor()
sql1 = 'update futureloan.invest set amount=1000 where id=1'
sql2='update futureloan.invest set amount=999 where id=2'
#3.执行语句
cur.execute(sql1)
cur.execute(sql2)
#4.提交事务
conn.commit()
result=cur.execute('select * from futureloan.invest')  # 执行语句，返回值是 返回的记录数
#使用游标对象获得一条数据
res=cur.fetchmany(3)
print(res)
#5.关闭游标
cur.close()
#6.关闭连接
if conn is not None:
   conn.close()