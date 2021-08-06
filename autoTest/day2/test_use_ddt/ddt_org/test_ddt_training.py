"""
第三方插件ddt的使用
"""
import unittest
from ddt import ddt,data
from autoTest.day2.last_homework.reigster import register
from autoTest.day2.test_use_ddt.test_ddt import case

@ddt
class RegisterTestCase(unittest.TestCase):

    cases=[
        {"title": "注册成功",  'expected': {"code": 1, "msg": "注册成功"},'data':["limiyou","123456",'123456']},
        {"title": "密码不一致", 'expected': {"code": 0, "msg": "两次密码不一致"}, 'data': ["miyoua", "12345", '123456']},
        {"title": "账户已存在", 'expected': {"code": 0, "msg": "该账户已存在"}, 'data': ["lemontree", "123456", '123456']},
    ]
    @data(*cases)
    def test_register(self,case):
        self.assertEqual(case['expected'],register(*case['data']))

if __name__ == "__main__":
    unittest.main()
