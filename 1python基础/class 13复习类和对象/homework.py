"""
封装一个学生类，(自行分辨定义为类属性还是实例属性)

属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩， 职责。

如果是类属性请提前定义，

如果是实例属性请初始化以后添加这个属性的值
"""
# class Student():
#     identity="student"
#     responsibility="study"
#     def __init__(self,name,age,gender,englishgrade=0,mathgrade=89,chinesegrade=99):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.englishgrade=englishgrade
#         self.mathgrade=mathgrade
#         self.chinesegrade=chinesegrade
# Lily=Student("lily",12,"female",99,98,99)
# print(Lily.name)
"""
定义一个登录的测试用例类LoginTestCase 登录url地址为："http://www.xxxx.com/login" 请求方法为："post" 、 请自行分辨下列属性，应该定义为类属性还是实例属性 

- 属性：用例编号 url地址 请求参数 请求方法 预期结果 实际结果"""
# class LoginTestCase():
#     url="http://www.xxxx.com/login"
#     method=["post","get"]
#     def __init__(self,caseid,parameters,respected,actual):
#         self.caseid=caseid
#         self.parameters=parameters
#         self.respected=respected
#         self.actual=actual
#
# testcase1=LoginTestCase("001",["useername","pasword"],"login sucess",'login sucess')
# print(testcase1.caseid)




"""
定义一个手机类，

1. 具有打电话和录音的方法

2. 打电话的时候可以录音，也可以不录音。（方法调用其他方法）"""

# class Mobile():
#    def __init__(self,number):
#       self.number=number
#    def call(self,to,recorded=False):
#        """打电话"""
#        print("{}给{}打电话。。。".format(self.number,to))
#
#        if recorded:
#            self.record()
#    def record(self):
#        """录音"""
#        print("{}正在录音".format(self.number))
#
# phone=Mobile("15711375237")
# phone.call("小新",recorded=True)


"""
定义一个 ExcelHandler 类，所有方法不需要实际操作实现（不需要你真的去打开 excel, 不需要你真的把数据读出来。我们练习的是定义类的思维。）

1. 初始化传入 文件路径。


2， 定义打开 excel 方法。


3. 定义获取 sheet 表格方法，根据 名称获取。


4. 定义读取 sheet 表格数据的方法。 （读取需要先打开，再获取表格。）


5， 定义关闭文件方法。"""

class ExcelHandler():
    def __init__(self,file_path):
        """初始化"""
        self.file_path=file_path

    def open(self):
        "打开文件"
        print("打开文件{}".format(self.file_path))


    def get_sheet(self,name):
        "获取表格"
        self.open_file(self)
        print(f"获取表格：{name}")

    def read_data(self,name):
        "读取数据"
        self.get_sheet(name)
        print("读取数据")

    def close(self):
        print("关闭文件：{}".format(self.file_path))
