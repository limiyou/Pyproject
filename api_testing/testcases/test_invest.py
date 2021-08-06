import os
import unittest
from dataclasses import replace
from decimal import Decimal

import jsonpath
from requests import request

from api_testing.common.handle_config import conf
from api_testing.common.handle_data import replace,EnvData
from api_testing.common.handle_db import MySQLHandler
from api_testing.common.handle_excel import HandleExcel
from api_testing.common.handle_path import DATA_DIR
from api_testing.library.myddt import ddt, data


@ddt
class InvestTestCase(unittest.TestCase):
    filename = os.path.join(DATA_DIR, 'apicases.xlsx')
    excel = HandleExcel(filename, sheet_name='invest')
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = MySQLHandler()

    @data(*cases)
    def test_invest(self, case):

        # 1、准备数据
        url = conf['env']['url'] + case['url']
        headers = eval(conf['env']['headers'])
        # 判断 case['interface']是不是login
          #1.如果不是登录接口，需返回token
        if case['interface'] != 'login':
            headers['Authorization']=getattr(EnvData,'token') # 把token添加到headers中
        # 替换数据
        case['data'] = replace(case['data'])
        if case['check_sql']:  # 投资前的信息：投资人用户余额，投资记录数，流水记录数
            sql1 = "select * from futureloan.member where id = {}".format(EnvData.member_id)
            sql2 = "select*from futureloan.invest where member_id={} and loan_id={}".format(EnvData.member_id,EnvData.loan_id)
            sql3 = 'select * from futureloan.financelog where pay_member_id = {};'.format(EnvData.member_id)
            before_amount=self.db.find_one(sql1)['leave_amount']
            before_invest_count=self.db.find_count(sql2)
            before_invest_log=self.db.find_count(sql3)
        data=eval(case['data'])
        resp=request(method=case['method'],url=url,headers=headers,json=data)
        res=resp.json()
        print(str(case['case_id'])+"预期结果是：",case['expected'])
        print(str(case["case_id"])+"实际结果是： ", res)
        #2.case['interface']是登录接口
        if case['interface']=='login':#登录的特殊处理
            EnvData.member_id=jsonpath.jsonpath(res,'$..id')[0]
            token=jsonpath.jsonpath(res,"$..token")[0]
            token_type=jsonpath.jsonpath(res,"$..token_type")[0]
            EnvData.token=token_type +" "+token

        #3.case['interface']是添加项目接口
        if case['interface']=='add':
            EnvData.loan_id=jsonpath.jsonpath(res,"$..id")[0]

        if case['check_sql']:

           after_amount = self.db.find_one(sql1)['leave_amount']
           after_invest_count = self.db.find_count(sql2)
           after_invest_log = self.db.find_count(sql3)
           print(before_amount, before_invest_count, before_invest_log)
           print(after_amount, after_invest_count, after_invest_log)
           invest_amount=Decimal(str(data['amount']))
           self.assertEqual(before_amount- after_amount, invest_amount)
           self.assertEqual(after_invest_count - before_invest_count, 1)
           self.assertEqual(after_invest_log - before_invest_log, 1)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close()

if __name__ == '__main__':
    unittest.main()
