"""
类和对象的关系，面向对象编程思想
"""


# 设计闹钟类
class Clock:
    id = None  # 序列号
    price = None  # 价格

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)  # 2000频率 3000响声持续时间


# 构建2个闹钟对象，让其工作
c1 = Clock()
c1.id = 12341234
c1.price = 58.8
print(f'闹钟1，id是{c1.id},价格是{c1.price}')
c1.ring()

c2 = Clock()
c2.id = 434234234
c2.price = 68.8
print(f'闹钟1，id是{c2.id},价格是{c2.price}')
c2.ring()
