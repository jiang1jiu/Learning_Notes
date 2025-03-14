"""
目录：
    1.函数介绍
    2.函数的定义
    3.函数的参数
    4.函数的返回值（None类型）
    5.函数说明文档
    6.函数的嵌套调用
    7.变量的作用域
"""
"""
1.函数介绍
    定义：
        函数是组织好的，可重复使用的，用来实现特定功能的代码段
"""
"""
2.函数的定义
    语法：
        def 函数名（传入参数）：   #参数可省略     #形参
            函数体
            return 返回值     #返回值可省略
    调用语法：
        函数名（参数）       #参数可省略     #实参
    
    注意：
        函数必须先定义后使用
"""
# # 例子 创建函数
# def ni_hao():
#     print("你好")
# # 调用函数
# ni_hao()
"""
3.函数的参数
    功能：
        在函数进行计算的时候，接受外部（调用时）提供的数据
    注意：
        ·多个参数之间用逗号隔开
        ·传入参数的时候，按照顺序传入数据，用逗号隔开
"""
# # 例子
# def add(a,b):
#     result = a + b
#     print(f"{a}+{b}的结果是{result}")
# # 调用函数
# add(1, 2)
# add(3, 6)
"""
4.函数的返回值
    定义：
        返回值就是程序中函数完成事情后，最后给调用者的结果
    语法：
        def 函数名（参数）：
            函数体
            return 返回值
        接取返回值的语法
            变量 = 函数名（参数）
    （返回来的东西需要一个箱子装起来，变量就相当于是箱子)
    注意：
          return后的代码不会执行
"""
# 例子 接取返回值变量
# def add(x,y):
#     result = x + y
#     return result
# # 调用函数
# a = add(5,6)
# print(a)
"""
4.函数的返回值——None类型
    None表示：空的，无实际意义的意思
    函数返回None，就表示，这个函数没有返回什么有意义的内容。
    也就是返回了空的意思。
    
    无返回值函数，返回的内容就是None
    
    None类型的应用场景：
        None作为一个特殊的字面量，用于表示：空，无意义，其有很多的应用场景。
            1.用在函数无返回值上
            2.用在if判断上
                ·在if判断中，None等同于False
                ·一般用于在函数中主动返回None，配合if判断做出相关处理
            3.用于声明与内容的变量上
                ·定义变量，但暂时不需要变量有具体价值，可以用None来代替
                    #暂时不赋予变量具体意义
                    # name = None
"""
"""
5.函数说明文档
    函数是纯代码语言，想要理解其含义，就需要一行行的去阅读理解代码，效率比较低。
    我们可以给函数添加说明文档,辅助理解函数的作用。
    使用方法：
        通过多行注释的形式，对函数进行说明解释
            ·内容应写在函数体之前
        可以通过鼠标悬停，查看调用函数的说明文档
"""
# 例子
# def add(x, y):
#     """
#     add函数可以接收两个参数，进行两数相加减
#     :param x: 形参x表示相加的其中一个数字
#     :param y: 形参y表示相加的另一个数字
#     :return: 返回值是两数相加的结果
#     """
#     result = x + y
#     return result
# a = add(5,6)    # 鼠标悬停查看调用函数的说明文档
"""
6.函数的嵌套调用
    定义：
        所谓函数嵌套调用指的是一个函数里面又调用了另外一个函数
    执行流程：
        如果函数A中,调用了另外一个函数B,
        那么先把函数B中的任务都执行完毕之后才会回到上次函数A执行的位置
"""
# 例子

# 定义函数b
def b():
    print("----2----")

# 定义函数a
def a():
    print("----1----")

# 嵌套调用函数b
    b()

    print("----3----")
# 调用函数a
a()
"""
7.变量的作用域
    变量作用域指的是变量的作用范围(变量在哪里可用,在哪里不可用)
    主要分为两类:局部变量和全局变量
        局部变量：
            定义在函数体内部的变量，即只在函数体内部生效
        局部变量的作用:
            在函数体内部,临时保存数据,即当函数调用完成后,则销毁局部变量
            
        全局变量：
            指的是在函数体内、外都能生效的变量
    global关键字
        使用 global关键字 可以在函数内部声明变量为全局变量
"""
# 例子 global关键字
num = 100
def a():
    global num     # 把局部变量转换为全局变量
    num = 200
    print(num)

a()
print(num)















