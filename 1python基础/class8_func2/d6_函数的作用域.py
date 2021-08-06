#全局作用域
#全局变量：函数外部定义的变量，叫做全局变量
#局部变量：在函数内部定义的变量，仅限函数内部可以使用，函数外部无法使用
def add(a,b):
    #局部作用域
   c=a+b
   return c
#不能直接使用c
#TODO:局部变量不能在全局作用域获取
c=add(4,5)
print(c)




#TODO:局部作用域可以使用全局变量
C=6
def minus(a,b):
    d=a+b
    print(d-c)
    return d-c
minus(3,7)


