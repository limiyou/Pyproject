""""

字符串常用方法join

"""
name='li shi lan'
#字符串拼接:使用前面的内容对后面的内容进行拼接
#Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
print(name.join("h"))
print(name.join(["aa",'bb','cc']))
#时间['2002','09','03']用/连接
date=['2020','09','03']
print("/".join(['2020','09','03']))#==print("2020)+"/"+'09'+'/'+'03')






#find：在字符串当中查找某个字符或者子字符串的位置
a="lihongpeng"
print(a.find('g')) # = index=a.find('g')
#如果找的字符有两个，回得到第一个字符的位置
print(a.find('n'))

#如果是一个子串，则会显示第一个字符的位置
print(a.find("ng"))

#如果找不到，则会返回-1
print(a.find('w'))
#如果子串不在一起，则会返回-1
print(a.find("hp"))

#index约等于 find,区别：index找不到元素会报错，find 找不到会返回-1
print(a.index('ng'))
print(a.find("ng"))