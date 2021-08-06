"""
不定长参数 * **
# * *args
当在一个形式参数的前面加一个*号，它会收集所有剩下没有配对的实际参数的位置参数
"""
"""def add(a,*b):
    print(f"a为：{a}")
    print(f"b为：{b}")
add(3,4)
add(3,4,5,6) #a为3，b为（4,5,6）
"""

# def add(c,*d,e=3,):
#     print(f"c为：{c}")
#     print(f"d为：{d}")
# add(3,4)
# add(3,4,5,6,7) #c为3，d为（4,5,6）


def add(a,*c,b=3):
    print(f"a为：{a}")
    print(f"c为：{c}")

add(5,6)
add(4,7,7,9,10)

