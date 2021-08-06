#import sys 是python去查找包或模块的搜索路径
#在哪运行的脚本，就要从当前目录打开项目

#找模块：1、项目开始的根目录
        #2、python内置目录，不建议从内置目录查找，因为python目录主要存放外部的库或者第三方的库
#TODO：如果模块导入不了，可以使用sys.path


import sys
from class10_路径.pac01 import module02
print(module02.a)  #
print(sys.path)