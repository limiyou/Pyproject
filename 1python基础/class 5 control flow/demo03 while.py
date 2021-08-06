"""
while用的不是很多

"""

username=" "
# while username=="miyou":
#     print("hello world")
# print("finished")
while username!="miyou":
    print("hello world")
    #手动强制退出循环体
    break
print("finished")



# while username!="miyou":
#     print("hello world")
#     #进入下一个循环，continue后面的不再执行
#     continue
# print("finished")

#double king
# times=0
# while times<9:
#     print(f"我说了{times}次")
#     print("我喜欢小文！")
#     times=times+1
# print("有钱人终成眷属")


times=0
while times<9:
    print(f"我说了{times}次 我爱你")
    print("我说了{}次我爱你".format(times))
    print("我爱你")
    times+=1
print("有钱人终成眷属")