"""info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
1， 获取 [18, "男"]
2, 获取 “帅”
3， 获取“矮穷丑”的长度


"""

info =["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
#1 获取 [18, "男"]
print(info[1:3])
#2, 获取 “帅”
print(info[4][2])
#获取“矮穷丑”的长度
c=info[3]
print(len(c))
"""2，a = ["2020", "6", "5"], b = ["23", "4", 23"],

进行操作得到 “2020/6/5 23:4:23”"""
a = ['2020', '6', '5']
b = ['23','4','23"']
before="/".join(a)
after= ":".join(b)
print(before +" "+ after)
print(before)
print(after)



"""3, 总结本节知识点"""