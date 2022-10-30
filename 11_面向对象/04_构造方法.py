"""
构造方法

可以实现：__init_()方法，称之为构造方法。
在创建类对象（构造类）的时候/会自动执行。
在创建类对象（构造类）的时候/将传入参数自动传递给__init_()方法使用。

__init__()
	特性1：创建对象时会自动执行 stu = Student()
	特性2：自动接收创建对象时传的参数 stu = Student('Petter', '18', 'Male')
    特性3：可自动设置成员变量（成员变量的定义可省略）
"""


class Student:
    # name = None
    # tel = None
    # age = None
    sex = None

    def __init__(self, name, tel, age):
        self.name = name # 赋值，没定义就定义
        self.tel = tel
        self.age = age
        print('创建了Student对象')


stu = Student('Annie', '186888888889823', '19')
print(stu.name)
print(stu.sex)
