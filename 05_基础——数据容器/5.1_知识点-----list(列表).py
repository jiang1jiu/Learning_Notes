"""
目录：
    1.数据容器入门
    2.list（列表）
        2.1)列表的常用操作
        2.2)list(列表)的遍历
"""
"""
1.数据容器入门
    定义：
        一种可以容纳多份数据的数据类型，
        容纳的每一份数据称之为1个元素每一个元素，
        可以是任意类型的数据，如字符串、数字、布尔等。
        
    数据容器根据特点的不同，如：
        ·是否支持重复元素
        ·是否可以修改
        ·是否有序，等
    分为5类，分别是：
        列表（list）、元组（tuple）、字符串（str）、集合（set）、字典（dict）
"""
"""
2.1> list（列表）
    1>定义格式：
            #字面量
                [元素1，元素2，元素3，.....,元素N]
            #定义变量
                变量名称 = [元素1，元素2，元素3，.....,元素N]
            #定义空列表
                变量名称 = []
                变量名称 = list（）
        列表内的每一个数据，称之为元素
            ·以[]作为标识符
            ·列表内每一个元素之间用，逗号隔开
        注意:
            列表可以一次存储多个数据,且可以为不同的数据类型,支持嵌套ه
    2>下标索引：
        定义：
            列表中的每一个元素,都有其位置下标索引,从前向后的方向,从0开始,依次递增
        语法：
            列表[下标索引]
        下标索引——反向
            定义：
                从后向前，下标索引为：-1、-2、-3，依次递减。
                -1 = 列表的倒数第一个元素（最后一个）
                -2 = 倒数第二个
                ....
        列表嵌套同样支持下标索引
            语法：
                列表[外层元素下标][内层元素下标]
        注意：
            要注意下标索引的取值范围，超出范围无法取出元素，并且会报错
"""
# name = ['你好', '不好', '元素']
# print(name[1])
# # 嵌套列表下标索引
# name1 = [['你好1', '不好1', '元素1'], ['你好2', '不好2', '元素2']]
# print(name1[1][2])
"""
    3>常用操作（列表的方法）   
        1.定义
        2.使用下标索引(查询）：
            查询指定元素在列表中的下标：（如果找不到，就报错ValueError
            不能用于嵌套列表)
                列表.index（元素）
        3.插入元素：
             语法1，追加单个元素：
                列表.insert(下标,元素），在指定的下标位置，插入指定的元素
             语法2，追加一批元素：
                列表.extend(其他数据容器),将其他数据容器的内容取出，依次追加到尾部
        4.删除元素：
             语法1：
                del 列表[下标]
             语法2：
                列表.pop(下标)
             del 只能把元素给删除,pop不仅可以删除元素,还可以把删掉的元素当作返回值赋予变量
             变量 = 列表.pop(下标)
                相当于通过此方法取出列表内的元素
        5.删除某元素在列表中的第一个匹配项
             语法:
                列表.remove(元素)
                功能:
                    从前到后去寻找给出的元素,然后把找到的第一个元素删掉
                
        6.清空列表：
            语法:
                列表.clear()
        7.修改元素：
            语法：
                列表[下标]=值  
        8.统计某元素在列表内的数量
            语法:
                列表.count(元素)
        9.追加元素：
            语法：
                列表.append（元素），将指定元素，追加到列表的尾部
        10.统计列表内一共有多少元素
            语法:
                len(列表)

    关于方法：
            在python中，如果将函数定义为class（类）的成员，那么函数会称之为方法
            方法和函数功能一样，只是方法的使用格式不同：
            函数的定义：                         方法的定义：
                def add(x,y):                      class Student:
                    return x+y                          def add(x,y):
                                                            return x+y
    ----------------------------------------------------------------------       
            函数的使用：                          方法的使用：        
                num = add（1，2）                     Student = Student（）
                                                     num = Student.add(1,2)     

"""
# # 2
# name = ['你好', '不好', '元素']
# name1 = ['b站', 'python']
# index = name.index('不好')
# print(index)
# # 3
# name.insert(1, '无语')
# print(f"列表被插入元素之后{name}")
# name.extend(name1)
# print(f"将'name1'列表插入'name'列表{name}")
# # 4
# #   方法1
# del name[4]
# print(f"name通过方法1被删除元素后{name}")
# #   方法2
# i = name.pop(4)
# print(f"name通过方法2被取出元素后{name},取出的元素是{i}")
# # 5
# num1 = [1, 2, 3, 4, 5, 2]
# num1.remove(2)
# print(f"通过remove方法移除元素后列表的结果是{num1}")
# # 6
# name1.clear()
# print(f"列表被清空了,列表的结果是{name1}")
# # 7
# name[1] = "耳机"
# print(f"列表被修改元素之后{name}")
# # 8
# num2 = [1, 2, 3, 4, 5, 2, 3]
# print(num2.count(2))  # 查询num2中数字2的个数
# # 9
# name.append("追加元素")
# print(f"通过append方法追加元素之后的列表:{name}")
# # 10
# print(f"num2这个列表中共有{len(num2)}个元素,分别是{num2}")

"""
2.2>列表的遍历
    将容器内的元素依次取出进行处理的行为称为遍历、迭代
    while循环
        语法:
            index = 0 //定义一个变量表示要取出的下标默认为零
            while index < len(列表):  //控制条件,下标小于列表元素
                元素 = 列表[index] //通过下表索引的方式取出元素
                对元素进行处理
                index += 1  //每次循环将变量加一
    for循环
    语法
        for 临时变量 in 数据容器:
            对临时变量进行处理
    while循环和for循环不同的是
    在循环控制上:
        while循环'可以自定循环条件',并自行控制
        for循环'不可以自定循环条件',只可以一个个从容器内取出数据
    在无限循环上:
        while循环'可以'通过条件控制做到无限循环
        for循环理论上'不可以',因为被遍历的容器容量不是无限的
    在使用场景上:
        while循环适用于任何想要循环的场景
        for循环适用于遍历数据容器的场景或者简单的固定次数循环场景
"""
# 2.2例题
# 列表的遍历--while循环
# name = ['你好', '不好', '元素']
# index = 0
# while index < len(name):
#     a = name[index]
#     print(a)
#     index += 1
# 列表的遍历--for循环
# name = ['你好', '不好', '元素']
# for i in name:
#     print(i)







