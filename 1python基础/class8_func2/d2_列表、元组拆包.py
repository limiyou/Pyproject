"""
拆包

"""
#列表 和 元组拆包：拆成位置参数
"""def marry(male, female):
    print(male)
    print(female)
#marry("老王","小星星")

couple=("老王","小星星")
#couple=["老王","小星星"]

#函数定义当中，*args表示不定长的位置参数
#TODO:在调用的时候，把一个列表后者元素变量传入函数，在前面 加 *，就可以变成多个值

marry(*couple)

"""


def marry(male, *female):
    print(male)
    print(female)
#marry("老王","小星星")

couple=("老王","小星星","第三者")
#couple=["老王","小星星"]

#函数定义当中，*args表示不定长的位置参数
#TODO:在调用的时候，把一个列表后者元素变量传入函数，在前面 加 *，就可以变成多个值

marry(*couple)