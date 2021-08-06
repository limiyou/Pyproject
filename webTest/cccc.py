


# a=[1,7,4,88,78,90,65]
# for i in range(len(a)):
#     for j in range(0,len(a)-1-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#
# print(a)
#
#
# b=[1,9,77,6,34,56,6,86,3,98]
# n=len(b)
# for i in range(n):
#     for j in range(0,n-1-i):
#         if b[j]>b[j+1]:
#             b[j],b[j+1]=b[j+1],b[j]
# print(b)


# for i in range(1,10):
#     #print(i)
#     for j in range(1,i+1):
#         print(j)
#         #print('{} x {}\t'.format(j,i,i*j),end='')
    #print()
for i in range(1,10):
    for j in range(1,i+1):
        print("{} x {}\t".format(j,i,i*j),end='')
    print()