"""
def关键字 定义的函数是带有名称的函数：可基于名称多次使用
lambda关键字可定义匿名函数：只可临时使用一次
    语法：lambda 传入参数 : 函数体(一行代码，无法写多行代码)
"""


def test_func(func):
    # print(func(6))
    # print(func(6, 6))
    print(func())


# test_func(lambda x: x * 2)#一个参数
# test_func(lambda x, y: x * y)  # 两个参数
test_func(lambda: print("你好"))  # 无参数 你好 None
