"""

静态方法：当想在一个类中定义一个方法，和这个类或者对象没有直接的关系
        在方法当中，还没有使用到类或对象


类和对象，都可以调用
静态方法存在的理由，只是放在类里面方遍管理

"""


class Dog():
    taild=True
    """初始化函数，初始化方法"""
#自定义对象产生的过程
#实例属性的产生 self.name 定义一个叫做name 的实例属性
    def __init__(self,name,color):
        self.name=name
        self.color=color
    @staticmethod
    def say_static(times):
        print(f"汪汪了{times}次")
    #类方法，进化
    #声明：这是一个类方法

    @classmethod
    def jinhua(cls):
        print("狗类正在进化")
        Dog.tailed=False
teddy=Dog("taidi",'yellow')


# Dog.jinhua()
# print(teddy.tailed)

#静态函数的调用
print(teddy.say_static(7))