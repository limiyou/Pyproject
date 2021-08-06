"""打开一个文件"""
import  io
try:
    f=open("demo.py",'a')
    print(f.read())
except io.UnsupportedOperation as e:
    print('文件读取失败')
finally:
    f.close()
