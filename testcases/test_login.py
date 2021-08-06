import unittest
import os
from requests import request
from api_testing.common.handle_config import conf
from api_testing.common.handle_excel import HandleExcel
from api_testing.common.handle_logging import log
from api_testing.common.handle_path import DATA_DIR
from api_testing.library.myddt import ddt, data
import arrow
# 获取测试用例文件的绝对路径

filename = os.path.join(DATA_DIR, 'apicases.xlsx')

@ddt
class LoginTestCase(unittest.TestCase):

    # 从data/apicases.xlsx  读取用例
    excel = HandleExcel(filename=filename, sheet_name='login')
    cases = excel.read_data()

    @data(*cases)
    def test_login(self, case):
        # 1.发请求，获得响应数据
        # 1.1 请求方法是什么？
        method = case['method']
        # 1.2 提交的数据是什么？
        data = eval(case['data'])
        # 1.3 请求头
        # headers = conf.get('env','headers')
        headers = eval(conf['env']['headers'])
        # 1.4 请求地址
        url = case['url']
        #print(type(url), type(headers), type(data), type(method))
        resp = request(method=method, url=url, headers=headers, json=data)  # 发送请求，获得响应数据

        # 2. 对响应数据进行断言，对比预期结果和实际结果
        # 2.1 获得预期结果
        expected = eval(case['expected'])
        #print('预期结果是：', expected)
        # 2.2 获得实际结果
        res = resp.json()
        #print('实际结果是：', resp.json())
        # 2.3 断言预期结果和实际结果
        # 2.4 获取行号
        row = case['case_id'] + 1
        test_result = ''
        try:

            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except AssertionError as e:
            log.error('用例--{}--执行未通过'.format(case['title']))
            test_result = '未通过'
        else:
            log.info('用例--{}--执行通过'.format(case['title']))
            test_result = '通过'

        # 2.5  把结果写入excel
        finally:
            self.excel.write_data(row=row, column=8, value=test_result)


if __name__ == '__main__':
    unittest.main()
