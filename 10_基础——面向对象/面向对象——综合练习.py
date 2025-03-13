"""
题目：
    1：创建一个简单的类
    2：继承和多态
    3：封装和私有属性
    4：类方法和静态方法
    5：多重继承
    6：属性装饰器  未学到
"""
"""
1：创建一个简单的类
    题目：
        创建一个名为 Dog 的类，包含属性 name 和 age，以及方法 bark()，
        该方法打印出狗的名字和年龄。
"""
# class Dog:
#     """
#     Dog类提供了有关狗的信息，包括名字和年龄。
#     """
#     def __init__(self, name, age):
#         """
#         初始化Dog类的实例。
#
#         参数:
#         name (str): 狗的名字。
#         age (int): 狗的年龄。
#         """
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         """
#         打印狗的名字和年龄信息。
#         """
#         print(f"狗的名字是{self.name},年龄是{self.age}")
#
#
# # 创建Dog类的一个实例，名字设置为"旺财"，年龄设置为10。
# dog = Dog("旺财", 10)
# # 调用实例的bark方法来打印狗的信息。
# dog.bark()


"""
2：继承和多态
    题目：
        创建一个基类 Animal，包含方法 speak()。然后创建两个子类 Dog 和 Cat，
        分别重写 speak() 方法，使其输出不同的声音。
"""
# 定义一个动物类，作为后续狗和猫类的父类
# class Animal:
#     # 定义了一个 speak 方法，用于子类重写，本类中不实现具体逻辑
#     def speak(self):
#         pass
#
# # 定义狗类，继承自动物类
# class Dog(Animal):
#     # 重写 speak 方法，使狗类能够发出特定的声音
#     def speak(self):
#         print("狗会汪汪汪")
#
# # 定义猫类，继承自动物类
# class Cat(Animal):
#     # 重写 speak 方法，使猫类能够发出特定的声音
#     def speak(self):
#         print("猫会喵喵喵")
#
#
# # 创建狗和猫的实例
# dog = Dog()
# cat = Cat()
# # 调用实例的 speak 方法，输出对应的声音
# dog.speak()
# cat.speak()


"""
3：封装和私有属性
    题目：
        创建一个类 BankAccount，包含私有属性 __balance，
        并提供方法 deposit() 和 withdraw() 来修改余额。确保余额不能为负数。
"""
# class BankAccount:
#     def __init__(self, __balance=0):
#         self.__balance = __balance
#
#     def deposit(self, money):
#         if money > 0:
#             self.__balance += money
#         else:
#             print("存款金额必须为正数")
#
#     def withdraw(self, money):
#         if 0 < money <= self.__balance:
#             self.__balance -= money
#         else:
#             print("无效提现金额")
#
#     def get__balance(self):
#         return self.__balance
#
#
# bankAccount = BankAccount(100)
# bankAccount.deposit(50)
# bankAccount.withdraw(50)
# print(f"当前余额是{bankAccount.get__balance()}")


"""
4：类方法和静态方法
    题目：
        创建一个类 MathOperations，
        包含一个类方法 add() 和一个静态方法 multiply()，分别用于加法和乘法运算。
"""
# class MathOperations:
#     """
#     MathOperations类提供了加法和乘法运算的方法。
#     """
#
#     @classmethod
#     def add(cls, a, b):
#         """
#         执行两个数字的加法运算。
#
#         参数:
#             a: 第一个数字。
#             b: 第二个数字。
#
#         返回:
#             两个数字的和。
#         """
#         return a + b
#
#     @staticmethod
#     def multiply(a, b):
#         """
#         执行两个数字的乘法运算。
#
#         参数:
#             a: 第一个数字。
#             b: 第二个数字。
#
#         返回:
#             两个数字的乘积。
#         """
#         return a * b
#
#
# # 调用MathOperations类的add类方法计算4和5的和
# add = MathOperations.add(4, 5)
# # 调用MathOperations类的multiply静态方法计算4和5的乘积
# nul = MathOperations.multiply(4, 5)
# print(add)
# print(nul)


"""
5：多重继承
    题目：
        创建一个基类 Person，包含属性 name 和方法 introduce()。
        然后创建两个子类 Student 和 Teacher，分别继承 Person 并添加各自的属性和方法。
        最后创建一个类 TeachingAssistant，继承自 Student 和 Teacher。
"""
# class Person:
#     """
#     定义一个基本的Person类，包含一个名字属性和一个打印名字的方法。
#     """
#     def __init__(self, name):
#         """
#         初始化Person类的实例。
#
#         参数:
#         name (str): 人物的姓名。
#         """
#         self.name = name
#
#     def i(self):
#         """
#         打印人物的名字。
#         """
#         print(f"我的名字是{self.name}")
#
# class Student(Person):
#     """
#     定义一个Student类，继承自Person类，增加年龄属性和相应的打印方法。
#     """
#     def __init__(self, name, age):
#         """
#         初始化Student类的实例。
#
#         参数:
#         name (str): 学生的姓名。
#         age (int): 学生的年龄。
#         """
#         Person.__init__(self, name)
#         self.age = age
#
#     def e(self):
#         """
#         打印学生的名字和年龄。
#         """
#         print(f"我的名字是{self.name},年龄是{self.age}")
#
# class Teacher(Person):
#     """
#     定义一个Teacher类，继承自Person类，增加身高属性和相应的打印方法。
#     """
#     def __init__(self, name, height):
#         """
#         初始化Teacher类的实例。
#
#         参数:
#         name (str): 老师的姓名。
#         height (int): 老师的身高。
#         """
#         Person.__init__(self, name)
#         self.height = height
#
#     def w(self):
#         """
#         打印老师的名字和身高。
#         """
#         print(f"我的名字是{self.name},身高是{self.height}")
#
# class TeachingAssistant(Student, Teacher):
#     """
#     定义一个TeachingAssistant类，同时继承自Student和Teacher类，包含名字、年龄、身高和体重属性。
#     """
#     def __init__(self, name, age, height, weight):
#         """
#         初始化TeachingAssistant类的实例。
#
#         参数:
#         name (str): 助教的姓名。
#         age (int): 助教的年龄。
#         height (int): 助教的身高。
#         weight (int): 助教的体重。
#         """
#         Student.__init__(self, name, age)
#         Teacher.__init__(self, name, height)
#         self.weight = weight
#
#     def introduce(self):
#         """
#         打印助教的综合信息，包括名字、年龄、身高和体重。
#         """
#         print(f"我的名字是{self.name},年龄是{self.age},身高是{self.height},体重是{self.weight}")
#
#
# # 创建TeachingAssistant类的实例并调用其方法
# as_1 = TeachingAssistant("张三", 30, 176, 65)
# as_1.i()  # 仅打印名字
# as_1.e()  # 打印名字和年龄
# as_1.w()  # 打印名字和身高
# as_1.introduce()  # 打印名字、年龄、身高和体重


"""
6：属性装饰器
    题目：
        创建一个类 Temperature，包含属性 celsius，并使用属性装饰器 
        @property 和 @celsius.setter 来控制摄氏度的取值范围（-273.15°C 到 1000°C）。
"""