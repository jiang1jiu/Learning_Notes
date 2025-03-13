"""
目录：
     1.打印（print语句）
     2.注释
     3.查看数据类型（type语句）
     4.数据类型的转换
     5.标识符
     6.运算符
     7.字符串的三种定义方式
     8.字符串的拼接
     9.字符串格式化
     10.字符串格式化的精度控制
     11.字符串格式化的第二种方式
     12.对表达式进行格式化
     13.输入语句（input语句）
"""

"""
1. print() 打印内容，里面内容可多项 之间用<,>逗号隔开
    补充：
        输出不换行功能：
            在print语句中加入end='' 就可以实现不换行输出了
            格式：
                print（"内容",end=''）
                
"""
# 例子
# a = 10
# print("总钱数", a)
# a = a - 10
# # 优化
# a += 10  # 等于 a = a +10
# print(a)

"""
2. type() 查看数据类型  查看a的数据类型
"""
#例子
# print("剩余", type(a))

# 数据类型转换
"""
3. 转字符串 str()
   转小数（浮点数） float()
   转整数 int（）
    
    注意：
        万物皆可转成字符串，
        但是如果字符串要转成整数或者小数类型，
        要所转字符串内都是数字才可以
----------------------------------------------------- 
        整数类型的转小数，
        会自动增加一个小数点，如整数类型10 转换为小数会变成 10.0
----------------------------------------------------- 
        小数类型的转整数，
        只会保留整数部分，小数部分会丢失        
"""
# 标识符
"""
4. 标识符：
        指的是用户在编程的时候使用的一系列名字，用于给变量、类、方法等命名
---------------------------------------------------------
        标识符命名规范：
                    1.只允许出现，英文、中文、数字、下划线（_)这四种元素，
                    其余不允许出现
                    2.区分大小写
                    3.不可以使用关键字
----------------------------------------------------------     
        注意：1.标识符的命名不推荐使用中文
            2.数字不可以用在开头，下划线可以
            3.变量名 尽量全小写
"""
# 算数运算符
"""
    5.算术运算符
        + 加    += 加法赋值运算符
        - 减    -= 减法赋值运算符
        * 乘    *=
        / 除    /=
        // 取整除  //=
        % 取余   %=
        ** 指数  **= 幂赋值运算符
        = 运算符   == 等于（和运算符无关，一般用于判断）
"""
# # 举例
# a = 1
# a = a + 1
# # 同等于
# a += 1
# # 二者结果一致
"""
  6. 字符串相关
    引号的嵌套
       1.使用 \ 转义字符
            可用转移字符将字符串本身的引号给解除效用，变成普通字符
            如：要打印  "你好世界"
            可以这样  "\"你好世界\""
            \ 后面的引号不做引用正常输出
       2.可以单引号，双引号混用
            如：要打印  "你好世界"
            内容是双引号，就可以用单引号来定义
            ' "你好世界" '
            相反同理
       3. 字符串拼接
            1.用+拼接
            2.只适用于字符串之间的拼接，数字不能用加号拼接
       4.字符串格式化
            可以通过 %s 来实现字符串和变量之间的快速拼接
            其中 % 表示占位
            s 表示将变量变成字符串放入占位的地方
       注意：
            多个变量占位，变量要用括号括起来，见例三
"""

# 使用 \ 转义符 例子
print(" \"转义符\" ")

# 单引号，双引号混用例子
print(" '单引号' ")
print(' "双引号" ')

# 字符串拼接
name = "张三"
print("他的名字是" + name)

# 字符串格式化举例 %s
# 例一 在变量中使用
height = 173
zsheight = "张三的身高 %s" % height
print(zsheight)

# 例二 在打印中使用
age = 27
print("他的年龄是 %s" % age)

# 例三 多个占位符运用
name = "李四"
height = 170
age = 30
print("这个人的名字叫%s，他的身高是%s，他今年%s岁" % (name, height, age))

"""
字符串占位符相关
    常用占位符：
        %s 将内容转换成字符串，放入占位符
        %d 将内容转换成整数，放入占位符
        %f 将内容转换为浮点型（小数），放入占位符
    三者用法同理
    这样可以使数据保持原类型输出出来
"""
"""
字符串格式化--数字精度控制
    可以使用”m .n“来控制数据的宽度和精度
        · m，控制宽度，要求是数字，设置的宽度小于数字自身，不生效  **很少使用**
        · .n，控制小数点精度，要求是数字，会进行小数的四舍五入
    格式：
        %md 控制一个整数的宽度
        %mf 控制一个浮点数的宽度
        %.nf 控制一个浮点数的精度
        %m.nf 控制一个浮点数的宽度和精度
        m和.n 中 m和n指的是数字
"""
# 例子
num1 = 11
num2 = 11.234
print("数字11宽度限制5，结果是：%5d" % num1)    # 结果为[空格][空格][空格]11
print("数字11宽度限制1，结果是：%1d" % num1)    # 结果为 11 因为设置的宽度小于数字自身，不生效
print("数字11.234宽度限制7，小数精度2，结果是：%7.2f" % num2)    # 结果为[空格][空格]11.23
print("数字11.234宽度无限制，小数精度2，结果是：%.2f" % num2)    # 结果为11.23

"""
字符串格式化--快速写法
    语法格式：
        f"内容{变量}"
    特点：
        不限数据类型，不做精度控制
        更加方便
"""
# 例子
name = "王五"
height = 170
age = 30
print(f"我的名字是{name},我身高是{height},我今年{age}岁了")

"""
字符串格式化--对表达式格式化
    表达式定义：
        一条具有明确执行结果的代码语句
        如：1+1、5*2，就都是表达式，因为有具体的结果，结果是一个数字
        表达式可以简单的理解为 除了单个变量或者数字 其他都是表达式
    对表达式格式化的好处：
        在无需使用变量进行数据存储的时候，可以直接格式化表达式，简化代码
"""
# 例子 三种方法
print("1*1的结果是：%d" % (1*1))
print(f"1*2的结果是：{1*2}")
print("字符串在python中的类型是：%s" % type("字符串"))

"""
7.input() 输入语句
要用一个变量接收用户输入的内容
如 变量 = input（)
    input（"提示内容"）
    注意：
        input（）获得的内容默认为字符串，想要获得其他类型的数据，需要自行转换
"""











