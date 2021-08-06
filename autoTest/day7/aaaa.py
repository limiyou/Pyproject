import requests
def test_user_is_register():
    url= 'http://api.lemonban.com/futureloan/member/register'
    data = {
        'mobile_phone': '17801234000',
        'pwd': '12345678'
    }
    #请求头
    headers = {
        'X-Lemonban-Media-Type': 'lemonban.v2'
    }
    resp=requests.post(url=url,json=data,headers=headers)
    if resp.json()['msg']=='账号已存在':
        print("测试通过,账号已存在")
def test_user_register_ok():
    """前提条件：17801234568未注册"""
    url = 'http://api.lemonban.com/futureloan/member/register'
    data = {
        'mobile_phone': '17801235000',
        'pwd': '12345678'
    }
    # 请求头
    headers = {
        'X-Lemonban-Media-Type': 'lemonban.v2'
    }
    resp = requests.post(url=url, json=data, headers=headers)
    if resp.json()['msg'] == 'OK':
        print('测试通过，注册成功')
if __name__ == '__main__':
    test_user_is_register()
    test_user_register_ok()

