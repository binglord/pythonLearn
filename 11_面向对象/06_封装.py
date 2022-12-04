"""
面向对象3大特性：
1、封装：将现实世界的事物的属性和行为，转化为类的成员变量和成员方法。
    对用户开放的属性和行为：如手机的品牌、尺寸；上网、通话 => 公开的成员变量和方法
    对用户隐藏的属性和行为：如手机的电压、驱动信息；程序调度、内存管理 => 私有成员变量和方法：定义方法：名称前面加2下划线 __
2、继承
3、多态
"""


# 私有成员变量、成员方法
class Phone:
    IMEI = None  # 序列号
    producer = None  # 厂商

    __current_voltage = None  # 当前电压  私有成员变量

    __storage = 0 # 电量

    def call_by_5g(self,elec):
        self.__storage = self.__storage + elec
        __current_voltage = 4.5  # 私有成员在类内部可使用
        print('当前电压：' + str(self.__current_voltage))
        print('当前电量：' + str(self.__storage))
        if self.__storage >= 30:
            print('5G通话已开启')
        else:
            print('5G通话开启失败，电量不足！')

    # 私有成员方法
    def __keep_single_core(self):
        print('让CPU以单核运行以节省电量')

    def charge(self,elc):
        __storage = self.__storage + elc
        print(__storage)

p = Phone();
# p.call_by_5g()  # 5G通话已开启
# p.__keep_single_core() # AttributeError: type object 'Phone' has no attribute '__keep_single_core'
# p.call_by_5g()
p.call_by_5g(30)
