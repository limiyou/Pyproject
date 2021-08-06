""""
逻辑运算 and or not  ()设置优先级
成员运算 in not in
"""
a=(3 >4)
print(a)
b=4!=5
print(b)
#运算 and  每一个都为true
print (a and b)  # False
#运算 or  一个为true 即为true
print(a or b)  # True
# 练习
a=True
b==5==4  # False
c=5!=3  #True
print(a and b or c)
print(a or b and c)
#python的运算优先级：
#使用()设置优先级
print((a and b )or c)

#not
print (not b)
# name
name=("miyou")
print("m" in name)
print("h"in name)
print("li"not in  name)