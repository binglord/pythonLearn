def fun_02():
    print('fun_02开始')
    1 / 0  # 异常没被捕获就会往上级调用传递
    print('fun_02结束')


def fun_01():
    print('fun_01开始')
    fun_02()  # 异常没被捕获就会往上级调用传递
    print('fun_01结束')


def main():
    # fun_01()
    try:
        fun_01()
    except Exception as e:  # 捕获异常
        print(f'出现异常：{type(e)},{e}')


# main()
"""
fun_01开始
fun_02开始
出现异常：<class 'ZeroDivisionError'>,division by zero
"""


# 触发异常 raise
def function_name(level):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行


function_name(0)

# 用户自定义异常

# 异常的参数
