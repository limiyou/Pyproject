

"""
属性和方法
属性是指类或对象的特征
方法是指类或对象的行为
属性：
    类属性（类变量）：类当中每一个成员都具备的特征
        类和对象都可以获取
    实例属性（实例变量）/对象属性:类当中的成员不一定都具备的特征，是某个对象单独持有的，其他对象没有的
方法：
    类方法：每一个成员或者整个类都能执行的行为
    实例方法/对象方法  ：需要一个单独的成员调用的行为，不能是整个类调用
    #TODO:不要用整个类去调用实例方法
    实例方法在定义的时候，自带一个参数，self
    todo:但是实例方法在调用的时候不需要传self参数的实际参数
    object.实例方法（）
"""

# class Dog:
#     #类属性
#     tailed =True
#
#     #实例方法
#     def say(self):
#         print("汪汪队")
# #对象
# teddy=Dog
# #类属性的获取
# print(Dog.tailed)
#
# #对象属性的获取
# print(teddy.tailed)
#
# #属性可以后天修改
# Dog.tailed=False
# print(Dog.tailed)
# print(teddy.tailed)
#
# teddy.tailed="有时候有尾巴，有时候没尾巴"
# print(Dog.tailed)
# print(teddy.tailed)
#
#
# #类方法的调用
#
# teddy.say('abc')





# class Animal():
#     tail=True
#     def speak(self):
#         print('i can speak animal language')
# Cat= Animal()
# print(Cat.tail)
# print(Animal.tail)
# Cat.tail="long"
# Animal.tail='short'
# print(Cat.tail)
# print(Animal.tail)



class Animal1():
    eyes="big"
#实例方法
    def speak(self):
        print("i can speak animal language")
Sheep=Animal1()
print(Sheep.eyes)
print(Animal1.eyes)
Sheep.eyes='small'
Animal1.eyes='long'
print(Sheep.eyes)
print(Animal1.eyes)

#类方法的调用
Sheep.speak()