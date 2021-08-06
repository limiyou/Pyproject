def max(a,b):
    if a>b:
        return a
    else:
        return b
c=max(7,6)
print(c)





# def area(width,height):
#     return width * height
# def print_welcome(name):
#     print("welcome",name)
# print_welcome("miyou")
# w=7
# h=8
# print("width=",w,"height=",h,"area=",area(w,h))




#函数调用

# def printme(str):
#     print(str)
#     return
# printme("我要调用用户自定义的函数！")
# printme("再次调用同一函数")


#python 传不可变对象
#TODO:可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id。

# def change(a):
#     print(id(a))  #指向的是同一个对象
#     a=10
#     print(id(a)) #一个新对象
# a=1
# print(id(a))
# change(a)



#传可变对象实例
#TODO:可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了

# def changeme(mylist):
#     #修改传入的列表
#     mylist.append([1,2,3,4])
#     print("函数内取值：",mylist)
#     return
# #调用 changeme函数
# mylist=[10,20,30]
# changeme(mylist)
# print("函数外取值：",mylist)


#关键字参数


# def printhh(str):
#     print(str)
#     return
# #调用printhh函数
# printhh(str="limiyou")
#
# #函数参数的使用不需要使用指定顺序
# def printinfo(name,age):
#     print("名字：",name)
#     print("年龄：",age)
#     return
# #调用priintinfo 函数
# printinfo(age=18,name="小红")




#默认参数：调用函数时，如果没有传递参数，则会使用默认参数
# def printinfo(name,age=8):
#    '打印任何输入的字符串'
#    print('名字：',name)
#    print('年龄：',age)
#    return
# #调用printinfo函数
# printinfo(name='miyou')  #输出结果：名字： miyou 年龄： 8




#不定长参数：需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数

# def printinfo(arg1,*vartuple):
#     print("输出: ")
#     print(arg1)
#     print(vartuple)
#  #调用 printinfo函数
# printinfo(70,80,90)
#结果：输出:
#70
#(80, 90)

#如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量
def printinfo1(arg1,*vartuple):
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)#
#调用 printinfo1函数
printinfo1(10)
printinfo1(70,60,50)
# 以上实例输出结果：
# 输出:
# 10
# 输出:
# 70
# 60
# 50

#加了两个星号 ** 的参数会以字典的形式导入。

# def printinfo2(arg1, **vardict):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vardict)
# # 调用printinfo 函数
# printinfo2(1, a=2, b=3)




#return语句
#return[表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None

def sum(arg1,arg2):
    total=arg1+arg2
    print("函数内: ",total)
    return
total=sum(10,20)
print("函数外：",total)


def sum(arg1,arg2):
    total=arg1+arg2
    print("函数内: ",total)
    return total
total=sum(10,20)
print("函数外：",total)


