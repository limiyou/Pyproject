"""
setUpClass： 只执行一次，在所有用例前
tearDownClass： 只执行一次，在所有用例后
setUp: 每个用例前执行
tearDown：每个用例后执行
"""
import unittest
class TestDemo(unittest.TestCase):
    # def setUp(self) -> None:
    #     print("3.setup....")

    @classmethod
    def setUpClass(cls) -> None:
        print('1.我是setUpClass')
    def test01(self):
        print('test01')

    def test02(self):
        print('test02')
    @classmethod
    def tearDownClass(cls) -> None:
        print('2.我是tearDownClass')

    # def tearDown(self) -> None:
    #     print('4.tearDown....')

if __name__ == '__main__':
    unittest.main()