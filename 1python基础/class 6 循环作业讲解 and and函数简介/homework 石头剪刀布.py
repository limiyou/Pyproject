"""
提示：电脑随机出拳

使用随机数，首先需要导入随机数的模块 —— “工具包”

import random

导入模块后，可以直接在 模块名称 后面敲一个"."然后按 Tab键，会提示该模块中包含的所有函数

random.randint(a, b)，返回[a, b]之间的整数，包含a和b

random.randint(1,10) # 生成的随机数n: 1 <= n <= 10
random.randint(4,4) # 结果永远是 4
random.randint(25,12) # 该语句是错误的，下限必须小于上限
"""
while True:
 import random
 choice=input("请输入猜拳： 石头 （1）/剪刀（2）/布（3）/退出（4）")
 if choice==4:
    print("退出游戏")
     #break
 computer_choice=random.randint(1,3)
 if (computer_choice==1 and choice=='3') or (
    computer_choice==2 and choice=="1") or(
    computer_choice==3 and choice=='2'):
    print("我很厉害哦，我赢了！")
 elif str(computer_choice)==choice:
    print("平局")
 else:
    print("失败")