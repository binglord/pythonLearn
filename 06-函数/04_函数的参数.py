def add(x,y):
    result = x + y
    print(f"{x} + {y} 的结果是{result}")

add(5,4)

def passed(temp):
    if temp < 37.5:
        print("温度正常")
    else:
        print("温度异常")

passed(37)