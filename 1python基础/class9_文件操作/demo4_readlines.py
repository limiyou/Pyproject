"""
读取的另外两个方式：

readline  readlins
"""

#readline 读取第一行
with open("demo.txt ",encoding='utf8')as f:
    print(f.readline())

#readlins  #读取多行,一列表的形式得到且可以展示出换行符
with open("demo.txt",encoding="utf8") as f1:
    print(f1.readlines())