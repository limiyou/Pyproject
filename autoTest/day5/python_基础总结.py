#encoding:utf8
import sys
#1.assert
# l=[1,2,3,4]
# try:
#     9==l[2]
#
# except :
#         print('判断错误')
# else:
#         print('aaa')
# finally:
#         print("无论如何都会执行的语句")


#2.raise
# x=10
# if x>5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
# try:
#     raise NameError('HiThere')
# except NameError:
#         print('An exception flew by!')
#         raise
from accepts import accepts

"""定义一个PageNotFound 的异常，当页面不存在的时候，抛出异常"""
class PageNotFound(Exception):
    def __init__(self,msg,*args,**kwargs):
        self.msg=msg
        pass
try:
    raise PageNotFound(msg="页面未找到")
except PageNotFound as e:
    print(e.msg)


#3.yeild
def f():
    print("hi")
    yield 1
    yield 2
    yield 3
g=f()
#next(g) 会自动取出当前对象的下一个元素
for value in g:
    print(value)

#4.global
z=0
def f():
    global  z
    z=1
    print(z)

g=f()  #1


#


#6.函数
#6.1 传参  其实就是赋值
#TODO：面试：函数传参，传的是引用
def f1(a,b):
    print(a,b)
f1(1,2)

#7.类
class Student(object):
    """学生类"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def modify_name(self,name):
        self.name=name
stu=Student("MIYOU",2)
print("修改前的name",stu.name)
stu.modify_name("liyijin")
print("修改后的名字",stu.name)


#奥特曼打怪兽的例子
class Animal(object):
    def beaten(self):
        pass
class Cat(Animal):
    def beaten(self):
        print("喵喵~~~")
class Dog(Animal):
    def beaten(self):
        print("汪汪~~~")
class ATM(object):
    def beat(self,animal):
        """
        :param animal: 被打的怪兽
        :return: None
        """
        animal.beaten()
dijia=ATM()
hello_kitty=Cat()
black_police=Cat()
wangwang=Dog()
dijia.beat(hello_kitty)
dijia.beat(black_police)
dijia.beat(wangwang)



#8.闭包
#用一个函数把一个变量和一个函数包起来

#使用闭包实现累加功能（特点：一个数【变量】，一个加【函数】）
def f():
    number=0

    def add(x):
        nonlocal number
        number+= x
        return number
    return add
## f()返回的是一个add()函数的引用
accumulate=f()#把函数名绑到 accurate 变量
print(accumulate(1))
print(accumulate(2))
print(accumulate(3))
print(accumulate(4))


#9.

def run_log(f):
    """@run_log的装饰器"""
    def inner():
        print('函数开始运行')
        f() # 调用传过来的函数，其实就是调用被装饰的函数
    return inner


def func1():
    print('Hi,同学们')
def func2():
    print('Hi,同学们')


run_log(func1)  # 返回值是inner
run_log(func1)()  # 运行inner方法
# 我们可以用@run_log简化以上写法

@run_log
def func3():
    print('Hi,同学们')

@run_log
def func4():
    print('Hi,func4')


# @run_log
def func5():
    print('Hi,func5')

func3()
func4()
func5()

# 用装饰器实现参数检查
# pip install accepts
# accepts可以实现对函数的参数类型进行检查

@accepts(int,float)
def demo(a,b):
    print(a,b)