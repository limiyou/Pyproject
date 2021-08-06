""""
字符串操作"""

name="miyou"
family_name='Li'
print(name + family_name)
print(name +' ' + family_name )
#字符串和数字能相加
print("miyou"+ str(7))
#数据类型的转换：
str()
list()
dict()
bool()
int()
float()

print(int("12"))

# 字符串换行: 三引号 换行，获得多行数据
#\不会分开
name6="""miyou 
  i 
  love 
  you
  """
print(name6)
#单引号当中\n表示换行
name7 = 'xiaomiyou \n i \n love\n you'
print(name7)