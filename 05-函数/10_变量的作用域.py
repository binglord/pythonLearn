"""
函数内部变量作用域
"""


# 局部变量：在函数外部无效
def test_a():
    num = 17  # 在函数内部有效
    print(num)


test_a()
# print(num) #NameError: name 'num' is not defined

# 全局变量
num_2 = 200


def test_b():
    print(num_2)


def test_c():
    print(num_2)


test_b()
test_c()
print(num_2)


# 函数内修改全局变量的值：不行
def change_global_value(number):
    num_2 = number  # 这里的num_2是一个新的局部变量，不是上面的全局变量num_2


change_global_value(300)
print(num_2)  # 200，无法修改


# global 在函数内改全局变量值、定义新的全局变量
def test_d():
    global num_2
    global num_3
    num_3 = 700
    num_2 = 600


test_d()
print(num_2)
print(num_3)


def test_e():
    print(num_3)


test_e()
