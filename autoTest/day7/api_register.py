'''演示注册接口的测试
需要：
1. 地址是啥？http://api.lemonban.com/futureloan/member/register
2. 请求方法是啥？POST
3. 需要传递什么参数  mobile_phone   pwd
4. 预期结果是啥？
'''
import requests
def test_user_is_register():
    url = 'http://api.lemonban.com/futureloan/member/register'
    data = {
        'mobile_phone': '16789012345',
        'pwd': '12345678'
    }
    # 请求头
    headers = {
        'X-Lemonban-Media-Type': 'lemonban.v2'
    }
    resp = requests.post(url=url, json=data, headers=headers)
    if resp.json()['msg'] == '账号已存在':
        print('测试通过')


def test_user_register_ok():
    """前提条件：17801234568未注册"""
    url = 'http://api.lemonban.com/futureloan/member/register'
    data = {
        'mobile_phone': '17801234561',
        'pwd': '12345678'
    }
    # 请求头
    headers = {
        'X-Lemonban-Media-Type': 'lemonban.v2'
    }
    resp = requests.post(url=url, json=data, headers=headers)
    if resp.json()['msg'] == 'OK':
        print('测试通过')


# 测试用例一：  用户名，密码合法，且用户为注册，预期结果是注册成功。
# 测试用例二：  用户名，密码合法，且用户已注册，预期结果是用户已存在。

if __name__ == '__main__':
    test_user_is_register()
    test_user_register_ok()