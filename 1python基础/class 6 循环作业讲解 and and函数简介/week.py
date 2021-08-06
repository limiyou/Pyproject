week=["周一","周二","周三","周四","周五","周末"]
while True:
    inputnum = int(input("请输入数字"))
    num = inputnum
    if num >0 and num<=5:
        print(f"数字{num}对应的星期为{week[num-1]}")
    elif num==6 or num==7:
        print(f"您输入的数字{num}对应的星期为：周末")
    else:
        print("输入的数字有误")

