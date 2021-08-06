"""
3.求三个整数中的最大值

提示：定义 3 个变量

"""
# a=89
# b=4
# c=99
# if a>b and a>c:
#  print("a是最大值")
# elif b>c:
#     print("b是最大值")
# else:
#     print("c是最大值")
#TODO：写完一个if分支，要习惯写else，如果else不执行任何代码，再把它去掉
#老师讲解：
#方法一：
a=88
b=99
c=33
#
#方法二：
#如果有50个数，怎么比较
max_mun=a
for num in[a,b,c]:
    if max_mun<num:
        max_mun=num
print(max_mun)

#方法三
nums=[a,b,c]
nums.sort()
print(nums[-1])

nums=[c,a,b]
nums.reverse()
print(nums[0])
