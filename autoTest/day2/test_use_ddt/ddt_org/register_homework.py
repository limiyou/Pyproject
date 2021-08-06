
import unittest
from ddt import ddt,data
from autoTest.day2.last_homework.reigster import register
from autoTest.day2.test_use_ddt.test_ddt import case

@ddt
class RegisterATestCase(unittest.TestCase):
    cases = [
        {"title": "注册成功", 'expected': {"code": 1, "msg": "注册成功"}, 'data': ["limiyou", "123456", '123456']},
        {"title": "密码不一致", 'expected': {"code": 0, "msg": "两次密码不一致"}, 'data': ["miyoua", "12345", '123456']},
        {"title": "账户已存在", 'expected': {"code": 0, "msg": "该账户已存在"}, 'data': ["lemontree", "123456", '123456']},
        { "title": "用户名不能为空","expected": {"code": 0, "msg": "所有参数不能为空"},"data":["lem",'123456', '123456']},
        {"title": "密码不能为空", "expected": {"code": 0, "msg": "所有参数不能为空"}, "data": ["miyoua","", ""]},
        {"title": "用户名、密码不能为空", "expected": {"code": 0, "msg": "所有参数不能为空"}, "data": ["", "", ""]},
        {"title": '用户名不能小于6位',"expected":{"code": 0, "msg": "账号和密码必须在6-18位之间"},"data":["miyou","123456","123456"]},
        {"title": '密码不能小于6位', "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"}, "data": ["miyoua", "12345", "12345"]},
        {"title": '用户名、密码不能小于6位', "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"}, "data": ["miyou11111111111111111", "12345", "12345"]},
        {"title": '用户名不能大于18位', "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"},
         "data": ["miyou", "123456", "123456"]},
        {"title": '密码不能大于18位', "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"}, "data": ["miyoua", "12345111111111111111111111", "12345111111111111111111111"]},
        {"title": '用户名、密码不能小于6位', "expected": {"code": 0, "msg": "账号和密码必须在6-18位之间"},
         "data": ["miyou11111111111111111111111111111111111", "12345111111111111111111111","12345111111111111111111111"]},

    ]

    @data(*cases)
    def test_register(self,case):
        self.assertEqual(case['expected'],register(*case['data']))

if __name__ == "__main__":
    unittest.main()
