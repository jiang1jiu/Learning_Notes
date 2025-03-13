"""
题目：
    定义一个全局变量: money,用来记录银行卡余额(默认5000000)
    定义一个全局变量: name,|用来记录客户姓名(启动程序时输入)
    定义如下的函数：
        ·查询余额函数
        ·存款函数
        ·取款函数
        ·主菜单函数
要求：
    ·程序启动后要求输入客户姓名
    ·查询余额、存款、取款后都会返回主菜单
    ·存款、取款后，都应显示一下当前余额
    ·客户选择退出或输入错误，程序会退出，否则一直运行
"""
money = 0
name = input("请输入账户名称：")
# 主菜单
def menu():
    print("------------主菜单------------")
    print(f"尊敬的{name}您好，欢迎使用本ATM机")
    print(f"请选择操作:")
    print("查询余额\t【请按1】")
    print("进行存款\t【请按2】")
    print("进行取款\t【请按3】")
    print("退出程序\t【请按4】")
    num = int(input("请输入您的选择："))
    if num == 1:
        balance()
    else:
        if num == 2:
            saving()
        else:
            if num == 3:
                take()
            else:
                return print("已退出...")
# 查询余额
def balance():
    print("------------查询余额------------")
    print(f"尊敬的{name}您好，您账户所剩余额为{money}元")
    menu()
# 存款
def saving():
    print("------------存款------------")
    num = int(input("请输入您要存入的金额："))
    global money
    money += num
    print(f"以为您存入{num}元，您账户剩余{money}元")
    menu()
# 取款
def take():
    print("------------取款------------")
    num = int(input("请输入您要取出的金额："))
    global money
    if num <= money:
        money -= num
        print(f"以为您取出{num}元，您账户剩余{money}元")
        menu()
    else:
        print(f"抱歉您的余额好像并没有这么多，账户剩余{money}元")
        menu()
# 调用函数
menu()