#TODO:字典 拆包，拆成 关键字参数

#列表拆包
# def marry(male,female):
#     print(male)
#     print(female)
# couple=["小王","老刘"]
# marry(*couple)

# 字典拆包
def marry(male,female):
    print(male)
    print(female)
couple={"male":"小王","female":"老刘"}
marry(**couple)  #==marry(male="小王",female="老刘")
