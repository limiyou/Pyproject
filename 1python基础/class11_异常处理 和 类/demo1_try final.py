try:
    1/1
    print("正常执行的代码")
except ZeroDivisionError as e:
    print("不能除以0")
finally:
    print("无论报错与否，都会继续执行的代码")


try:
    1/0
    print("正常执行的代码")
except ZeroDivisionError as e:
    print("不能除以0")
finally:
    print("无论报错与否，都会继续执行的代码")
  #else :正常执行的代码
try:
    1/0
    print("正常执行的代码")
except ZeroDivisionError as e:
    print("不能除以0")
else:
    print("无论报错与否，都会继续执行的代码")