"""

列表和字符串：
列表有其他的操作：增、删、改、查

列表的添加操作：
  append 添加到列表的最后
  insert（索引）
  extend 添加多个元素

"""
# append 增加某个元素,修改的是原来的的变量lst
lst=['yuze',"miyou",'anna']
lst.append("裴纶") #在最后增加“裴纶”
print(lst) #改变列表，在最后 增加

#insert（索引，data）

lst.insert(2,"仙人球")
print(lst)

#添加多个元素,即合并两个列表，添加多个
lst.extend(["xiaomi",'honor'])
print(lst)

lst.append(['f2','hello'])
print(lst)
lst.extend(["f2",'hello'])
print(lst)