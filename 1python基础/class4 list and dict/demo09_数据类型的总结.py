"""数据类型
-string
-int
-float
-bool
-list
-dict
-tuple
-set
-None 什么都没有
"""

#bool
#只要是代表0 空 就是False,否则就是true





a='4',
b=bool(a)  #True
b=bool([1]) #True
b=bool({"name":"anna"}) #True
b=bool(7)  #True
print(b)

#False
#对数字进行bool转换，非0为True，0 为False
f=bool(0) #True
f=bool(-1000) #True
print(f)


#字符串 空字符串为False
f=bool("") #False
f=bool(" ") #空格为True

print(f)
