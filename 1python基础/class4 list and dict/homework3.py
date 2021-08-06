"""2、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，

要求一：去除列表中的重复元素，

要求二：删除 77，88，99这三个元素



"""

li = [11,22,33,22,22,44,55,77,88,99,11]
li_after=list(set(li))
sorted(li_after)
print (sorted(li_after))
li_after.remove(77)
li_after.remove(88)
li_after.remove(99)
print (li_after)