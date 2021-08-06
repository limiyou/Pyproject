"""
字符串的切片：slice 如何获取多个字符

索引获取的公式：
   m_str[start:end:step]
end:不包含该数字，应取到该数字-1
"""
name="limiyou"
#要第一个和第二个字符
#取头不取尾
print(name[0:2])#li
print(name[3:6])#iyo
print(name[2:4])# mi
#step：步长，应该取完第一个索引，把索引加多少再去取后面的索引
 #step=2
print(name[3:6:2])  # io
print(name[1:5:3])#iy
print(name[5:1:-3])#ym
#end减去start的符号 必须和step的符号相同才可以获取到索引
print(name[1:4:-2])#None
#step不能为0

name1='limiyoumeinv'
#省略end,取到最后
print(name1[2: ])
#TODO:IndexError
#print(name(1000000))
#省略start
print(name1[: 7])
#复制.copy
#TODO:面试题，复制
print (name[:])
name_copy=name[:]
print(name_copy)

#"123456'==>'654321'倒叙排列
#TODO:面试题，倒叙字符串
print(name[::-1])