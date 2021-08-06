import os
import unittest

# 审核接口： 普通用户添加项目，管理员进行审核。
# 前置条件
#  1. 管理员登录，普通用户要登录
#  2. 有待审核的项目
# 每个审核用例执行之前，添加一个项目（用普通用户），普通用户登录后添加项目
import jsonpath
from ddt import ddt, data
from requests import request

from api_testing.common.handle_config import conf
from api_testing.common.handle_excel import HandleExcel
from api_testing.common.handle_logging import log
from api_testing.common.handle_db import MySQLHandler
from api_testing.common.handle_path import DATA_DIR


@ddt
class TestAudit(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicases.xlsx'), sheet_name='audit')
    cases = excel.read_data()

    # 管理员登录, 普通用户登录，所有用例执行前
    @classmethod
    def setUpClass(cls) -> None:
        """前置条件：管理员登录，然后执行审核测试用例"""
        url = conf['env']['url'] + '/member/login'
        data = {
            'mobile_phone': conf['test_data']['admin_phone'],
            'pwd': conf['test_data']['admin_pwd']
        }
        headers = eval(conf['env']['headers'])
        resp = request(method='post', url=url, json=data, headers=headers)
        res = resp.json()  # 获得登录成功后的响应数据

        # 设置管理员用户token和id
        cls.admin_member_id=jsonpath.jsonpath(res,'$..id')[0]
        #cls.admin_member_id = jsonpath.jsonpath(res, '$..id')[0]  # 从响应数据中 获取member_id
        cls.admin_token = 'Bearer' + ' ' + jsonpath.jsonpath(res, '$..token')[0]  # 从响应数据中 获取token

        """前置条件：普通用户登录，用来新增项目"""
        url = conf['env']['url'] + '/member/login'
        data = {
            'mobile_phone': conf['test_data']['phone'],
            'pwd': conf['test_data']['pwd']
        }
        headers = eval(conf['env']['headers'])
        resp = request(method='post', url=url, json=data, headers=headers)
        res = resp.json()  # 获得登录成功后的响应数据
        # 设置普通用户token和id
        cls.member_id = jsonpath.jsonpath(res, '$..id')[0]  # 从响应数据中 获取member_id
        cls.token = 'Bearer' + ' ' + jsonpath.jsonpath(res, '$..token')[0]  # 从响应数据中 获取token
        #连接数据库
        cls.db = MySQLHandler()

    # 每条用例执行前，需要一个前置条件：普通用户创建项目，创建的项目必须是未审核的项目。
    def setUp(self) -> None:
        """前置条件：每条用例执行前，需要一个前置条件：普通用户创建一条待审核的项目"""
        url=conf['env']['url']+'/loan/add'
        data={
            'member_id':self.member_id,'title':'借钱想借多少借多少','amount':3000,"loan_rate": 12.0, "loan_term": 3,
            "loan_date_type": 1, "bidding_days": 5
        }
        headers=eval(conf['env']['headers'])
        headers['Authorization']=self.token #设置普通用户的token
        resp=request(method='post',url=url,headers=headers,json=data) #发送新增项目请求
        res=resp.json() #获取响应数据
        #print(res)
        self.loan_id=jsonpath.jsonpath(res,'$..id')[0]
        #print(self.loan_id)
    @data(*cases)
    def test_audit(self, case):
        #准备数据
        url=conf['env']['url']+case['url']
        case['data']=case['data'].replace('#loan_id#',str(self.loan_id))
        #pass_loan_id替换为self.pass_loan_id(最后审核通过的项目id)
        if '#pass_loan_id'in case['data']:
            case['data']=case['data'].replace('#pass_loan_id#',str(self.pass_loan_id))
        data=eval(case['data'])
        method=case['method']
        #headers添加admin_token,因为审核操作需要管理的token
        headers=eval(conf['env']['headers'])
        headers['Authorization']=self.admin_token
        resp=request(method=method,url=url,json=data,headers=headers) #发送审核请求
        expected=eval(case['expected'])  #预期结果
        res=resp.json() #审核操作后的实际结果

        #把标题为‘审核通过’的用例的loan_id记为：pass_loan_id
        if case['title']=='审核通过'and res['msg']=='OK':
            TestAudit.pass_loan_id=data['loan_id']#创建一个类属性

        #断言
        test_result='pass'
        try:
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'],res['msg'])
            #对数据库进行校验

            if case['check_sql']:
                sql = case['check_sql'].replace('#loan_id#', str(self.loan_id))
                status=self.db.find_one(sql)['status']
                self.assertEqual(expected['status'],status)
        except AssertionError as e:
            log.debug('预期结果是：',expected)
            log.debug('实际结果是：',res)
            log.exception(e)
            test_result='fail'
            raise e
        finally:
            self.excel.write_data(row=case['case_id']+1,column=8,value=test_result)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close()
if __name__ == '__main__':
    unittest.main()
