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


def recharge(amount):
    url = 'http://api.lemonban.com/futureloan/member/recharge'
    # 只有登录后，才能获得id和token
    # 不带token，服务器报 未授权或token已过期 错误。  token：令牌
    resp = login()
    token = jsonpath.jsonpath(resp.json(), '$..token')[0]  # 获取登录后的token值
    print(token)
    id = jsonpath.jsonpath(resp.json(), '$..id')[0]  # 获取id
    print(id)
    headers = {
        'X-Lemonban-Media-Type': 'lemonban.v2',
        'Authorization':'Bearer' + ' ' +token  # 格式是HTTP协议中规定的格式
    }
    data = {
        'member_id': id,
        'amount': amount
    }
    response = request('post', url=url, json=data, headers=headers)
    return response

if __name__ == '__main__':
    # resp = login()
    # id = jsonpath.jsonpath(resp.json(),'$..id')[0]  # 获取id
    # token = jsonpath.jsonpath(resp.json(),'$..token')[0]  # 获取登录后的token值
    # print(id)
    # print(token)
    resp = recharge(120000)
    print(resp.json())


