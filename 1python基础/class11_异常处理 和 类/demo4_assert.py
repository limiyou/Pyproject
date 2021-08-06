"""断言 assert
我断言：xx跑步比刘翔快  False
断言的作用：判断真假
断言的时候：如果断言成功，程序继续执行
如果断言失败，程序终止进行，断言失败会触发一个异常类型：AssertionError
断言：预期结果和实际结果的比对
"""
miyou_height=int(input("米柚的身高： "))
assert miyou_height>100
print("断言有结果")