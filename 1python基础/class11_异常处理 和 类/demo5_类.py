"""
类：所有符合某种特征的个体的集合 class
对象：某个类当中的一个成员，一个个体 object

类的表示：
class 类名称：
     #类当中的内容
     属性==》特征
     行为
类的命名： 标识符、字母数字下划线 有意义 规范：大驼峰式 SingleDog
  #对象是从类当中产生的
"""

# class Dog:
#     #类内容
#     tailed =True
#     def say(self):
#         print("汪汪队")
#     pass
# #类==》函数的定义
# #对象==》函数的调用
# #TODO:得到对象的时候，一定要+ （）
# zhonghua=Dog() #对象
# print(zhonghua)
# print(Dog)
#
# zhonghua=Dog #类
# print(zhonghua)



class Animal:
     eyes=True
     def say(self):
         print("动物都会叫")
Cat=Animal()
Cat.eyes=False
print(Cat.eyes)