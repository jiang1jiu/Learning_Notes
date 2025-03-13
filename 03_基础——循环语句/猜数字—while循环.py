"""
题目：
    设置一个范围1-100的随机整数变量，
    通过while循环，配合input语句，
    判断输入的数字是否等于随机数
要求：
    1.无限次机会，直到猜中为止
    2.每一次猜不中,会提示大了或小了
    3.猜完数字后，提示猜了几次

     随机数代码提示：
        通过以下代码可以定义一个变量num，变量内 存储随机数字
        import random
        num = random.randint(1,100)
"""
# 设置随机数
import random
num = random.randint(1, 100)
# 通过一个布尔类型变量，做循环是否继续的标记
flag = True
# 定义一个初始变量记录用户猜了几次
i = 0
while flag:

    num_1 = int(input("请输入一个数字:"))
    # 进行计算用户猜的次数
    i += 1
    # 通过if来判断
    if num_1 == num:
        print("你猜对了")
        flag = False
    else:
        if num_1 > num:
            print("你猜大了")
        else:
            print("你猜小了")

print(f"你猜了{i}次就猜到了")


