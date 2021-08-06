#函数调用

'''def get_offer(name,money,food=None):
    print(f"{name}获得了一个{money}k的offer")
    # 吃最喜欢的食物
    eat("芒果")

def eat(food):
     print(f"这个人正在猛吃{food}")
#get_offer函数当中调用了另外的一个函数 eat
get_offer("米柚",30,"辣条")

'''
#
def get_offer(name,money,food=None):
    print(f"{name}获得了一个{money}k的offer")
    # 吃最喜欢的食物
    eat("芒果")  #会报错，eat在调用的时候还没有被读到

#get_offer函数当中调用了另外的一个函数 eat
get_offer("米柚",30,"辣条")

def eat(food):
    print(f"这个人正在猛吃{food}")



#todo:python 如何运行代码
#todo:函数调用是去执行函数体内部的逻辑