
#定义函数的时候，return
# TODO:只要调用了函数，就要用参数去接收，参数的值是由函数定义的时候 return 决定的



li1=[1,4,6,7]
#append  没有返回值

res=li1.append(10)
print(res) #None

#remove 没有返回值
res1=li1.remove(4)
print(res1)  #None


#pop 有返回值 ，即要删除的索引的值

res2=li1.pop(0)
print(res2) #1


