"""函数的参数
##位置参数
"""
def add(a,b):
    c=a+b
    return c
res=add(6,7)    #add(6,7)-->13
print(res) #18

#报错，因为参数不匹配，没有成CP,
#res=add(6,7,8)

#CP是按位置、按顺序来配对的
#形式参数和实际参数的这种位置关系就叫位置参数
res=add("yuze","wang")
print(res)

#TODO:关键字参数:函数调用时，通过给实际参数贴标记，标记是形式参数的变量名
#通过关键字参数，可以不按照顺序来配对
#关键字参数的作用：当参数很多的时候，
res=add(b="yuze",a='wang')
print(res) # wangyuze

#TODO:关键字参数，要放到位置参数的后面
#res=add(b='yuze','wang') #报错
res=add("wang",b='yuze')
print(res)


def add1(c,d):
    return c+d
res1=add1("li",d="miyou")
print(res1)


