"""

字典
"""

beisheng={"favor":"星际穿越",
          "hate":"蜘蛛侠",
          "first":"上海堡垒",
          "last":"分手大师",
          "twice":"前任3"}
#获取，查
print(beisheng["hate"])
#字典没有索引和切片

#修改
beisheng["hate"]="蝙蝠侠" #将原来的蜘蛛侠 改为 蝙蝠侠
print(beisheng)

#添加:与修改的语法一致
  #当key已经存在时，为修改，当之前没有这个key,就是添加
beisheng["scared"]="贞子"
print(beisheng)

#字典删除  pop
#列表的删除：remove pop
beisheng.pop("scared")
print(beisheng)

#查
print(beisheng.keys()) #打印所有的key
print(beisheng.values()) #打印所有的value
print(beisheng.items())  #获取所有的键值对