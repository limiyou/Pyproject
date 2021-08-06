import unittest
from BeautifulReport import BeautifulReport

from autoTest.day2.last_homework import test_register
from autoTest.day2.last_homework.test_register import RegisterTestCase

if __name__ == '__main__':

 '''创建suite对象'''
 suite=unittest.TestSuite()
 """加载器"""
loader=unittest.TestLoader()
"""往套件里加测试用例"""
#方法1.从类中加载所有case
#suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))
#方法2.从模块中加载所有case
#suite.addTest(loader.loadTestsFromModule(test_register))
#方法3.从文件夹加载所有case
suite.addTest(loader.discover(r"D:\python\pythonProject\autoTest\day2\last_homework"))
'''运行器'''
# runner=unittest.TextTestRunner()
"""运行测试用例"""
# runner.run(suite)
br=BeautifulReport(suite)
br.report("李静的第一份测试报告",'br.html',report_dir='.')
