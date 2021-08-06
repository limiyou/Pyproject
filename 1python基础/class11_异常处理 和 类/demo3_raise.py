"""
raise 主动抛出异常
"""

def adult_add(a,b):
    """两数想加，a,b一定要大于18，否则不能运行"""
    if (a<18)or (b<18):
        raise  ValueError("参数必须大于18")
    c=a+b
    return c
adult_add(3,4)
print("函数执行完成")# 这一句，不会执行