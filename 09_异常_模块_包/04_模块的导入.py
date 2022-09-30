"""
模块：就是一个py文件
语法

[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
"""

"""
常用组合

import 模块名
import 模块名 as 别名
from 模块名 import 类、变量、方法等
from 模块名 import *
from 模块名 import 功能名 as 别名
"""

# 导入time模块，使用sleep函数

# ipmort
# import time
# print('a')
# time.sleep(3)
# print('b')

# import *
# from time import *
# print('a')
# sleep(3)
# print('b')

#导入一个函数、功能、变量
# from time import sleep
# print('a')
# sleep(3)
# print('b')

# as 别名
# import time as t
# print('a')
# t.sleep(3)
# print('b')

# 导入一个函数、功能、变量 as
from time import sleep as s
print('a')
s(3)
print('b')
