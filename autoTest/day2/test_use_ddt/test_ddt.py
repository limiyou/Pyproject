import unittest

from BeautifulReport import BeautifulReport

from autoTest.day2.last_homework.reigster import register
from autoTest.day2.test_use_ddt.test_register import RegisterTestCase

cases=[
    {
        "name":'register_success',
        "expected": {"code":1,"msg":"注册成功"},
        'actual_args':{'username':"python14",'password1':'123456','password2':'123456'}

    },
    {
        "name": 'register_username_exists',
        "expected": {"code": 0, "msg": "该账户已存在"},
        'actual_args': {'username': "lemontree", 'password1': '123456789', 'password2': '123456789'}

    },
    {
        "name": 'register_pswd1_not_equal_pswd2',
        "expected": {"code": 0, "msg": "两次密码不一致"},
        'actual_args': {'username': "python15", 'password1': '12345678', 'password2': '1234567'}

    },
    {
        "name": 'register_user_empty',
        "expected": {"code": 0, "msg": "所有参数不能为空"},
        'actual_args': {'username': "", 'password1': '123456', 'password2': '123456'}

    },
    {
        "name": 'register_pswd1andpwsd2_empty',
        "expected": {"code": 0, "msg": "所有参数不能为空"},
        'actual_args': {'username': "python15", 'password1': '', 'password2': ''}

    },
    {
        "name": 'register_usernameandpswd1andpswd2_empty',
        "expected": {"code":0,"msg":"所有参数不能为空"},
        'actual_args': {'username': "", 'password1': '', 'password2': ''}

    },
    {
        "name": 'register_usrname_less6',
        "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"},
        'actual_args': {'username': "pyth", 'password1': '123456', 'password2': '123456'}

    },
    {
        "name": 'register_usrname_more18',
        "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"},
        'actual_args': {'username': "pyth11111111111111111111111", 'password1': '', 'password2': ''}

    },
    {
        "name": 'register_pswd1andpswd2_less6',
        "expected":{"code": 0, "msg": "账号和密码必须在6-18位之间"} ,
        'actual_args': {'username': "pyth", 'password1': '12345', 'password2': '12345'}

    },
    {
        "name": 'register_pswd1andpswd2_more18',
        "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"},
        'actual_args': {'username': "pyth11111", 'password1': '111111111111111111', 'password2': '111111111111111111'}

    },
    {
        "name": 'register_usernameandpswd_more18',
        "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"},
        'actual_args': {'username': "pyth1111111111111111111111111", 'password1': '111111111111111111', 'password2': '111111111111111111'}

    },
    {
        "name": 'register_usernameandpswd_less6',
        "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"},
        'actual_args': {'username': "pyth", 'password1': '1111', 'password2': '1111'}

    }
]

#RegisterTestCase是一个空类


#1.定义一个方法：构造一个通用的函数
def make_test_func(expected,**actual_args):
    """
    构造测试用例方法
    :param expected: 预期结果
    :param actual_args: 被测对象需要传递的参数
    :return: 一个函数
    """
    def test_(self):
        #参数化：把写死的值用变量代替
        self.assertEqual(expected,register(**actual_args))

    return test_
#2.遍历cases，通过步骤1定义的方法，生成len(cases)个 test_开头的方法，并把方法添加到
 #RegisterTestCase类中
for case in cases:
    name,expected,actual_args=case.values()
    # print(name,expected,actual_args)
    #动态地生成函数
    test_func=make_test_func(expected,**actual_args)
     # print(test_func)
    setattr(RegisterTestCase,"test{name}".format(name=name),test_func)
    # print(dir(RegisterTestCase))

    #3.运行测试用例，生成报告
    #3.1创建suite对象
suite=unittest.TestSuite()
#3.2创建加载器
loader=unittest.TestLoader()
#3.3往套件里添加测试用例
suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))
 #3.生成报告
br=BeautifulReport(suite)
#br.report("注册时自动化测试报告","myddt.html",report_dir='.')



