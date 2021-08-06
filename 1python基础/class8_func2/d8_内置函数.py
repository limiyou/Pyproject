# max

#可以传多个值
max_num=max(1,3,68)
print(max_num)  #68

#也可以传列表
max_num1=max([1,4,7,8])
print(max_num1)

#sum 求和
sum_num=sum([4,7,8])
print(sum_num)

#eval，表示可以去掉字符串的引号，python可执行代码
m_str="6>7"
print(m_str)
print(eval(m_str))


m_str1='{"username":"miyou","age":1}'
print(type(m_str1))
print(eval(m_str1))


m_str2=('"limiyou ","i love you","hopelee"')
print(eval(m_str2))

#filter 过滤一个元组
  #先定义一个列表，
# li=[2,5,7,8,9,10,18]
# def get_odd(value):
#     if value %2==0:
#         return True
#     return False
# res=filter(get_odd,li)
# print(list(res))




#map 是对元组或者列表的每个元素进行操作
li1=[2,5,7,8,9,10,18]
li4=[1,2,3,45,6,7,8]
def sqare(value):
    return value **2
def add(value1,value2):
    return value1+value2
res3=map(add,li1,li4)
res1=map(sqare,li1)
print(list(res1))
print(list(res3))






#zip
li2=["miyou","hopelee","anna"]
li3=[1.5,28,28]
print(type(zip(li2,li3)))
print(list(zip(li2,li3)))
print(dict(zip(li2,li3)))  #压缩成字典

