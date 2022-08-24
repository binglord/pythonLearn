str1 = "apple"
str2 = "xiaoMi"
str3 = "HuaWei"

print(len(str1))
print(len(str2))
print(len(str3))

def my_len(data):
    count = 0
    for i in data:
        count += 1
    return count

print(my_len(str1))
print(my_len(str2))
print(my_len(str3))

