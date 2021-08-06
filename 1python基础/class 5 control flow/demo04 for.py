"""
for

"""
cases=[{"username":"miyou","pswd":""},
       {"username":"xianrenqiu","pswd":"123456"},
       {"username":"","pswd":""},

]
#把cases 当中的每个元素都执行一遍
#把值{"username":"miyou","pswd":""}赋给case
#case是个变量
for case in cases:
    case=cases[0]
    print(case)
    print("正在执行用例")

#当for循环执行完一个子循环后，索引index+=1

#debug
  #暂停代码的运行去获取现在的数据状态
  #打断点，告诉程序应该在哪里暂停
