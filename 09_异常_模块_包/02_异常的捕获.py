# 捕获异常
# try:
#     f = open("d:/678.txt", 'r', encoding='UTF-8')
# except:  # 捕获所有类型异常
#     print('有异常！文件不存在，用w模式打开')  # 有异常！
#     f = open('d:/678.txt', 'w', encoding='UTF-8')

# 捕获指定异常 ZeroDivisionError
# try:
#     1 / 0  # ZeroDivisionError: division by zero
#     f = open("d:/999.txt", 'r', encoding='UTF-8')
# except ZeroDivisionError as e:  # 只捕获了异常ZeroDivisionError
#     print(e)
#     print(f'异常是：{type(e)}')

# 捕获多个异常:用元组列出要捕获的异常类型，如果有异常没包含在元组里，还是会报异常，进而程序停止运行
# try:
#     # 1 / 0  # ZeroDivisionError: division by zero
#     f = open("d:/999.txt", 'r', encoding='UTF-8')  # FileNotFoundError
#     # print(name)  # NameError
# except (ZeroDivisionError, ZeroDivisionError, FileNotFoundError, NameError) as e:
#     print(e)
#     print(f'异常是：{type(e)}')

# 捕获所有异常 Exception as e
# try:
#     # 1 / 0  # ZeroDivisionError: division by zero
#     f = open("d:/999.txt", 'r', encoding='UTF-8')  # FileNotFoundError
#     # print(name)  # NameError
# except Exception as e:  # 捕获第一次出现的异常ZeroDivisionError
#     print(e)
#     print(f'异常是：{type(e)}')

# 异常else
# try:  # 尝试捕获异常
#     print('0')
#     # print(age)
# except Exception as e:  # 出现异常了执行
#     print(f'出现异常：{type(e)},{e}')
# else:  # else可选。没出现异常执行
#     print('没出现异常')

# 异常的finally
try:  # 尝试捕获异常
    # print('0')
    # print(age)
    f = open('d:/000.txt', 'r', encoding='UTF-8')
except Exception as e:  # 出现异常了执行
    f = open('d:/000.txt', 'w', encoding='UTF-8')
    print(f'出现异常：{type(e)},{e}')
else:  # else可选。没出现异常执行
    print('没出现异常')
finally:  # 最终都会执行，无论出现异常没有。常用于关闭文件、资源。
    f.close()
    print('程序结束')
