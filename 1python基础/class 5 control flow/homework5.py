"""
你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=

['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']

当中, 请依次把这 5 个人分别从 black_list 当中删除，最后 black_list 为空。（不要使用 clear）
"""
black_list=["卖茶叶","买面膜","卖保险","卖花生","卖手机"]
# for i in range(len(black_list)):
#     black_list.pop(0)
# print(black_list)
#     #print(i)
lenth=0
while lenth<len(black_list):
    black_list.pop(0)
print(black_list)