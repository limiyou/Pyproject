"""函数的返回值"""
'''def add(a,b):
    """两数相加"""
    c=a+b
    print(a+b)
    return(c)
#第1步：计算两个数，计算相加
#第2步：通过得到相加的值*6

#先把相加的数据存起来
#函数体执行以后得到的结果必须通过 return 返回
#return的作用：是为了得到函数计算以后的结果
#函数计算以后的结果，return的值，是给函数的调用方法使用的
result=add(4,5)  # c=a+b=4+5  ==>result = c
print(result*6)  #54
'''
def add1(a,b):
    c=a+b
    print(c)
    return a-b

#print（）的作用：是显示在屏幕上，和函数的返回值没有关系
#TODO:函数的返回值只能由 return 决定， yield
res=add1(4,5)
print(res*6)  #-6

#TODO:return，函数遇到return就终止
def add3(a,b):
    c=a+b
    print("函数没有执行完")
    return a-b
    print("函数执行完了")  #不会执行打印
res1=add3(4,5)
print(res1*6) #
