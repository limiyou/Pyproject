"""
编写如下程序


有以下数据来自于一个嵌套字典的列表（可自定义这个列表），例如：

person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} , .... 其他]

创建一个txt文本文件，来添加数据

a.第一行添加如下内容：

name,age,gender,hobby,motto


b.从第二行开始，每行添加具体用户信息，例如：

yuze,17,男,假正经, I am yours

cainiao,18,女,看书,Lemon is best!
"""
with open("homework.txt",mode='w',encoding="utf8")as f:
    f.write("name,age,gender,hobby,motto")









"""有两行数据，存放在txt文件里面(手动建立文件，并添加如下数据)：

url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456

url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000

请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）

[{'url':'/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},{'url':'/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}] 

"""

with open("homework2.txt",encoding="utf8") as f2:
    print(f2.read())

