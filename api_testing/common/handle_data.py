import re
import unittest

from api_testing.common.handle_config import conf


class EnvData(object):
    """用来保存动态环境变量"""
    loan_id=None
    member_id=None
    token=None


def replace(data):
    """把测试用例中如#phone#、#pwd#等数据替换成conf.ini中对应的数据
        配置文件conf.ini中没有的数据，从内存中动态获取，如：member_id,token....

        """
    matches=re.finditer("#(.*?)#", data)
    for match in matches:
        s1=match.group()
        print(s1)
        try:
            key=match.groups()[0]
            s2=conf['test_data'][key]

        except KeyError as e:
            s2=getattr(EnvData,key)
        data=data.replace(s1,str(s2))
    return data

if __name__ == '__main__':
    data='{"mobile_phone":"#phone#","pwd":"#pwd#"}'
    print(replace(data))


