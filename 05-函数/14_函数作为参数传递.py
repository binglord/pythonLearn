def compute(x, y):  # 数据不确定，逻辑确定
    return x + y


# 函数作为参数
def test_function(func):
    print(compute(3, 4))  # 调用compute函数
    print(type(func))  # <class 'function'>
    print(func(1, 2))  # 函数作为参数：逻辑不确定，数据确定
    print(type(func))  # <class 'function'>


test_function(compute)  # 计算逻辑的传递，而非数据参数的传递
