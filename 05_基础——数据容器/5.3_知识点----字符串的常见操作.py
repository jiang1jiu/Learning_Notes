"""
1.定义
2.通过下标索引取值
3.字符串的可变性
4.查找特定字符串的下标索引值
5.字符串的替换
6.字符串的分割
7.字符串的规整操作
8.统计字符串中某字符串出现的次数
9.统计字符串的长度
"""
"""
1.定义：
    字符串是字符的容器，一个字符串可以存放任意数量的字符 
2.通过下标索引取值
    和其他容器（列表，元组）一样，字符串也可以通过下标进行访问
        从前往后，下标从0开始
        从后往前，下标从-1开始
3.字符串的可变性
    同元组一样，字符串是一个‘无法修改’的数据容器
    所以：
        修改指定下标的字符
        移除特定下标的字符
        追加字符等
    均无法完成。如果必须要做，只能得到一个新的字符串，旧的字符串是无法修改的
4.查找特定字符串的下标索引值
    语法：
        字符串.index（字符串）
5.字符串的替换
    语法：
        字符串。replace（字符串1，字符串2）
    功能：
        将字符串内的全部：字符串1，替换成字符串2
    注意：
        不是修改字符串本身，而是得到了一个新的字符串
6.字符串的分割
    语法：
        字符串.split（分割字符串）
    功能：
        按照指定的分割符字符串，将字符串划分为多个字符串，并存入列表对象中
    注意：
        字符串本身不变，而是得到了一个列表对象
"""
#  6.例子
my_str = "hello word my python"
print(my_str.split(" "))    # 通过空格分割结果等于['hello', 'word', 'my', 'python']
"""
7.字符串的规整操作
    7.1.去前后空格
        语法：
            字符串.strip()
    7.2.去前后指定字符串
        语法：
            字符串.strip（字符串）
        注意：
            传入的是“12”其实就是：”1”和“2”都会移除，是按照单个字符。
8.统计字符串中某字符串出现的次数
    语法：
        字符串. count(字符串)
9.统计字符串的长度
    语法：
        len（字符串）
"""