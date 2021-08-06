


import unittest
# todo:在单独的文件中运行任意测试用例
from unittest import TestCase, suite

from autoTest.day1.tests.test_login import LoginTestCase





if __name__ == '__main__':
 '''创建suite对象'''
 suite=unittest.TestSuite()
 """加载器"""
loader=unittest.TestLoader()
"""往套件里加测试用例"""
suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))
'''运行器'''
runner=unittest.TextTestRunner()
runner.run(suite)

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))
runner=unittest.TextTestRunner()
runner.run(suite)