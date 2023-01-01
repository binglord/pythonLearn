class phone:
    IMEI = 123456 # 序列号
    producer = 'ITCAST' # 厂商

    def call_by_5G(self):
        print('5G第一版本')

# 定义子类，复写父类的属性和方法
class MyPhone(phone):
    IMEI = 653468
    producer = 'XiaoMi' # 复写父类属性

    def call_by_5G(self): # 复写父类方法
        print('5G第二版本')

phone = MyPhone()
print(phone.IMEI)
phone.call_by_5G()