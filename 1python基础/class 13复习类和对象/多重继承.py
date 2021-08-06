'''
多重继承：
一个类可以同时继承多个类

'''
class Phone():
    def call(self):
        print("正在打电话")

class video():
    def capture(self):
        print("正在录屏")
class SmartPhone(Phone,video):
    pass

iPhone=SmartPhone()

iPhone.call()
iPhone.capture()
print(SmartPhone.__mro__)#继承顺序