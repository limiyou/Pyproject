import os
import unittest

import jsonpath
from requests import request

from api_testing.common.handle_config import conf
from api_testing.common.handle_path import DATA_DIR
from api_testing.common.handle_excel import HandleExcel
from api_testing.common.handle_db import MySQLHandler
# 添加项目
# 前置条件： 登录
# 数据库检验思路: 添加项目条数 + 1  =    添加后项目条数
from ddt import data, ddt
from api_testing.common.handle_logging import log


@ddt
class TestAdd(unittest.TestCase):
    excle = HandleExcel(os.path.join(DATA_DIR, 'apicases.xlsx'), 'add')
    cases = excle.read_data()

    @classmethod
    def setUpClass(cls) -> None:
        url = conf['env']['url'] + '/member/login'
        data = {
            'mobile_phone': conf['test_data']['phone'],
            'pwd': conf['test_data']['pwd']
        }
        headers = eval(conf['env']['headers'])
        resp = request(method='post', url=url, json=data, headers=headers)
        res = resp.json()  # 获得登录成功后的响应数据
        cls.member_id = jsonpath.jsonpath(res, '$..id')[0]  # 从响应数据中 获取member_id
        cls.token = 'Bearer' + ' ' + jsonpath.jsonpath(res, '$..token')[0]  # 从响应数据中 获取token
        cls.db = MySQLHandler()

    @data(*cases)
    def test_add(self, case):
        # 准备用例数据
        before_count = 0
        after_count = 0
        url = conf['env']['url'] + case['url']
        case['data'] = case['data'].replace('#member_id#', str(self.member_id))
        data = eval(case['data'])
        headers = eval(conf['env']['headers'])
        headers['Authorization'] = self.token
        expected = eval(case['expected'])

        # 添加项目前，如果有check_sql，执行sql语句，记录返回值，记做before_count

        sql = case['check_sql']  # None  or   具体的sql语句
        if sql:  # 如果有sql语句
            sql = sql.replace('#member_id#', str(self.member_id))
            before_count = self.db.find_count(sql)

        # 添加项目
        resp = request(method=case['method'], url=url, json=data, headers=headers)
        res = resp.json()  # 获取实际结果

        # 添加项目后，如果有check_sql，执行sql语句，记录返回值，记做after_count
        if sql:  # 如果有sql语句
            after_count = self.db.find_count(sql)

        # 如果有check_sql，self.assertEqual(before_count + 1, after_count)

        test_result = '通过'
        try:
            # 预期结果和实际结果的断言
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'],res['msg'])

            # 数据库校验的断言
            if sql:
                self.assertEqual(before_count + 1, after_count)
        except AssertionError as e:
            test_result = '不通过'
            log.error('用例---{}---执行未通过'.format(case['title']))
            log.debug('预期结果是：{}'.format(expected))
            log.debug('实际结果是：{}'.format(res))
            log.critical(e)
            raise e
        finally:
            self.excle.write_data(row=case['case_id'] + 1,column=8,value=test_result)


if __name__ == '__main__':
    unittest.main()
