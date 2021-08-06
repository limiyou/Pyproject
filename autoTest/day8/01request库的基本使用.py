'''
使用requests完成登录
'''
import requests
from requests import request


def login():

   url='http://api.lemonban.com/futureloan/member/login'
   data={
       'mobile_phone':'17801234561',
       'pwd':'12345678'
   }
   headers={
       'X-Lemonban-Media-Type':'lemonban.v1'
   }
   resp= request('post',url=url,json=data,headers=headers)
   print(resp.json())
   print(resp.request.headers)  # 查看请求头

if __name__=="__main__"   :
    login()