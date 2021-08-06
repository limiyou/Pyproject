"""
#函数的调用，print的作用是讲数据答应在屏幕上，打印数据的意思
"""
print("hello world")
#input的作用：获取用户输入的内容，输入的参数是提示语
a=input("用户名：")
print(a) #打印a

#函数名称不能体现函数的作用时，用注释docstring
def func(a,b):
    """本函数是为了计算2个数的相乘 """
    print(a*b)
func(3,4)    