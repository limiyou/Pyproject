import unittest
from ddt import ddt,data

from autoTest.day3.homework.HandleExcel import Hand_Excel
from autoTest.day3.homework.login import login_check

@ddt
class LogingTestCase(unittest.TestCase):
    excel=Hand_Excel(r"D:\python\pythonProject\autoTest\day3\homework\登录接口.xlsx")
    cases=excel.read_data()
    @data(*cases)
    def test_login(self,case):
        test_result=""
        try:
            self.assertEqual(eval(case["expected"]),login_check(*eval(case["data"])))
        except AssertionError as e:
            test_result="不通过"
        else:
            test_result="通过"
        finally:
            self.excel.write_data(row=case["id"]+1,column=5,value=test_result)

if __name__ == '__main__':
    unittest.main()
