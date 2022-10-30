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
