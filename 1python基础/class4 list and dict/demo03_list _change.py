"""

列表的修改：

"""
#单个修改
lst=[1,3,3,4] #修改索引为2的值为a
lst[2]='a'
lst[3]='miyou'
print(lst)
#多个修改
lst[1],lst[2]='c',"d"
print(lst)

#多个修改
lst[1:3]=5,6
lst[1:3]=99,'xiaohong'
print(lst)