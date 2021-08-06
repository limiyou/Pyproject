

"""对象的初始化
TODO:对象：除了整个类都具备的属性，还有自己的特征，即 实例属性
     def __init__(self):
         pass
是在什么时候调用的？
    Dog(name='teddy',color='blue')自动调用init
    Dog.__init__()
    TODO:不要写成__int__

"""
class Dog:
    #类属性
    tailed =True
#定义一个特殊函数、方法，定义好的形式参数，最终在对象初始化的时候传入实际参数
    def __init__(self,name,color):
        '''初始化函数、初始化方法'''
        #自定义对象产生的过程

        #实例属性的产生:self.name定义一个叫做name的实例属性
        self.name=name
        self.color=color
    #实例方法
    def say(self):
        print("汪汪队")

teddy=Dog(name='teddy',color='blue')
teddy.say()
#获取实例属性
print(teddy.color)
#类不能调用实例属性
#print(Dog.color)  #报错


class Bus():
    def __init__(self,name,type,num):
        self.name=name
        self.type=type
        self.num=num
    def addOil(self):
        print("需要添加多少油？"+ self.num)

    def run(self):
        print("可以跑1000公里")
bus=Bus('奔驰品牌',"私家车", 50)
print(bus.name+'\n'+ bus.type +'\n'+str(bus.num))



class Phone():
    def __init__(self,name,brand,color):
        self.name=name
        self.brand=brand
        self.color=color
    def play(self):
        print("手机都可以可以打游戏")

Oppo=Phone("Android",'VIVO','red')
Iphone=Phone("ios",'apple','yello')
print(Oppo.color)
print(Oppo.brand)
print(Oppo.name)
print((Iphone.brand ) + Iphone.color)


