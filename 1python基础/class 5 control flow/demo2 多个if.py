#尽量避免多重嵌套
username="miyou"
password=" "
gender="未知"
# if username=="miyou":
#     print("用户名正确")
#     if password=="123456":
#         print("密码正确")
#         if gender=="男":
#           print("性别符合条件")
#         else:
#             print("性别不符合")
#     elif password==" ":
#         print("密码为空")
#     else:
#         print("密码错误")
# else:
#     print("用户名不正确")

#尽量避免多重嵌套
if username=='miyou' and password=='123456' and gender=='男':
    print("登录成功")
elif username=="miyou" and password==" ":
    print("密码为空")
else:
    print("登录失败")
