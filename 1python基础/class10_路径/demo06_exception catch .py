
"""
#异常捕获


try:
   要执行可能发生异常的代码
except:
     程序发生异常以后，希望程序做的事情
"""
#todo:程序先执行 try 当中的代码，一旦try当中某个代码报错，会执行except，try剩下的代码不会再执行
#
# try:
#     print("正在运行程序")
#     a=1/0 #不会执行，会直接执行except 语句
#     print(f"计算结果：{a}")
# except:
#     print("我知道1不能/0，需要更改除数")
# print("剩下的程序")


#异常类型的捕获
# try:
#     print("正在运行程序")
#     a=1/0 #不会执行，会直接执行except 语句
#     print(f"计算结果：{a}")
# except ZeroDivisionError:
#     print("我知道1不能/0，需要更改除数")
# print("剩下的程序")


#展示异常
# try:
#     print("正在运行程序")
#     a=1/0 #不会执行，会直接执行except 语句
#     print(f"计算结果：{a}")
# except ZeroDivisionError as err:
#     print(err)
# print("剩下的程序")




