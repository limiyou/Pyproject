#1. 异常捕获的语法是什么样的？ 请列举你会的错误类型。
KeyError
IndexError
IOError
SyntaxError
ZeroDivisionError

#2输入用户的体重身高，计算 bmi, (考虑异常情况）

# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 : 65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
# 低于18.5： 过轻，18.5-25：正常，25-28：过重，28-32：肥胖，高于32：严重肥胖

# def get_BMI(weight,height):
#     BMI=weight/height**2
#     if BMI <=18.5:
#         return '过轻'
#     elif BMI>18.8 and BMI<=25:
#         return '正常'
#     elif BMI>25 and BMI<=28:
#         return '过重'
#     elif BMI>28 and BMI<=32:
#         return '肥胖'
#     else:
#         return '严重太胖'
# a=height=input("请输入身高")
# b=weight=input("请输入体重")
# print(get_BMI(a,b))
# try:
#     print(get_BMI(weight,height))
# except TypeError:
#     print("请输入两个数字类型")
# except ZeroDivisionError:
#     print("height 不能为0")









# 优化去生鲜超市买橘子程序
#
# a.收银员输入橘子的价格，单位：元／斤
#
# b.收银员输入用户购买橘子的重量，单位：斤
#
# c.计算并且 输出 付款金额
#
#
# d.使用捕获异常的方式，来处理用户输入无效数据的情况

price = (input("请输入橘子的价格:"))
weight = (input("请输入用户购买橘子的重量:"))
try:
    price=float(price)
    weight=float(weight)
except Exception as error:
    print("您输入的{a}橘子价格不是数字,请重新输入")
    print("您输入的{b}橘子的重量不是数字，请重新输入")
if price>-0 and weight>0:
    print(price*weight)
  




