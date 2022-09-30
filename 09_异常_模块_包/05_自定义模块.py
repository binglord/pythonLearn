# 导入自定义模块
# import my_module1 as mm1
#
# sum = mm1.add(2, 3)
# print(sum)

# from my_module1 import add
#
# sum = add(2, 3)
# print(sum)

# 导入不同模块的相同功能
# from my_module1 import add  # 被覆盖
# from my_module2 import add  # 最后一个生效
#
# sum = add(5, 6)
# print(sum)

# __main__变量
# import my_module1
# 输出了5，为什么？因为导入了某个模块，会执行这个模块的代码。解决办法：在my_module1里 if __name__ == '__main__':

"""
__all__变量
被导入模块里定义此变量：__all__ = ['add', 'm']
import * 时，只能使用指定的资源。* 的值取自于__all__变量
"""
from my_module2 import *
add(2,3)
m(5,7)

