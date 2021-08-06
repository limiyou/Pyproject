
#self,是在类里面，类当中表示对象本身，我自己
#类外面：用实例
class Dog():
    def __init__(self,name,color):
        self.name=name
        self.color=color
        print(self)
    def say(self):
        print("汪汪")
teddy=Dog("taidi",'yellow')
tianyuan=Dog("田园犬",'black')
print(teddy.color)
print(teddy)
print(tianyuan)
