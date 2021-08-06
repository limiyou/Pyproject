"""
定义函数：将用户输入的所有数字相乘之后对20取余数

用户输入的数字个数不确定
"""
# def multiply_module(numbers):
#    start_number=1
#    for i in numbers:
#        start_number*=int(i)
#    module=start_number %20
#    return module
# input_numbers=   input("请输入所有的数字，以, 隔开：（4,5,6）")
# numbers=input_numbers.split(",")


"""编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
"""
def func(arr):
    a=len(arr)
    if a>2:
        print(arr[0:2])
    return (arr[0:2])

arr=[3,4,4,5,6]
arr=[4,6,7,"米柚"]
func(arr)



def func1(arr1):
    a=len(arr1)
    if a>2:
        print(arr1[0:2])
    return (arr1[0:2])
arr1=[5,6,7,8,9]
func1(arr1)





"""列表去重

定义一个函数 def remove_element(m_list):，将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
"""
# def remove_element(m_list):
#  new_m_list=[]
#  for i in m_list:
#     if i not in new_m_list:
#         new_m_list.append(i)
#  print(new_m_list)
#  return
# m_list= [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# remove_element(m_list)



def remove_element(m_list):
 for i in m_list:
   if i==i+1:
       m_list.pop(i+1)
 print(m_list)
 return
m_list= [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
remove_element(m_list)











"""
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 : 65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5：过轻；18.5-25： 正常； 25-28：过重；
28-32：肥胖；高于32：严重肥胖"""
# def  BMI(weight,height):
#     BMI=weight/height
#     if BMI<18.5:
#         print("过轻")
#     elif BMI>=18.5 and BMI <25:
#            print("正常")
#     elif BMI >=28 and BMI <32:
#                print("肥胖")
#     else:
#       print("严重肥胖")
#     return
# weight=float(input("请输入体重： "))
# height=float(input("请输入身高： "))
# BMI(weight,height)