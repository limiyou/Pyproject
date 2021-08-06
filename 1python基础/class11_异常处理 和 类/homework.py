'''
封装一个学生类，(自行分辨定义为类属性还是实例属性)

属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩， 职责。

如果是类属性请提前定义，

如果是实例属性请初始化以后添加这个属性的值。
'''



class student():
    def __init__(self,identity,name,age,gender,EnglishGrade,MathGrade,ChineseGrade,responsibiity):
        self.identity=identity
        self.name=name
        self.age=age
        self.gender=gender
        self.EnglishGrade=EnglishGrade
        self.MathGrade=MathGrade
        self.ChineseGrade=ChineseGrade
        self.resonsibility=responsibiity
        print("{}的英语成绩为{}".format(name,EnglishGrade) )
    def teacher(self,teacherName):
        print(self.name +f"的老师是 {teacherName}")
lily=student("学生",'lily',18,'female',99,89,88,'study')
lily.teacher("李老师")


# class Student():
#    def __init__(self,identity,name,age,gender,englishGrade ,mathGrade,chineseGrade, responsibility):
#      self.identity=identity
#      self.name=name
#      self.age=age
#      self.gender=gender
#      self.englishGrade=englishGrade
#      self.mathGrade=mathGrade
#      self.chineseGrade=chineseGrade
#      self.responsibility=responsibility
#    def teacher(self):
#        print(self.name+"的老师是李老师")
# Lily=Student(identity='banzhang',name='lily',age=18,
#         gender='female',englishGrade=88,mathGrade=99,chineseGrade=99,responsibility='good student')
# Lily.teacher()
# print(Lily.name+"的年龄是"+str(Lily.age))






'''
5 定义一个登录的测试用例类LoginTestCase 登录url地址为："http://www.xxxx.com/login" 请求方法为："post" 、 请自行分辨下列属性，应该定义为类属性还是实例属性 

- 属性：用例编号 url地址 请求参数 请求方法 预期结果 实际结果'''
class LoginTestCase():
     def __init__(self,caseid,url,parameter,method,respectResult,actualResult):
         self.caseid=caseid
         self.url=url
         self.parameter=parameter
         self.post=method
         self.respectResult=respectResult
         self.actualResult=actualResult
         print(f'{caseid}的实际结果为：{actualResult}')

testcase1=LoginTestCase("0318001","http://www.xxxx.com/login","name,pwd",'psot','成功','成功')













# class LoginTestCase():
#     def __init__(self, caseid, url, parameter, method, respectResult, actualResult):
#         self.caseid = caseid
#         self.url = url
#         self.parameter = parameter
#         self.method = method
#         self.respectResult = respectResult
#         self.actualResult = actualResult
# case1 = LoginTestCase(caseid="test001",url= "http://www.xxxx.com/login",
#                       parameter="name",method="post",respectResult="pass",actualResult="fail")
# print(case1.actualResult)

