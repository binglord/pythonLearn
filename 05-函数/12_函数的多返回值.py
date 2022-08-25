"""
函数的多返回值
"""


def test():
    return 11, "hello", True


num, str, b = test()

print(num)
print(str)
print(b)
