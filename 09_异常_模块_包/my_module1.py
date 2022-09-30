def add(x, y):
    return x + y


def test(x, y):
    print(x + y)


# test(2, 3)  # 直接这样调用函数时，本py文件被其他py文件导入时会执行，怎么解决？如下

"""
内置变量：__name__
当右键运行本py文件时，变量 __name__ 的值就被赋值为 __main__ ，被导入时 则不会给变量 __name__赋值__main__，就不会进if
"""
if __name__ == '__main__': #右键运行时，可执行测试函数，外部导入时不会执行测试函数
    test(5, 5)
