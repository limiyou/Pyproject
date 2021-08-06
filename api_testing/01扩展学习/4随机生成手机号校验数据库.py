from random import randint

from api_testing.common.handle_db import MySQLHandler


def random_phone():
    """随机生成一个数据库中没有的手机号"""
    db=MySQLHandler()
    phone='178'#前缀
    while True:
        s=[]
        for i in range(8):
            n=randint(0,9)
            s.append(str(n))
        #累加到phone
        print(''.join(s))
        phone+=''.join(s)
        print('1. ',phone)
        #查询数据库中有没有这个phone
        sql='SELECT reg_name FROM futureloan.member where mobile_phone={}'.format(phone)
        print(sql)
        res=db.find_count(sql)#查看有几个phone
        #如果有，重新生成

        if res:
            continue
        #如果没有，返回phone
        else:
            return phone

    db.close()


if __name__ == '__main__':
    p=random_phone()
    print(p)

