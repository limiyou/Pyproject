"""
count 统计出现的次数
"""
m_name="look forward to"
print(m_name.count("o"))

#replace 替换 replace("a被替换的','b替换成的')'
song="我爱你 你爱我 她爱我"
print(song.replace("爱" , "love"))


#split 切分 ，拼接
time_string="2020/09/03"
print(time_string.split("/"))
couple="I & U"
print(couple.split("&"))
#upper  大写
career="lawyer"
print(career.upper())
#lower 小写
gender="FEMALE"
print(gender.lower())
#strip 去掉两边的特殊字符，如果什么都不传就是去掉空格或者换行符
name=' li mi  you  '
print(name.strip())
print(name)
cp="@miyou@@lijing@"
print(cp.strip("@"))

"""#formate  字符串的格式化
-------------
借条
借款：小米
债权人：美的
金额：1亿
借款时间：2020/09/03
期限:一年
------
"""

#{}表示占坑符，占位符，用来表示一些变化的数据
#位置要匹配，顺序不能乱
loan_name='xiaomi'
Richman="meidi"
money=500


print(

    """
    --------------
    借条
借款：{}
债权人：{}
金额：{}万
------------
""".format(loan_name,Richman,money)
)

#f-string:python3.6以后支持，其功能与 format一样

print(f"""
    --------------
    借条
借款：{loan_name}
债权人：{Richman}
金额：{money}万
------------
""")
#len长度
print(len(loan_name))