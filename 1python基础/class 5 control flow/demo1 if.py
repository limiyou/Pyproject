"""""

测试登录用例
如果 用户名=‘米柚’：
   登录成功
如果 用户名=空：
   请输入用户名
否则：
   登录失败

if的写法：
if 条件表达式：
  （缩进）
   条件满足回执行的程序
   多行程序
条件表达式：要得到的值值一个布尔类型，有一个条件True,False
如果条件成立，子代码执行，如果不成立，后面的子代码不成立

if 条件表达式：
   子代码
else:
  子代码  表示 上面 if的条件都不成立时，需要执行的代码


if(条件表达式)：
  pass
elif(条件表达式)：
  pass
elif(条件表达式)：
  pass
else:
  pass
在同一个 if...elif...else条件中，只要执行了其中的一个分支，其他的分支就不会再执行了
"""
#if
# username="abc"
# if username=="miyou":
   #缩进表示条件满足以后需要执行的子代码，是一个分支
#   print("登录成功")
# print("条件之后")

#if...else
# username="abc"
# if username=="miyou":
#     print("登录成功")
# else:
#     print("登录失败")
# print("条件之后")


#if ...elif... else....

# username="demons"
# if username=="miyou":
#     print("登录成功")
# elif username==" ":
#     print("请输入用户名")
# elif username=="demons":
#     print("没有该用户")
# else:
#     print("登录失败")
# print("条件之后")

#TODO:只要执行了其中的一个分支，其他的分支就不会再执行了
#TODO:但是如果是不同的if if...elif..if...elif
#TODO:else是可以省略的
username="demons"
# if username=="miyou" or username=="demons":
#     print("登录成功")
# elif username==" ":
#     print("请输入用户名")
# elif username=="demons":
#     print("没有该用户")
# else:
#     print("登录失败")
# print("条件之后")


#不是同一个if语句，
if username=="miyou" or username=="demons":
    print("登录成功")
elif username==" ":
    print("请输入用户名")#
#else是可以省略的
# else:
#     pass
#第二个条件，与上边的if 没有关系
if username=="demons":
    print("没有该用户")
else:
    print("登录失败")
print("条件之后")