
import  random
class User():
    def __init__(self):
        self.age=random.randint(0,99)

u1=User()
u2=User
print(u1,u2)

users=[User(),User(),User()]
#取出所有的age
li=[]
for user in users:
    li.append((user.age))

print(li)
    