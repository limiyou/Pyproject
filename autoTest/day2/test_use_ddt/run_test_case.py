import unittest
#创建套件，自动发现并加载测试用例
from BeautifulReport import BeautifulReport

suite=unittest.defaultTestLoader.discover(r"D:\python\pythonProject\autoTest\day2\test_use_ddt\ddt_org")
br=BeautifulReport(suite)
#br.report("ddt测试注册报告",'ddt.html',report_dir='.')
br.report("李米柚的测试报告",'limiyou.html',report_dir='.')