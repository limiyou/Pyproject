"""
TODO:当要打开的文件有中文，或者非英文格式时，需要用 open 函数，encoding 关键字参数
编码格式：utf-8进行编译

"""
with open("python321.txt",encoding="utf8") as f:
    print(f.read())

with open("flask.png",mode="rb") as f1:  #以二进制的形式打开
    print(f1.read())