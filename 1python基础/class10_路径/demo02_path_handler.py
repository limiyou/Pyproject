"""
路径获取
"""
#获取绝对路径

import os
abs_path=os.path.abspath(__file__)  #__file__表示运行的文件的名称
print(abs_path)


#后去获取文件的目录路径

dir_name=os.path.dirname(abs_path)
print(dir_name)


#打开pac01下的demo.txt,如何获取demo.txt的绝对路径
   #1、先获取当前文件的绝对路径
   #2、获取当前文件的目录路径
   #3、当前文件的目录路径和pac01拼接

abs_path=os.path.abspath(__file__)
dir_name=os.path.dirname(abs_path)
path_demo=dir_name +("class10_路径。pac01")
