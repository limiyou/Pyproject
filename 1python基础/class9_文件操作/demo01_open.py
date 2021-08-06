"""
#open()打开文件

#去看一些日志,文件
.txt

open("文件路径)
"""
#打开文件
# f=open ('python32.txt')
# #f表示文件
# #f.read()表示读取里面的内容
# print(f.read())
# #print(open("python32.txt").read()) 简单版
# #TODO:打开文件后，一定要关闭文件
# f.close()
#用一个with 语句
with open(("python32.txt")) as f:
    print(f.read())
with open("python32.txt")  as f1:
    print(f1.read())