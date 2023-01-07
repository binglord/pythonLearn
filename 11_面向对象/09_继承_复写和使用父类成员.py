class Phone:
    IMEI = 123456 # 序列号
    producer = 'ITCAST' # 厂商

    def call_by_5G(self):
        print('使用5G网络进行通话')

# 定义子类，复写父类的属性和方法
class MyPhone(Phone):
    IMEI = 653468
    producer = 'XiaoMi' # 复写父类属性

    IMEISuper = Phone.IMEI # 在子类中调用父类成员
    producerSuper = Phone.producer # 在子类中调用父类成员

    # IMEISuper2 = super().IMEI # RuntimeError: super(): no arguments
    # producerSuper2 = super().producer # RuntimeError: super(): no arguments

    def call_by_5G(self): # 复写父类方法：功能升级了，实现|复写父类方法
        print('CPU开启单核模式，通话时省电')
        # print('使用5G网络进行通话') 无需重写，复用父类方法即可
        Phone.call_by_5G(self)
        # super().call_by_5G()
        print(super().IMEI)
        print(Phone.IMEI)
        print('关闭单核模式，确保性能')

phoneInstance = MyPhone()
print(phoneInstance.IMEI)
phoneInstance.call_by_5G()

'''
在子类中 调用父类成员：
    子类复写父类成员后，调用时默认使用复写后的成员，怎么调用父类成员？
    方法1:
        使用成员变量：父类名.成员变量
        使用成员方法：父类名.成员方法（self）
    方法2:
        使用成员变量：super().成员变量
        使用成员方法：super().成员方法()
'''
print('===============在子类中调用父类成员===================')
print(phoneInstance.IMEISuper) # 123456
print(phoneInstance.producerSuper) # ITCAST
phoneInstance.call_by_5G()
# 5G第二版本
# 父类call_by_5G_way1：5G第一版本
# 父类call_by_5G_way2：5G第一版本