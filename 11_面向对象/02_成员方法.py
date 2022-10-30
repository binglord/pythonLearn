# 定义含有成员方法的类
class Student:
    name = None  # 姓名

    def say_hi(self):  # 成员方法必须有self参数
        print(f'大家好，我是{self.name}，请大家多多关照')  # 成员方法内部要用成员变量要用 self.成员变量 这样的格式

    def say_hi2(self, msg):
        print(f'大家好，我是{self.name},{msg}')


stu1 = Student()
stu1.name = 'Petter'
stu1.say_hi()  # 调用的时候，把 self 参数当做不存在

stu2 = Student()
stu2.name = 'Annie'
stu2.say_hi()  # 调用的时候，把 self 参数当做不存在


stu3 = Student()
stu3.name = 'Bruce'
stu3.say_hi2('有事找我！')
