"""
实例方法
第一个参数是self，在类和对象中实例方法用的最多

实例.方法（）
类.方法（）
类方法的表示：
@classmethod


静态方法：

"""


class Dog():
    taild=True
    """初始化函数，初始化方法"""
#自定义对象产生的过程
#实例属性的产生 self.name 定义一个叫做name 的实例属性
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def say(self,times):
        print(f"{self}汪汪了{times}次")
    #类方法，进化
    #声明：这是一个类方法
    @classmethod
    def jinhua(cls):
        print("狗类正在进化")
        Dog.tailed=False
teddy=Dog("taidi",'yellow')
print(teddy.say(6))
yingying=Dog("yingyong",'black')


Dog.jinhua()
print(teddy.tailed)