"""
for嵌套
先执行完内层for循环，再执行外层

"""
# a=[["s",'b','c',],(1,2,3)]
# for i in a:
#     #print (i)
#     for j in i:
#         print(j)



li=[1,2,3,4,5,6,7,8,9]
for i in li:
    for j in li:
        #print(i *j )
        #print(f"{i}*{j}={i*j}")
        print(f"{i}*{j}={i*j}",end='\t')