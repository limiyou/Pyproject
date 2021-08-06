import unittest

from BeautifulReport import BeautifulReport

from autoTest.day2.last_homework.reigster import register


class RegisterTestCase(unittest.TestCase):
    pass


if __name__ == '__main__':
 unittest.main()
 # suite=unittest.TestSuite
 # loader=unittest.TestLoader
 # suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))
 # runner=unittest.TextTestRunner
 # runner.run(suite)
 # br=BeautifulReport()
 # br.report("注册测试报告","br.html",report_dir='.')
