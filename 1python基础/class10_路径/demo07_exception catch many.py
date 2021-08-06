
"""
多异常类型的捕获
"""
# TODO:一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
#  处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
#  一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
#方式一，有多个异常时，只会捕捉第一个异常
# try:
#     print("正在运行程序")
#     {'name':'miyou'}['age']
#     a=1/0 #不会执行，会直接执行except 语句
#     lst=['miyou','xiaohong']
#     lst[3]
#     print(f"计算结果：{a}")
#
# except (KeyError,ZeroDivisionError,IndexError )as err:
#     print(err)
#     print("hello world")


#方式二
# try:
#     a = 1 / 0
#     lst = ['miyou', 'xiaohong']
#     lst[3]
#     {'name': 'miyou'}['age']
#
# except ZeroDivisionError as err1:
#     print(err1)
#
# except IndexError as err2:
#     print(err2)
#
# except ValueError as err3:
#     print(err3)



# try:
#     1/0
#     lst=['miyou','anna']
#     lst[3]
# except Exception as err4:
#      print(err4)
#

# while True:
#     try:
#         x=int(input("please input a number:"))
#         break
#     except ValueError:
#         print("您输入的不是数字，please try again！")
# print(x)

import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()