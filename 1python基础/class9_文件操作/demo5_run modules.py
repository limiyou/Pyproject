"""
在这个模块里使用其他模块的内容
使用其他模块的代码 需要先声明，import

import 模块名
from 路径 import 模块名/函数名/类/变量
from 路径 从项目根路径开始
"""

from class9_文件操作.pac.offers import get_offer
#from class9_文件操作.pac.offers import get_food
from class9_文件操作.pac.food import get_food
get_offer("Lijing",20)
get_food("米柚"," pure milk")
#get_food("Miyou","辣条")



#也可直接使用import +模块
#但是import ...只能跟到模块，不能到函数、类、变量
#TODO：导入自己的模块以及比人的第三方模块，一般使用 from...import...,不用import
import class9_文件操作.pac.offers
class9_文件操作.pac.offers.get_offer("李米柚",20)

#TODO：from ...import...只导入到模块，不导入函数
#google,导入模块只导入到模块这一层，不导入具体的类，函数，变量
from class9_文件操作.pac import offers
from class9_文件操作.pac import  food
offers.get_offer("李红朋",30)
food.get_food("李米柚","milk")


#TODO：除啦导入到模块，也可使用 as 关键字 对函数当中的函数、类、变量名进行重命名
#原函数很长的时候，也可以重命名  as  find_element_by_userid as  find

from class9_文件操作.pac .offers import get_offer as new_offer
def get_offfer():
    print("假的")
new_offer("xiaoong",30)
get_offfer()




#TODO：from ....import*导入所有的方法、类、变量，自己写的代码，不要用这个方式

