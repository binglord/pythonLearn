money = 5000000

name = input("请输入姓名：")
func_code = None


# 查询余额
def query_remain_money():
    print(f"{name},您的余额是：{money}元")


# 存款
def add_money(yuan):
    global money
    money += yuan
    print(f"{name},您存入了{yuan}元，账户余额：{money}元")


# 取款
def get_money(yuan):
    global money
    if money >= yuan:
        money -= yuan
        print(f"{name},您取走了{yuan}元，账户余额：{money}元")
    else:
        print(f"{name},您的余额不足，账户余额：{money}元")


def main_func():
    print("------------------菜单------------------")
    global func_code
    func_code = input(f"尊敬的客户{name}，您好！请选择业务编号后回车\n"
                      f"1 - 查询余额\n"
                      f"2 - 存款\n"
                      f"3 - 取款\n"
                      f"4 - 退出\n"
                      f"请输入业务编号：")

    if 1 == int(func_code):
        print("------------------查询余额------------------")
        query_remain_money()
    elif 2 == int(func_code):
        print("------------------存款------------------")
        yuan = input(f"{name}您好，请输入存款金额：")
        add_money(int(yuan))
    elif 3 == int(func_code):
        print("------------------取款------------------")
        yuan = input(f"{name}您好，请输入取款金额：")
        get_money(int(yuan))
    elif 4 == int(func_code):
        print("------------------退出------------------")
        print(f"{name} 再见，欢迎下次再来！")
    else:
        print(f"非法的功能码：{func_code}")


while True:
    if "4" == func_code:
        break
    main_func()
