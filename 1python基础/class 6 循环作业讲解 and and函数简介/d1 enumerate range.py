#同时打印列表的索引、值
#i 索引，value 值
list=["a","b","c"]
for i ,value in enumerate(list):
    print(i,value)

 #字典的循环
mdict={"name":"miyou","age":1}
#获取字典的键值对
for k,v in mdict.items():
    print(k,v)

for value in mdict.keys():
     print(value)
#range

for i in  range(1,101,2):
    print(i)
