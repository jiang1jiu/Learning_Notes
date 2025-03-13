# def outer(logo):
#     """
#     创建一个闭包函数，用于在消息周围添加特定的标志。
#
#     参数:
#     logo - 将被添加到消息周围的标志。
#
#     返回:
#     一个闭包函数，它接受一个消息参数，并打印带有标志的消息。
#     """
#
#     def inner(msg):
#         """
#         打印带有标志的消息。
#
#         参数:
#         msg - 需要被标志包围的消息。
#         """
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
#
# # 创建一个带有特定标志的闭包函数
# fn1 = outer("我")
# # 使用闭包函数打印带有标志的消息
# fn1("你")

def outer(num1):
    """
    外部函数，接收一个参数num1。
    :param num1: int 初始值，将在此函数基础上进行累加。
    :return: 返回内部函数inner，以便外部调用。
    """
    def inner(num2):
        """
        内部函数，用于累加num1和num2。
        :param num2: int 需要累加的值。
        """
        # nonlocal作用：
        #   当内部函数需要修改外部函数中的变量时，必须使用nonlocal 关键字来声明该变量。
        #   否则，Python会认为你是在创建一个新的局部变量，而不是修改外部的变量
        nonlocal num1  # 声明num1不是局部变量，而是外部函数outer定义的变量。
        num1 += num2  # 将num2的值累加到num1上。
        print(num1)  # 打印累加后的num1值。

    return inner  # 返回内部函数inner的引用。


fn1 = outer(10)  # 调用外部函数outer，并传入初始值10，得到内部函数的引用赋值给fn1。
fn1(10)  # 通过fn1调用内部函数，传入值10进行累加。
fn1(10)  # 再次调用内部函数，传入值10进行累加。



