"""
写入操作
"""
#写入：write  w
#w模式比较危险，如果之前已有同名文件，用w会覆盖之前的内容
# with open ("demo.txt",mode='w',encoding="utf8")as f:
#     print(f.write("小hong"))

#todo:a add 追加模式
with open("demo.txt",mode='a',encoding="utf8")as f1:
    f1.write("李米柚啊aa ")
    f1.write("小米柚1")
    f1.write("小米柚2")
    f1.write("小米柚3")
with open('demo3.txt',mode='w',encoding='utf8')as f:
    f.write("i loveyou3")
    f.write("i love you baby")

