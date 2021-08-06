import re
import unittest

# 1. re.findall()
# 2. re.search()
# 3. re.complie()
# 4. re.finditer()
# 5. re.Match类常用的几个方法：  group()  groups()  start()  end()
import requests


def demo01():
    s='This is li miyou,hello,sweet!,your birthday is 20190423'
    p = re.compile(r'\d+|[a-zA-Z]+') #使用compile把正则表达式预编译，能提高速度
    matches = p.findall(s)
    print(matches)

def demo02():
    data1 = '{"user":"#user#","pwd":"#pwd#"}'
    data2 = {"user":"miyou","pwd":"123456"}
    regex=r"#(.*?)#"
    mathches=re.finditer(regex,data1)#返回的是一个迭代器，迭代器速度快，省内存
    for match in mathches:
        #print(type(match))
        #print(dir(match))
        print(match.group()) #group 获取匹配到的结果
        print(match.groups())#groups 获取匹配到的结果里的值

def demo03_search():
    # 扫描字符串以查找与模式的匹配项，返回Match对象，如果找不到匹配项，则返回None。
    s = '米柚 爱 7妈妈 的老师'
    patter = re.compile(r'(.*) 爱 (.*?) .*')  # 匹配模式
    match = patter.search(s)  # 返回的是类re.Match的一个对象
    # print(match.group())
    print(match.groups())  # groups 把所有的组匹配匹配到的结果放到一个元组。

def demo03_findall():
    s = '米柚 爱 7妈妈 的老师'
    mathces=re.findall(r'(.*) 爱 (.*?) .*', s) #返回的是列表
    print(mathces)
    print(type(mathces))


def demo04():

    url = 'http://jinyongxiaoshuo.com/xueshanfeihu/'
    r = requests.get(url)
    matches = re.findall(
        r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)',
        r.text)
    for match in matches:
        if match[1]:
            print('http://jinyongxiaoshuo.com/' + match[1])

data2 = {"user": "wuji", "pwd": "123456", "age": "18"}
def demo05(data1):
    matches=re.finditer('#(.*?)#',data1)
    for match in matches:
        print(match.group())
        #获得（.*?）匹配到的值
        print(match.groups()[0])
        data1=data1.data1.replace(match.group(),data2[match.groups()[0]])
    return data1

def demo06():
    '''
    match:从头匹配，如果匹配到，返回class re.Match的一个对象。匹配不到，返回None

    '''
    s='python is good, python is easy, python is fast!'
    r=re.match('python',s,flags=re.U)#re.I忽略大小写
    if r is not None:
        print(r.start())#匹配到的起始位置是从0即从头开始找
        print(r.end()) #匹配到的结束位置 6
        print(r.group())
        print(r.groups())
    else:
        print('没有匹配到任何结果')

def demo07_search():
    """
    search:扫描字符串以查找与模式的匹配项，返回Match对象；否则，返回None。
    找到之后，就不再找了。


    """
    s='hi，python is good, python is easy, python is fast, python is boss！'
    r=re.search('python', s)
    if r is not None:
        print(r.start())#匹配到的起始位置
        print(r.end()) #匹配到的结束位置
        print(r.group())#匹配到的值
        print(r.groups())#匹配到的组
    else:
        print('没有匹配到任何结果')

def demo08_findall():
    """
    findall:如果模式中存在一个或多个捕获组，则返回一个组列表；
    否则，返回一个列表。如果模式包含多个组，则这将是一个元组列表

    """
    s='hi，python is good, python is easy, python is fast, python is boss！'
    r= re.findall('python', s)
    if r:
        print(r)
    else:
        print('没有匹配到任何结果')
if __name__ == '__main__':
    # demo01()
    # demo02()
    # demo03_search()
    # demo03_findall()
    # demo04()
    # result=demo05(data1='{"user":"#user#","pwd":"#pwd#"}')
    # print(result)
    # demo06()
    # demo07_search()
    demo08_findall()