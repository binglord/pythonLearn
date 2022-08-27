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
#     # f = open("d:/999.txt", 'r', encoding='UTF-8')  # FileNotFoundError
#     print(name)  # NameError
# except Exception as e:  # 捕获第一次出现的异常ZeroDivisionError
#     print(e)
#     print(f'异常是：{type(e)}')
