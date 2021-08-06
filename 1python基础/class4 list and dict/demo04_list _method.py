"""
列表的方法
-index  获取列表值
-count  计数
-sort  排序
-reverse
-clear
"""
lst=[1,2,3,5,3]
print(lst.index(3)) #查找第一次出现的索引值
print(lst.count(3))
#排序(正向)
#lst.sort()
#print(lst)
#逆序,反向倒序
#lst.reverse()
#print(lst)
#反向排序,相当于：[::-1]
lst.sort(reverse=True)
print(lst)


#清除列表：clear （）
lst.clear()
print(lst)