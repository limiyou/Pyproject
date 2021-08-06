"""
集合：
{}
集合当中的元素不能重复
"""
s={1,2,3}
print(s)
s={1,2,3,1,2,4,4,5}
print(s)

#使用列表存储用例
money=[1,5,100,0,1,100]
print(money)
print(len(money))
#转化成集合
money_after=list(set(money))
print(money_after)
print(len(money_after))


