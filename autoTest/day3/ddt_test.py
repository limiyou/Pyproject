import unittest
from ddt import ddt,data
from autoTest.day2.last_homework.reigster import register
@ddt
class RegisteraaTestCase(unittest.TestCase):
    cases=[
        {"title":"测试一下1",'expected':{"code":1,"msg":"注册成功"},"data":["lemont","123456","123456"]}
    ]
    @data(*cases)
    def test_registeraa(self,case):
        self.assertEqual(case['expected'],register(*case['data']))

if __name__ == '__main__':
    unittest.main()


