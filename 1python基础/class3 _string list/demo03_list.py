"""
list 列表
数据类型：可以存储多个数据的的数据类型
列表的表示：
--[]表示列表,前边没有东西，只有一个变量，a=[]
--区别：mstr[]获取切片
--列表当中每个元素可以是python的任意数据类型

索引：获取某一个元素

切片：获取多个元素
"""
# 元素可以是任意数据类型
big_boss=['demods','go','ee','上善若水','Summer']
big_boss=['demods',11,True,33.33,['a','b',['yuze',True]]]
print (big_boss)

#索引：  获取索引为0的元素
print(big_boss[0])
print(big_boss[-1])
print(big_boss[-2]) # 33.33
#切片：
print(big_boss[:-3])  # ['demods',11,True]
#获取a
print(big_boss[-1][0])
#== last_one=big_boss[-1]
#print(last_one[0])

#获取yuze
print(big_boss[-1][2][0])