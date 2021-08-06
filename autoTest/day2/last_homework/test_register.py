import unittest

from BeautifulReport import BeautifulReport

from autoTest.day2.last_homework.reigster import register


class RegisterTestCase(unittest.TestCase):
    def test_register_success(self):
        """正确的用户名密码注册返回：{"code":1,"msg":"注册成功"}"""
        self.assertEqual({"code":1,"msg":"注册成功"},register("python14",'123456','123456'))
    def test_register_username_exists(self):
        """用户名已存在，返回：{"code": 0, "msg": "该账户已存在"}"""
        self.assertEqual({"code": 0, "msg": "该账户已存在"},register("lemontree",'123456789','123456789'),msg="实际结果与预期结果不符，测试用例执行失败")
    def test_register_pswd1_not_equal_pswd2(self):
        """密码输入不一致：{"code": 0, "msg": "两次密码不一致"}"""
        self.assertEqual({"code": 0, "msg": "两次密码不一致"},register("python15",'12345678','123456'))
    def test_register_user_empty(self):
        """用户名为空返回：{"code": 0, "msg": "所有参数不能为空"}"""
        self.assertEqual({"code": 0, "msg": "所有参数不能为空"},register("",'123456','123456'))
    def test_register_pswd1andpwsd2_empty(self):
        """密码为空返回：{"code": 0, "msg": "所有参数不能为空"}"""
        self.assertEqual({"code": 0, "msg": "所有参数不能为空"},register("python15",'',''))
    def test_register_usernameandpswd1andpswd2_empty(self):
        """用户名密码、确认密码都为空返回：{"code": 0, "msg": "所有参数不能为空"}"""
        self.assertEqual({"code": 0, "msg": "所有参数不能为空"},register("",'',''))
    def test_register_usrname_less6(self):
        """用户名输入小于6位注册返回：{"code": 0, "msg": "账号和密码必须在6-18位之间"}"""
        self.assertEqual({"code": 0, "msg": "账号和密码必须在6-18位之间"},register("pyth",'123456','123456'))
    def test_register_usrname_more18(self):
        """用户名大于18位位注册返回：{"code": 0, "msg": "账号和密码必须在6-18位之间"}"""
        self.assertEqual({"code": 0, "msg": "账号和密码必须在6-18位之间"},register("python11111111111111",'123456','123456'))
    def test_register_pswd1andpswd2_less6(self):
        """密码小于6位注册返回：{"code": 0, "msg": "账号和密码必须在6-18位之间"}"""
        self.assertEqual({"code": 0, "msg": "账号和密码必须在6-18位之间"},register("python14",'12345','12345'))
    def test_register_pswd1andpswd2_more18(self):
        """密码大于18位注册返回：{"code": 0, "msg": "账号和密码必须在6-18位之间"}"""
        self.assertEqual({"code": 0, "msg": "账号和密码必须在6-18位之间"},register("python14",'1234561111111111111','1234561111111111111'))
    def test_register_usernameandpswd_more18(self):
        """用户名、密码都大于18位注册返回：{"code": 0, "msg": "账号和密码必须在6-18位之间"}"""
        self.assertEqual({"code": 0, "msg": "账号和密码必须在6-18位之间"},register("python14python14python14",'1234561111111111111','123456'))
    def test_register_usernameandpswd_less6(self):
        """用户名、密码都小于6位注册返回：{"code": 0, "msg": "账号和密码必须在6-18位之间"}"""
        self.assertEqual({"code": 0, "msg": "账号和密码必须在6-18位之间"}, register("pytho", '12345', '12345'))


if __name__ == '__main__':
 unittest.main()
 # suite=unittest.TestSuite
 # loader=unittest.TestLoader
 # suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))
 # runner=unittest.TextTestRunner
 # runner.run(suite)
 # br=BeautifulReport()
 # br.report("注册测试报告","br.html",report_dir='.')
