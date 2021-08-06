import unittest

# from autoTest.day1.user.login import login_check
#
#
# class LoginTestCase(unittest.TestCase):
#     def test_login_success(self):
#         self.assertEqual({"code":1,"msg":"登录成功"},login_check("lemon",'123456'))
from autoTest.day1.tests.test_login import LoginTestCase

if __name__ == '__main__':
  unittest.main()

#  suite=unittest.TestSuite()
# loader=unittest.TestLoader
# suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))
# runner=unittest.TextTestRunner()
# runner.run(suite)
