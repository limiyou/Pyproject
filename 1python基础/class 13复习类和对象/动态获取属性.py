class Mobile:
    def __init__(self,brand,model):
        #先天初始化过程当中形成的属性
        self.brand=brand
        self.color=model
    def __call__(self):
        print("正在打电话")

iPhone=Mobile('apple','xr')
#获取属性
print(iPhone.brand)
#修改属性
iPhone.brand='aple'

#定义新的实例属性
#后天养成的
# iPhone.video='美颜'
# print(iPhone.video)

#获取不存在的属性，会报错
# print(iPhone.games) #会报错

#动态获取属性
#getattr 内置函数
#default，如果获取不到属性名，传入default默认值，就不会报错了
#getattr不会修改原来的对象的属性
print(getattr(iPhone,"games",'吃鸡'))
# print(iPhone.games)

#修改动态属性
setattr(iPhone,'games','吃鸡')
print(iPhone.games)
setattr(iPhone,'games',"开心消消乐")
print(iPhone.games)