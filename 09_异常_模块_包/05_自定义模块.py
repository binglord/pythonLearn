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
from my_module1 import add  # 被覆盖
from my_module2 import add  # 最后一个生效

sum = add(5, 6)
print(sum)

# __main__变量

# __all__变量
