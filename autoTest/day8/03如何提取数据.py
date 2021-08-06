"""
response.text  返回的是文本str
response.content  返回的是bytes类型
response.json()   返回的是对象
"""
import json
from requests import request
def login():
   url='http://api.lemonban.com/futureloan/member/login'
   data={
       'mobile_phone':'17801234567',
       'pwd':'12345678'
   }
   headers={
       'X-Lemonban-Media-Type': 'lemonban.v1'
   }
   response=request('post',url=url,json=data,headers=headers)
   return response
if __name__ == '__main__':
    resp=login()
    print(resp.json())
    print(type(resp.json()))  # 返回的是Python对象
    # 获得返回值中的code
    print(resp.json()['code'])
    print(type(resp.text))  # 返回的是字符串，响应的内容，以unicode表示。（str  python3）

    print(json.loads(resp.text)['code'])
    print(type(resp.content))  # 返回的bytes  Content of the response, in bytes.
    print(json.loads(resp.content)['code'])
