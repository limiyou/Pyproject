import decimal
import os
import unittest

import jsonpath
from requests import request

from api_testing.common.handle_config import conf
from api_testing.common.handle_db import MySQLHandler
from api_testing.common.handle_excel import HandleExcel
from api_testing.common.handle_logging import log
from api_testing.common.handle_path import DATA_DIR
from api_testing.library.myddt import ddt, data
from autoTest.day2.test_use_ddt.test_ddt import cases


@ddt
class WithdrawTestCase(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicases.xlsx'), 'withdraw')
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls) -> None:
        # 1。登录成功，获得response
        url = conf['env']['url'] + '/member/login'  # 登录接口的完整地址
        data = {
            'mobile_phone': conf['test_data']['phone'],
            'pwd': conf['test_data']['pwd']
        }
        headers = eval(conf['env']['headers'])
        resp = request(method='post', url=url, json=data, headers=headers)
        res = resp.json()
        # 2. 获取token，并把token设置为类属性   cls.token  = ....
        cls.token = 'Bearer' + ' ' + jsonpath.jsonpath(res, '$..token')[0]
        print(cls.token)
        # 3. 获取member_id，并把member_id设置为类属性  cls.member_id = ....
        cls.member_id = jsonpath.jsonpath(res, '$..id')[0]
        # 4. 连接数据库
        cls.db = MySQLHandler()

    @data(*cases)
    def test_withdraw(self, case):
        url = conf['env']['url'] + case['url']
        data = eval(case['data'].replace('#member_id#', str(self.member_id)))
        headers = eval(conf['env']['headers'])
        headers['Authorization'] = self.token
        expected = eval(case['expected'])
        # 判断用例是否需要数据库校验
        sql = case.get('check_sql')
        if sql:
            sql = sql.format(self.member_id)  # 把sql语句中的id={}  替换为  当前用户的ID
            before_money = self.db.find_one(sql)['leave_amount']  # 提现钱前余额
        resp = request(method=case['method'], url=url, json=data, headers=headers)
        res = resp.json()
        print(res)
        # 获得充值后的余额
        if sql:
            after_money = self.db.find_one(sql)['leave_amount']
        test_result = '通过'
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            if sql:
                money = decimal.Decimal(str(data['amount']))
                self.assertEqual(money, before_money - after_money)
        except AssertionError as e:
            log.error('用例--{}--执行未通过'.format(case['title']))
            # log.debug("预期结果：{}".format(expected))
            # log.debug('实际结果 {}'.format(res))
            # log.exception(e)
            test_result = '不通过'
            raise e

        finally:
            self.excel.write_data(row=case['case_id']+1,column=8, value=test_result)
    @ classmethod
    def tearDownClass(cls) -> None:
        # 关闭数据库
        cls.db.close()


if __name__ == '__main__':
    unittest.main()
