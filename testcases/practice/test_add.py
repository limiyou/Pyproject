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


@ddt
class AddTestCase(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicases.xlsx'), 'add')
    cases = excel.read_data()
    #前置条件：登录成功，获取用户信息
    @classmethod
    def setUpClass(cls) -> None:
        url=conf['env']['url']+'/member/login'
        data={
            'mobile_phone':conf['test_data']['phone'],
            'pwd':conf['test_data']['pwd']
        }
        headers=eval(conf['env']['headers'])
        resp=request(method='post',url=url,json=data,headers=headers)#发送登录请求
        res=resp.json()#获取登录响应数据
        cls.member_id = jsonpath.jsonpath(res, '$..id')[0]  #获取用户登录成功后的member_id
        cls.token='Bearer'+' '+jsonpath.jsonpath(res,'$..token')[0]
        cls.db=MySQLHandler()  #连接数据库

    @data(*cases)
    def test_add(self,case):
        before_count=0
        after_count=0
        url=conf['env']['url']+case['url']
        data=eval(case['data'].replace('#member_id#',str(self.member_id)))
        headers=eval(conf['env']['headers'])
        headers['Authorization']=self.token
        expected=eval(case['expected'])
        method=case['method']
        sql=case.get('check_sql')
        if sql:
            sql=sql.format(self.member_id)
            before_count=self.db.find_count(sql)  #获取新增项目前的项目数量

        resp=request(method=method,url=url,json=data,headers=headers)
        res=resp.json()
        if sql:

            after_count=self.db.find_count(sql) #获取新增后的项目数量

        test_result='测试通过'
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'],res['msg'])
            if sql:
                self.assertEqual(before_count+1,after_count)
        except AssertionError as e:

            log.error('--测试用例{}--执行未通过'.format(case['title']))
            log.debug('--测试用例的预期结果是：{}'.format(case['expected']))
            log.debug('--测试用例的实际结果是：{}'.format(res))
            test_result = '测试不通过'
            raise e
        finally:
            self.excel.write_data(row=case['case_id']+1,column=8,value=test_result)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close()


if __name__ == '__main__':
    unittest.main()
