"""
理解继承的概念
掌握继承的使用方式
掌握pass关键字的作用
"""


class phone:
    IMEI = None  # 序列号
    producer = 'XIAOMI'  # 厂商
    __ele = 0  # 电量

    def call_by_4g(self):
        print('4g通话')


# 单继承
# 继承语法 class 类名(父类名):
class phone2022(phone):
    face_id = '30001'  # 面部识别

    def call_by_5g(self):
        print("2022最新5g通话")

    def call_by_4g(self):
        print('4g快速通话')


p = phone2022()
p.call_by_5g()
p.call_by_4g()
print(p.IMEI)
print(p.producer)
print(p.face_id)
print(p.__ele)  # 父类私有属性不能被继承


# 多继承
# 多继承语法 class 类名(父类名1,父类名2,父类名3....父类N):
class BasePone:
    IMEI = None  # 序列号
    producer = None  # 厂商

    def call_by_5g(self):
        print('5g通话')


class NFCReader:
    nfc_type = '第五代'
    producer = 'XIAOMI'

    def read_card(self):
        print('读取NFC卡')

    def write_card(self):
        print('写入NFC卡')


class RemoteControl:
    rc_type = '红外遥控'

    def control(self):
        print('红外遥控开启')


# 手机有： nfc 遥控器 手机等三个功能
class MyPhone(BasePone, NFCReader, RemoteControl):
    pass  # pass关键字功能：补全语法
