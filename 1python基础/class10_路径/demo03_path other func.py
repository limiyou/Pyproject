#获取文件夹的固定写法
import os
current_file_path=os.path.abspath(__file__)
dir_name=os.path.dirname(current_file_path)
#或者
dir_name=os.path.dirname(os.path.abspath(__file__))
print(dir_name)