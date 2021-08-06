def login_check(username=None,password=None):
    """
    登录校验
    :param username: 账号
    :param password: 密码
    :return: 字典烈性的提示信息
    """
    # 如果用户名或密码错误，提示：{"code":0,"msg":"账号或密码不正确"}
    if username != 'lemon' or password != '123456':
        return {"code": 0, "msg": "账号或密码不正确"}
    # 用户名或密码为空，返回{"code":0,"msg":"所有的参数不能为空"}
    if not username or not password:
        return {"code": 0, "msg": "所有的参数不能为空"}
    # 用户名和密码正确，返回 {"code":1,"msg":"登录成功"}
    if username == "lemon" and password == "123456":
        return {"code": 1, "msg": "登录成功"}
    return {"code": 1, "msg": "未知错误，请联系管理员"}

if __name__ == '__main__':

    result = login_check('python32', '1234567')
    print(result)