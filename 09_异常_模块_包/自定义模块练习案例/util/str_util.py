# 字符串工具类

def str_reverse(s):
    """
    反转字符串
    :param s: 字符串
    :return: 字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    按照下标x和y，对字符串进行切片
    :param s:
    :param x: index x
    :param y: index y
    :return: 切片后的字符串
    """
    return s[x:y]


# 内部测试执行，被导入不会执行
if __name__ == '__main__':
    print(str_reverse('学习python'))
    print(substr('学习python', 1, 3))
