def test(name, age, gender):
    print(f"姓名：{name},年龄：{age},性别：{gender}")


# 1-位置参数：按顺序
test("小明", 19, "男")

# 2-关键字参数：键值对
test(name="petter", age=18, gender="男")
# 可以不按顺序
test(gender="男", name="petter", age=18)
# 位置参数和关键字参数混用
test("Annie", 17, gender="女")


# 位置参数在关键字参数前
# test("Annie", age=17, "女")  # SyntaxError: positional argument follows keyword argument

# 3-缺省参数
def test_a(name, age, gender="女"):
    print(f"姓名：{name},年龄：{age},性别：{gender}")


# 缺省参数可赋值可不赋值
test_a("Annie", age=20)
test_a("Annie", 20, "女")


# 缺省参数必须在非缺省参数后
# def test_a(name="小李", age, gender="女"): # non-default parameter follows default parameter
#     print(f"姓名：{name},年龄：{age},性别：{gender}")

# 4-不定长（可变）参数：可不传参
# 位置传递不定长
def user_info(*args):  # args形参可接收不定长参数：多个或0个. args为元组类型
    print(args)
    print(type(args))  # <class 'tuple'>


user_info()  # ()
user_info(90)  # (90,)
user_info(90, 90, True, "hello")  # (90, 90, True, 'hello')


# 关键字传递不定长
def user_action(**kwargs):  # kwargs(key - word)形参可接收不定长参数：多个或0个. args为字典类型
    print(kwargs)
    print(type(kwargs))  # <class 'dict'>


user_action()  # {}
user_action(name="Tom")  # {'name': 'Tom'}
user_action(name="Tom", age=19, gender='男')  # {'name': 'Tom', 'age': 19, 'gender': '男'}
