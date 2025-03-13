"""
题目：
    某公司，账户余额有1W元，给20名员工发工资。
要求：
    1.员工编号从1到20,从编号1开始,依次领取工资,每人可领取1000元
    2.领工资时，财务判断员工的绩效分（1-10） （随机生成），如果低于5，不发工资，换下一位
    3.如果工资发完了，结束发工资。
提示：
    随机数：
        import random
            num = random.randint(1,10)
"""
# 总工资
money = 10000
for x in range(1, 21):
    import random
    num = random.randint(1, 10)
    if num > 5:
        money -= 1000
        print(f"向员工{x}发放工资1000元，账户余额还剩{money}元")
        if money < 1000:
            print("工资发完了，等下个月吧")
            break
    else:
        print(f"员工{x}，绩效分{num}，低于5分，不发工资，下一位")
        continue
