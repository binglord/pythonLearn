"""
包：就是文件夹，里面有多个模块
组成：多个模块 + __init__.py
__init__.py文件存在，就在一个包，没有，就是一个普通的文件夹
"""

"""
导入自定义包，使用里面的函数
"""
# import my_package.my_module1 as mm1
# import my_package.my_module2 as mm2
#
# mm1.print_info1()
# mm2.print_info2()

# from my_package import my_module1
# from my_package import my_module2
# my_module1.print_info1()
# my_module2.print_info2()

# from my_package.my_module1 import print_info1
# from my_package.my_module2 import print_info2
# print_info1()
# print_info2()

"""
__all__变量控制能导入哪个模块，在__init__.py文件里定义
"""
from my_package import *
my_module1.print_info1()
my_module2.print_info2()
