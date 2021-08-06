"""默认参数
在函数定义的时候，给形式参数一个默认的值
默认参数的作用：可以少写实际参数
"""
def add(a,b=9):
    return a+b

#print(add(3,4)) #7
#print(add(a=3,b=4))
#print(add(8)) #b默认为9，8默认与a配对
#print(add(b=7)) #报错，因为 a没有实际参数


def add(e,f=10):
    return e+f
print(add(4))