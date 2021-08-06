"""
**只能收集关键字参数 **kwds
不定长参数的作用：在函数定义时，不知道有多少个参数会传进来
"""
def add(a,**b):
    print(a)
    print(b)

add(3,c=6,d=7)
print("hello","world","excel")

def add(aa,*cc,**bb):
    print(aa)
    print(cc)
    print(bb)
add(3,4,10,f=7,g=8)   #aa与3配对，cc收集了所有的没有配对的实际参数，4,10,bb收集了所有的关键字参数
#TODO:*收集所有的没有配对的实际参数；**收集所有的关键字参数

