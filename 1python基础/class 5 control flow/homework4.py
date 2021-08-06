"""使用for打印九九乘法表

提示：

输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）

1 * 1 = 1  1 * 2 = 2 2 * 2 = 4  1 * 3 = 3 2 * 3 = 6  3 * 3 = 9
 1 * 4 = 4 2 * 4 = 8 3 * 4 = 12 4 * 4 = 16  1 * 5 = 5 2 * 5 = 10 3 * 5 = 15 4 * 5 = 20
 5 * 5 = 25  1 * 6 = 6 2 * 6 =12

"""
#看到数据，有行有列的，一般都有2个for循环
list=[1,2,3,4,5,6,7,8,9]
for i in list:
    for j in list:
        #判断，如果j 比i 小,就打印
        if i>=j:
          print(f"{j}*{i}={i*j}",end="\t")
    print()


list1=[1,2,3,4,5,6,7,8,9]
for i in list:
    for j in list:
        if i>=j:
            print(f"{j}*{i}={i*j}",end="\t")
    print()