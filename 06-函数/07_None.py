# None是类型<class 'NoneType'>的字面量
# 主动返回None
def say_hi():
    print("你好")
    return None


print(f"结果内容：{say_hi()}")
print(f"结果内容类型：{type(say_hi())}")


# 用于if判断，表示false
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None


result = check_age(17)
if not result:
    print("未成年人禁止进入")

# 声明无内容变量
name = None
print(name)
