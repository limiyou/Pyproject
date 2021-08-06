import re

# todo:re.match与re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
#re.match(pattern,string,flags)
   #pattern:匹配的正则表达式
   #string：要匹配的字符串
   #flags:标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配。。
print(re.match('www','www.rubbon.com').span()) #在起始位置匹配  （0,3）

print(re.match('com','www.rubbon.com')) #不在起始位置匹配  None


def demo_match():
    line='Cats nihao are smatter than dogs'
    r=re.match(r'(.*) are (.*?) .*', line,re.M|re.I)
    if r is not None:
        print("r.group():",r.group())
        print("r.group(1):",r.group(1))
        print("r.group(2):",r.group(2))
    else:
        print('No mathch!!!')



#re.search()方法
#匹配成功re.search方法返回一个匹配的对象，否则返回None。
#我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
def demo_search():
   line='Cats are smarter than dogs'
   r=re.search(r'(.*) are (.*?) .*', line, re.M|re.I)
   if r is not None:
       print("r.group():", r.group())
       print("r.group(1):", r.group(1))
       print("r.group(2):", r.group(2))
   else:
       print('Nothing found!!!')


def demo3():
    line = "Cats are smarter than dogs";

    matchObj = re.match(r'dogs', line, re.M | re.I)
    if matchObj:
        print("match --> matchObj.group() : ", matchObj.group())

    else:
        print("No match!!")

    matchObj = re.search(r'dogs', line, re.M | re.I)
    if matchObj:
        print("search --> searchObj.group() : ", matchObj.group())

    else:
        print("No match!!")



#re.sub(pattern, repl, string, count=0, flags=0)
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

if __name__ == '__main__':
    # demo_match()
    # demo_search()
    demo3()
