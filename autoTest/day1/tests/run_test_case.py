
import unittest
# todo:在单独的文件中运行任意测试用例
from unittest import TestCase, suite

from BeautifulReport import BeautifulReport

from autoTest.day1.tests.test_login import LoginTestCase


if __name__ == '__main__':

 '''创建suite对象'''
 suite=unittest.TestSuite()
 """加载器"""
loader=unittest.TestLoader()
"""往套件里加测试用例"""
#方法1.从类中加载所有case
suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))
#方法2.从模块中加载所有case
suite.addTest(loader.loadTestsFromModule())
'''运行器'''
# runner=unittest.TextTestRunner()
"""运行测试用例"""
# runner.run(suite)
br=BeautifulReport(suite)
br.report("李静的第一份测试报告",'br.html',report_dir='.')

