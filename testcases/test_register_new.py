import os
import unittest
from random import randint

from requests import request

from api_testing.common.handle_config import conf
from api_testing.common.handle_path import DATA_DIR
from api_testing.library.myddt import ddt, data
from api_testing.common.handle_excel import HandleExcel
from api_testing.common.handle_logging import log
from api_testing.common.handle_db import MySQLHandler


@ddt
class RegisterTestCase(unittest.TestCase):
    # 1. 读取用例
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicases.xlsx'), 'register')
    cases = excel.read_data()
    print(cases)

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = MySQLHandler()

    @data(*cases)
    def test_register(self, case):
        # 0.处理数据
        self.phone = self.random_phone()

        # 0.1 获得随机手机号,并替换
        if "#phone#" in case['data']:
            # 0.2 把data中#phone#替换为随机的手机号
            case['data'] = case['data'].replace('#phone#', self.phone)
        # 0.3 把sql语句中#phone#替换为随机的手机号
        sql = case.get('check_sql')
        # 如果有sql，就验证sql语句
        if sql:
            sql = case['check_sql'].replace('#phone#',self.phone)

        # 1.发送请求
        resp = request(method=case['method'], url=case['url'], json=eval(case['data']),
                       headers=eval(conf['env']['headers']))
        # 2.获取预期结果和实际结果
        expected = eval(case['expected'])
        res = resp.json()
        # 3. 断言
        test_result = '通过'
        log.info('用例--{}--执行通过'.format(case['title']))
        # print(res)
        # 判断是否需要验证sql语句的执行
        #  把#phone# 替换为随机手机号

        try:
            if sql:
                r = self.db.find_count(sql)
                # self.assertEqual(1, r)
            self.assertEqual(expected['code'], res['code'])
        except AssertionError as e:
            test_result = '未通过'
            log.error('用例---{0}---执行未通过,注册手机号是{1}'.format(case['title'],self.phone))
            log.exception('e')
            raise e

        finally:
            self.excel.write_data(row=case['case_id'] + 1, column=8, value=test_result)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close()

    @classmethod
    def random_phone(cls):
        """随机生成一个数据库中没有的手机号"""
        phone = '178'  # 前缀
        while True:
            # 随机生成8个字符
            s = []
            for i in range(8):
                n = randint(0, 9)
                s.append(str(n))
            # 累加到phone
            phone += ''.join(s)
            # 查询数据库中有没有phone
            sql = 'SELECT reg_name FROM futureloan.member where mobile_phone={}'.format(phone)
            res = cls.db.find_count(sql)  # 看有几个phone的记录
            # 如果有，重新生成
            if res:
                continue
            # 如果没有，返回phone
            else:
                # cls.db.close()
                return phone


if __name__ == '__main__':
    unittest.main()
