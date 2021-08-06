#url='http://httpbin.org/post' #用于http测试的网站
import requests
url='http://httpbin.org/post'
hraders={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
data={
    'name':'miyou',
    'pwd':'123456'
}
resp=requests.post(url,json=data,headers=hraders)
# print(resp.json())
# print(resp.text)
with open('cnblogs.html',mode='wb') as f:
    f.write(resp.content)
# 爬虫工程师：  requests 采集数据，   网站 反爬措施， 例如： 使用UA检测（User-Agent)