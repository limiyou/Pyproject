import decimal
import unittest
import os

import jsonpath
from requests import request

from api_testing.common import handle_excel
from api_testing.common.handle_config import conf
from api_testing.common.handle_db import MySQLHandler
from api_testing.common.handle_excel import HandleExcel
from api_testing.common.handle_logging import log
from api_testing.common.handle_path import DATA_DIR
from api_testing.library.myddt import data, ddt

filename=os.path.join(DATA_DIR,'apicases.xlsx')
@ddt
class MyTestCase(unittest.TestCase):
    excel=HandleExcel(filename,'withdraw')
    cases=excel.read_data()

   #前置条件：登录成功，获取用户信息
    @classmethod
    def setUp(cls) -> None:
        url=conf['env']['url']+'/member/login'
        data={'mobile_phone':conf['test_data']['phone'],
              'pwd':conf['test_data']['pwd']
              }
        headers=eval(conf['env']['headers'])
        resp=request('post',json=data,url=url,headers=headers) #发送登录请求
        res=resp.json()
        #获取用户ID
        cls.member_id=jsonpath.jsonpath(res,'$..id')[0]
        #获取用户token
        cls.token=jsonpath.jsonpath(res,'$..token')[0]
        #连接数据库
        cls.db=MySQLHandler()
    @data(*cases)
    def test_withdraw_money(self,case):
        url=conf['env']['url']+case['url']
        data=eval(case['data'].replace('#member_id#', str(self.member_id)))#将Excel中的#member_id#替换为self.member_id
        headers=eval(conf['env']['headers'])
        headers['Authorization'] = self.token
        expected=eval(case['expected'])
        #判断是否需要检验数据库
        sql = case.get('check_sql')
        if sql:
            sql=sql.format(self.member_id)  #把sql语句中的id={}替换为当前用户的ID
            before_money=self.db.find_one(sql)['leave_amount']

        resp=request(method=case['method'],url=url,json=data,headers=headers)  #发送取现操作
        res=resp.json()
        if sql:

            after_money=self.db.find_one(sql)['leave_amount']
        test_result = '测试通过'
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])


            if sql:
               money=decimal.Decimal(str(data['amount']))
               self.assertEqual(money,before_money - after_money)
        except AssertionError as e:
           log.error('测试用例--{}执行未通过--'.format(case['title']))
           log.exception(e)
           test_result='测试不通过'
           raise e
        finally:
            self.excel.write_data(row=case['case_id']+1, column=8, value=test_result)

        @classmethod
        def tearDownClass(cls) -> None:
            cls.db.close()



if __name__ == '__main__':
    unittest.main()
