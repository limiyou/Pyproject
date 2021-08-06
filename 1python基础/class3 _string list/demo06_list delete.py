"""

列表的删除
-remove
-delete
-pop
"""
#remove：在列表当中删除指定的值
big_boss=['树',"君君","木易"]
big_boss.remove("木易")
big_boss.append("木易")
print(big_boss)

#delete：异类：尽量不要用

del big_boss[0]
print(big_boss)
#pop:操作，0代表 索引为0的值
big_boss.pop(0) #删除索引为0的值
big_boss[0]#获取索引为0的值
print(big_boss)