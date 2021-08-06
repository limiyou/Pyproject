"""
1,实例属性一般在__init__方法当中定义

2.什么时候设置类属性，什么时候设置实例属性

先设置实例属性，再检查一下是不是每个成员值都是同一个


3.方法，实例方法优先

方法：本质是函数，是动词，存储一段逻辑
属性：本质是变量，是名词，存储数据，赋值的


TODO：__init__没有返回值，返回值必须为none
   函数如果不return，默认返回none
"""

class Mobile():
    def __init__(self,brand,model,number):
        self.brand=brand
        self.model=model
        self.number=number


    def call(self):
        # self.number="123456"
        print('正在打电话  ')

iphone=Mobile("apple","xr",'12222')
iphone.call()
print(iphone.number)


class Iphone():
    #brand="apple"
    def __init__(self,model,brand="apple"):
        self.brand = brand
        self.model = model