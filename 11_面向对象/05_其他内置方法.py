class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


stu1 = Student('Annie', 19, 'Female')
print(stu1)  # <__main__.Student object at 0x0000028B3BCCDE80>
print(str(stu1))  # <__main__.Student object at 0x0000028B3BCCDE80>


# 为类定义__str__方法
class Dog:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return f'本类是Dog类，name={self.name},sex={self.sex},age={self.age}'


dog = Dog('puppy', 'male', 1)
print(dog)  # 本类是Dog类，name=puppy,sex=male,age=1
print(str(dog))  # 本类是Dog类，name=puppy,sex=male,age=1


# __lt__ 小于方法
class Box:
    def __init__(self, lenght, color):
        self.lenght = lenght
        self.color = color

    # 小于
    def __lt__(self, other):  # other 表示另一个对象
        return self.lenght < other.lenght  # 定义比较 lenght 变量

    # 小于等于
    def __le__(self, other):
        return self.lenght <= other.lenght

    # 等于。没实现__eq__()就是比较内存地址
    def __eq__(self, other):
        return self.lenght == other.lenght


b1 = Box(200, 'red')
b2 = Box(300, 'yellow')
# 类需要实现 __lt__() 方法才能比较
print(b1 < b2)  # True
print(b1 <= b2)  # True
print(b1 == b2)  # False
