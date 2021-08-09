import unittest
from BeautifulReport import BeautifulReport

from api_testing.common.handle_logging import log
from api_testing.common.handle_path import CASE_DIR, REPORT_DIR
from api_testing.common.handle_send_email import send_report
from api_testing.testcases import  test_audit
from api_testing.testcases.practice import test_add
from autoTest.day2.test_use_ddt import test_register

log.info('开始执行测试用例......')
def  set_up_suite1():
    """套件1的前置条件"""
    pass

set_up_suite1()
suite1 = unittest.TestSuite()
# 2. 加载测试用例到 套件
suite1.addTest(unittest.TestLoader().discover(CASE_DIR))  #运行所有测试用例
suite1.addTest(unittest.TestLoader().loadTestsFromModule(test_register))
#suite1.addTest(unittest.TestLoader().loadTestsFromModule(test_add))
#suite1.addTest(unittest.TestLoader().loadTestsFromModule(test_audit))

# 3. 执行用例生成报告
report_name='2021年7月7日_接口自动化测试报告.html'
BeautifulReport(suite1).report('接口自动化测试',filename=report_name,report_dir=REPORT_DIR)

log.info('测试用例执行完毕！')
send_report(report_name)

