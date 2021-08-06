# encoding='utf-8'
"""
安装requests库，模拟浏览器向服务器发送各种请求。
pip install requests
例如： 模拟浏览器发送http://api.lemonban.com/futureloan/请求
浏览器中输入一个地址，按回车，默认发送的是get请求。
"""
import requests
resp = requests.get('http://api.lemonban.com/futureloan/')  # 模拟浏览器发送get请求
print(resp.text)  # 输出服务器返回的数据
