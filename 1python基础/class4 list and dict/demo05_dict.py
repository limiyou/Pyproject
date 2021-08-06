"""
字典：{key1:value1,key2:value2...}
可以增删改查
可以存储多个数据

能够表示元素更具体的意义

key是有要求的，key不可以重名，
key是不能变的，列表是不能作为key的
"""
#列表：当每个元素有具体的意义，但是又想单独获取时，可读性不强
beisheng=["星际穿越","蜘蛛侠","上海堡垒","分手大师","前任3"]
print(beisheng[2])
#字典：key 元素的名称，value：元素的值；即 键值对
#key1:value1,key2:value2....

beisheng={"favor":"星际穿越","hate":"蜘蛛侠","first":"上海堡垒","last":"分手大师","twice":"前任3"}
print(beisheng["hate"])

#c重名的key
beisheng={"favor":"星际穿越",
          "hate":"蜘蛛侠",
          "first":"上海堡垒",
          "favor":"分手大师",
          "twice":"前任3"}

#后面的值会覆盖前面的
print(beisheng["favor"])
print(beisheng)


#key不能是列表,一般采用字符串的形式表示
"""beisheng={"favor":"星际穿越",
          ["hate"]:"蜘蛛侠",
          "first":"上海堡垒",
          "favor":"分手大师",
          "twice":"前任3"}
print(beisheng)"""
