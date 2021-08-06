"""1、.删除如下列表中的"矮穷丑"，写出 2 种或以上方法：

info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
"""
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
info.remove("矮穷丑")
print(info)
info.insert(3,["矮穷丑"])
print(info)
info.pop(3)
print(info)
info.append("矮穷丑")
print(info)
del info[-1]
print(info)