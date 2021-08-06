# 修改变量

"""
def add(a,b):
    #局部变量
   c=a+b
   return c
#todo:外面是不能修改函数内部变量
#c_copy #会报错

"""


#todo:函数内部可以修改全局变量，但是 要加上 global
c=8
def add(a,b):
    #局部作用域
    global c
    c=c+3
    #c+=3
    return c+a+b
print(add(1,2))





