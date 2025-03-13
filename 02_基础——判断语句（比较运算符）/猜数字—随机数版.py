"""
案例需求：
    定义一个数字(1~10随机产生），通过3次判断来猜出来数字案例
要求：
    1.数字随机产生，范围1-10
    2.有3次机会猜测数字,通过3层嵌套判断实现
    3.每次猜不中，会提示大了或小了

    随机数代码提示：
        通过以下代码可以定义一个变量num，变量内 存储随机数字
        import random
        num = random.randint(1,10)
"""
# 创建一个1~10的随机数
import random
num = random.randint(1, 10)
print(num)
# 用户输入的数字
num_1 = int(input("请输入您猜想的数字："))
if num_1 == num:
    print("恭喜您猜对了")
else:
    if num_1 > num:
        print("你猜的数字太大了")
    else:
        print("你猜的数字太小了")
# 第二次猜数
    num_2 = int(input("请输入您第二次猜想的数字："))
    if num_2 == num:
        print("恭喜您猜对了")
    else:
        if num_2 > num:
            print("你猜的数字太大了")
        else:
            print("你猜的数字太小了")
# 第三次猜数
        num_3 = int(input("请输入您最后一次猜想的数字："))
        if num_3 == num:
            print("恭喜您猜对了")
        else:
            if num_3 > num:
                print("你猜的数字太大了")
            else:
                print("你猜的数字太小了")
            print(f"这个数字是：{num}")
