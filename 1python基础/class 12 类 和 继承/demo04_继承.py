"""
继承：
子类（父类）:

#方法的重写：如果子类有一个方法，就不会去使用父类的同名方法
"""
class Mobile():
    def __init__(self,brand,model,color='blcak'):
        self.color="black"
        self.model=model
        self.brand=brand

    def call(self):
        print(f"{self}手机正在打电话")

class SmartPhone(Mobile):
    def __init__(self,model,color='red'):
        self.color=color
        self.model=model

    def play_game(self,name):
        print(f"{name}在玩游戏")

# iphone=SmartPhone('iphone12','apple')
# iphone.play_game("小红")
#重写父类方法
smart=SmartPhone('huawei','yellow')
print(smart.model)
print(smart.color)
