"""def bubble_sort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        for j in range(0, n - 1-i):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr=[2, 0, 7, 4,8,5,9]
bubble_sort(arr)

print(arr) """


""" 利用for循环，
完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法 """


a=[1,7,4,89,34,2]
for i in range(0,len(a)):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
           a[j],a[j+1]=a[j+1] ,a[j]
print(a)




