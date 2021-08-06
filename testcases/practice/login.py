# 获取测试用例的绝对路径
import os
import unittest

from requests import request

from api_testing.common.handle_config import conf
from api_testing.common.handle_excel import HandleExcel
from api_testing.common.handle_logging import log
from api_testing.common.handle_path import DATA_DIR
from api_testing.library.myddt import ddt, data

# 获取测试用例文件的绝对路径
filename = os.path.join(DATA_DIR, 'apicases.xlsx')


@ddt
class LoginTestCase(unittest.TestCase):
    excel = HandleExcel(filename=filename, sheet_name='login')
    cases = excel.read_data()

    # 从data/apicases.xlsx  读取用例
    @data(*cases)
    def test_login(self, case):
        # 1.发请求，获得响应数据
        # 1.1 请求方法
        method = case['method']
        # 1.2 提交的数据
        data = eval(case['data'])
        # 1.3 请求头
        # headers = conf.get('env','headers')
        headers = eval(conf['env']['headers'])
        # 1.4 请求地址
        url = conf['env']['url'] + '/member/login'
        #print(type(url), headers, data, type(method))
        # 发送请求，获得响应数据
        resp = request(method=method, url=url, json=data, headers=headers)

        # 2. 对响应数据进行断言，对比预期结果和实际结果
        # 2.1 获得预期结果

        expected = eval(case['expected'])
        # 2.2 获得实际结果
        res = resp.json()
        print(res)

        test_result = ''

        # 2.3 断言预期结果和实际结果
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except AssertionError as e:
            log.error('测试用例--{}--执行未通过'.format(case['title']))

            test_result = 'fail'
        else:
            log.info('测试用例--执行通过'.format(case['title']))
            test_result='pass'

        finally:
            self.excel.write_data(row=case['case_id']+1, column=8,value=test_result)


if __name__ == '__main__':
    unittest.main()
