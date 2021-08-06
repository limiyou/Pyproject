"""
第三方插件ddt的使用
"""
import unittest
from ddt import ddt,data
from autoTest.day2.last_homework.reigster import register
from autoTest.day3.Handle_Excel import Handle_Excel


@ddt
class RegisterTestCase(unittest.TestCase):

    # cases = [
    #     {'title':'注册成功','expected':{"code": 1, "msg": "注册成功"},'data':['wulaoer','123456','123456']},
    #     {'title': '密码不一致', 'expected': {"code": 0, "msg": "两次密码不一致"}, 'data': ['wuji', '123457', '123456']},
    #     {'title': '账户已存在', 'expected': {"code": 0, "msg": "该账户已存在"}, 'data': ['lemon', '123456', '123456']},
    # ]


    excel = Handle_Excel(r'D:\python\pythonProject\autoTest\day3\注册接口.xlsx')
    cases = excel.read_data()

    @data(*cases)
    def test_register(self,case):
        # 定义一个变量，用来存储结果
        test_result = ''
        # 如果测试通过，令test_result = '通过‘  (无异常，代表通过）
        # 如果测试失败，令test_result = '不通过'  (有AssertionError异常，代表不通过)
        # 最后把测试结果写入测试用例中
        try:
            self.assertEqual(eval(case['expected']),register(*eval(case['data'])))
        except AssertionError as e:
            test_result = '不通过'
            print(type(e))
            # raise e
        else:
            test_result = '通过'
        finally:
            self.excel.write_data(row=case['id']+1,column=5,value=test_result)


if __name__ == '__main__':
    unittest.main()