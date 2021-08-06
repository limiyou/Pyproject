import unittest
#创建套件，自动发现并加载测试用例
from BeautifulReport import BeautifulReport

from autoTest.day2.test_use_ddt.ddt_org.register_homework import RegisterATestCase


suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RegisterATestCase))
br=BeautifulReport(suite)
#br.report("ddt测试注册报告",'ddt.html',report_dir='.')
br.report("注册模块的ddt测试报告",'register_ddt.html',report_dir='.')