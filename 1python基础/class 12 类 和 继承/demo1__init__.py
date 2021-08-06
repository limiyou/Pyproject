
# 实例化
# 通过一个类去创建一个对象，产生对象的过程
# --》函数调用


class Dog():
    taild=True
    """初始化函数，初始化方法"""
#自定义对象产生的过程
#实例属性的产生 self.name 定义一个叫做name 的实例属性
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def say(self):
        print("汪汪")
teddy=Dog("taidi",'yellow')
print(teddy.color)


class Dog1():
    taied1=True
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def say(self):
        print("汪汪汪")
xiaohuang=Dog1("小黄","yellow")
print(xiaohuang.name)