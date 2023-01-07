import json
import random
"""
变量的类型注解
"""


# 基础数据类型注解
var_1: int = 10
var_2: float = 12.32
var_3: bool = True
Var_4: str = 'Annie'

# 类对象类型注解
class Student:
    pass

stu: Student = Student()

# 基础容器类型注解
my_list: list = [1,2,3]
my_tuple: tuple = (1,2,3)
my_dict: dict = {"Annie", 23}

# 容器类型详细注解
my_list: list[int] = [1,2,3]
my_tuple: tuple[int,str,bool,float] = (1,'Annie',True,4.23) # 每个元素都要注解类型
my_dict: dict[str,int] = {"Annie", 23}

# 在注释中进行类型注解
var_4 = random.randint(1,10) # type: int
print(var_4)
var_5 = json.loads('{"name": "Annie","age": 23}') # type: dict[str,str]
print(var_5)

def func():
    return 10
#对函数返回值做注释类型注解
var_6 = func() # type: int

# 类型注解的限制
var_7: int = 'petter'
var_8: str = 123
# 以上代码可运行，类型注解只是给开发者提示用，不是强制。哪怕标记错了，也不会影响程序运行