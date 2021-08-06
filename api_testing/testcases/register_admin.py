import jsonpath
from requests import request

from api_testing.common.handle_config import conf

#url='http://api.lemonban.com/futureloan/member/register'
url=conf['env']['url']+'/member/register'
data={
    'mobile_phone':'15538098212',
    'pwd':'lemonban',
    'type':0,
'reg_name':'柚柚7'

}
resp=request(method='post',url=url,json=data,headers=eval(conf['env']['headers']))
res=resp.json()
print(res)
admin_id=jsonpath.jsonpath(res,'$..id')[0]
print(admin_id)