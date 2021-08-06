"""、有下面几个数据 ，



某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄

b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；

c, 平台为了保护你的隐私，需要你删除你的联系方式；


d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。

e, 你进一步添加自己的兴趣，至少需要 3 项。


"""

dict={"name":"anna","gender":"female", "age": 18}
#有一个人对你很感兴趣，平台需要您补足您的身高和联系方式
dict["height"]="160cm",
dict["contact"]='15711375237'
print(dict)

#平台为了保护你的隐私，需要你删除你的联系方式；
dict.pop("contact")
print(dict)
# 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。

dict["nickname"]='xiaomiyou'
dict["height"]="190cm"
dict["age"]=16
print(dict)

#e, 你进一步添加自己的兴趣，至少需要 3 项。
dict["sport"]="basketball"
dict['sing']="love you"
dict['satr']="李宇春"

print(dict)