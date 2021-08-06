
"""
一、单元测试框架unittest的架构

1、TestCase:一个testcase的实例就是一个测试用例
2、TestSuite：多个测试用例集合在一起
3、TestLoader:用来加载TestCase到TestSuite中
4、TextTestRunner:用来执行测试用例的
5、fixture：包含setUp和tearDown,分别用于创建测试环境（前置条件）和销毁测试环境

二、使用unittest做单元测试的步骤：
导入unittest模块
导入被测对象 login_check
创建一个测试类，并继承unittest.TestCase
重写setUp和tearDown方法（如果有前置条件或者结束条件）
  def setUp(self)->None:
     print("执行每条测试用例前需执行")
以函数的形式写测试项：函数名以test开头
使用unittest.main（）运行测试用例（运行所有以test_开头的方法）

三、常用断言函数的说明：
assertEqual(self,fiest,secind,msg=None),如果两个对象不相等，msg可以用来指定信息

四、常用函数说明：
unittest.TestSuite()创建suite对象
unittest.TestLoader()创建用例加载器
unittest.TestSuite().addTest()向suite中添加用例
unittest.TextTestRunner()创建用例运行器
unittest.TextTestRunner().run(suite)使用用例运行器运行suite


五、如何生成测试报告
"""

import unittest
from unittest import TestCase
from autoTest.day1.user.login import login_check


class LoginTestCase(unittest.TestCase):
    def test_login_sucess(self):
        """正确的用户名、密码，返回值是{"code":1,"msg":"登录成功"}"""
        data = {"username": 'lemon', 'password': '123456'}
        expected = {"code": 1, "msg": "登录成功"}
        act=login_check(**data)
        self.assertEqual(expected, act)

    def test_username_error(self):
        """错误的用户名，返回值是：{"code":0,"msg":"账号或密码不正确"}"""
        expected={"code":0,"msg":"账号或密码不正确"}
        act=login_check("lemo12","123456")
        self.assertEqual(expected,act)

    def test_password_error(self):
        """错误的密码，返回值是：{"code":0,"msg":"账号或密码不正确"}"""
        expected={"code":0,"msg":"账号或密码不正确"}
        act=login_check("lemon","123456789")
        self.assertEqual(expected,act)

    def test_username_password_error(self):
        expected={"code":0,"msg":"账号或密码不正确"}
        act=login_check("lemon123","1234567890")
        self.assertEqual(expected,act)

    def test_username_is_empty(self):
        expected={"code":0,"msg":"所有的参数不能为空"}
        act=login_check("","123456")
        self.assertEqual(expected,act)

if __name__ == '__main__':
    unittest.main() #函数的运行顺序，按字母开头排序执行



