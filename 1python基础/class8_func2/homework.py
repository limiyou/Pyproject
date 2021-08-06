"""1、通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，
 选择之后返回对应操作的值"""


def caculator(x,y,method):
    if method==1:
        return  x+y
    elif method==2:
        return x-y
    elif method==3:
        return x*y
    elif method==4:
        return x/y
print(caculator(1,2,4))









# 2、一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，询问用户的性别和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。

def join_team(gender,age):
    for i in range(1,11):
       if gender=="女" and age>=15 and age<=22:
           return True
       else:
           return  False
def main():
    num=0
    for i in range(10):
        age=input("请输入年龄：")
        gender=("请输入性别：")
        if not age.isdigit():
            print("输入不合法")
            continue
        joined=join_team(int(age),gender)
        if joined:
            num+=1
    print(num)





"""
3、数据转换

# 有一组用例数据如下：
cases = [
['case_id', 'case_title', 'url', 'data', 'excepted'],
[1, '用例1', 'www.baudi.com', '001', 'ok'],
[4, '用例4', 'www.baudi.com', '002', 'ok'],
[2, '用例2', 'www.baudi.com', '002', 'ok'],
[3, '用例3', 'www.baudi.com', '002', 'ok'],
[5, '用例5', 'www.baudi.com', '002', 'ok'],
]


#要求一：把上述数据转换为以下格式
res1 = [
{'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
{'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
{'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
{'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
{'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
#要求二：把上面转换好的数据中case_id大于3的用例数据获取出来,得到如下结果
res = [
{'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
{'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]

"""

def transform_zip(cases):
    if type(cases)!=list:
        print("不是list")
        return
    new_cases=[]
    title=cases[0]
    for i  in cases[1:]:
        new_dict=dict(zip(title,i))
        new_cases.append(new_dict)
    print(new_cases)
    return new_cases
cases = [
['case_id', 'case_title', 'url', 'data', 'excepted'],
[1, '用例1', 'www.baudi.com', '001', 'ok'],
[4, '用例4', 'www.baudi.com', '002', 'ok'],
[2, '用例2', 'www.baudi.com', '002', 'ok'],
[3, '用例3', 'www.baudi.com', '002', 'ok'],
[5, '用例5', 'www.baudi.com', '002', 'ok'],]
transform_zip(cases)



def filter(cases,id):

    new_cases1=[]
    for c in cases:
        if int(c['cases_id'])>id:
            new_cases1.append(c)
    print(new_cases1)
    return new_cases1
cases = [
['case_id', 'case_title', 'url', 'data', 'excepted'],
[1, '用例1', 'www.baudi.com', '001', 'ok'],
[4, '用例4', 'www.baudi.com', '002', 'ok'],
[2, '用例2', 'www.baudi.com', '002', 'ok'],
[3, '用例3', 'www.baudi.com', '002', 'ok'],
[5, '用例5', 'www.baudi.com', '002', 'ok'],]
filter(cases,5)