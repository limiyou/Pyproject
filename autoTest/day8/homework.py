import jsonpath
from requests import request


def login():
    url = 'http://api.lemonban.com/futureloan/member/login'
    data = {
        'mobile_phone': '17801234567',
        'pwd': '12345678'
    }
    headers = {
        'X-Lemonban-Media-Type': 'lemonban.v2'
    }
    response = request('post', url=url, json=data,headers=headers)
    return response
def withdraw(amount):

    resp=login()
    id=jsonpath.jsonpath(resp.json(),"$..id")[0]
    token=jsonpath.jsonpath(resp.json(),'$..token')[0]
    url='http://api.lemonban.com/futureloan/member/withdraw'
    headers = {
        'X-Lemonban-Media-Type': 'lemonban.v2',
        'Authorization': 'Bearer' + ' ' + token  # 格式是HTTP协议中规定的格式
    }
    data = {
        'member_id': id,
        'amount': amount
    }
    response=request('post',url=url,json=data,headers=headers)
    return response
if __name__ == '__main__':
    money_resp=withdraw(50)
    print(money_resp.json())