# 文件处理工具类

def print_file_info(file_name):
    """
    接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
    :param file_name:文件路径
    :return:文件内容
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(f"出现异常：{e}")
    finally:
        if f:  # 如果f是None，表示False，否则就是True
            f.close()


def append_to_file(file_name, data):
    """
    将数据追加写入文件
    :param file_name: 文件路径
    :param data: 传入参数
    :return: 新文件
    """
    f = open(file_name, 'a', encoding='UTF-8')
    f.write(data)
    f.write('\n')
    f.close()  # 带有flush功能，会把内存里数据flush进文件里


if __name__ == '__main__':
    print_file_info("C:\\Users\\Administrator\\Desktop\\新建 文本文档.txt")
    print_file_info("C:\\Users\\Administrator\\Desktop\\新建文本文档.txt")
    append_to_file("C:\\Users\\Administrator\\Desktop\\新建 文本文档.txt", '追加的内容')
    print_file_info("C:\\Users\\Administrator\\Desktop\\新建 文本文档.txt")
