"""
位置参数一定要一一对应
关键字参数和默认参数一定要放在位置参数的后面
不定长参数： *剩下的位置参数， **关键字参数

解包：函数调用
"""

def add(a,b):
    return a+b
print(add(3,b=4))


#解包
def run(a,b):
    print(a)
    print(b)
# li=[3,4]
# run(*li)


#字典的解包

d={"a":3,"b":4}

run(a=3,b=4)