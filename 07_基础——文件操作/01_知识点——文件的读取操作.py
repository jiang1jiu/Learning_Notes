"""

"""
"""
1.打开文件函数
    语法：
        open('name','mode',encoding="编码格式")
            name: 是要打开的目标文件名的字符串(可以包含文件所在的具体路径) 是“/”右斜杠
            mode：设置打开文件的模式(访问模式)：只读，写入，追加等
            encoding：编码格式（推荐utf-8）
    三种访问模式：
        r ：只读，文件指针放在开头，是默认模式
        w ：写入，如果文件存在就打开，不存在会自动新建，写入模式写入的内容会覆盖掉原本内容
        a ：追加，存在打开，不存在新建，如果有内容会写到老内容后面
2.读取的相关操作
注意：
    "只要是在文件打开之后每一次读取，那么下一次读取就会从上一次读取的数据的结尾开始读取"
    1.read()方法
        语法：
            文件对象.read(num)
            num表示要从文件中获取到的数据长度（单位是字节），如果没有传入num，那就表示读取文件中所有数据
    2.readlines()方法 
        语法：
            f = open()   # 打开文件语法
            content = f.readlines()    
            readline可以按照执行的方法把整个文件中的内容进行一次性读取
            并且返回的是一个列表，其中每一行数据为一个元素 
    3.readline()方法
        语法：
            f = open()   # 打开文件语法
            content = f.readline()  
        readline()方法和readlines()差不多，但是不带s的每次调用读取一行
    4.for循环读取文件行
        语法：
            for line in open('name', 'mode',encoding="utf-8"):   
                print(line)
        注意：
            每一个line的临时变量，就记录了文件的一行数据
    5.关闭文件close()方法
        语法：
           f = open()
           f.close()    # 关闭文件语法
    6.with open语法
        语法：
            with open() as f:
                对文件进行操作代码串
        通过在with open 的语句块中对文件进行操作
        可以在操作完成之后自动关闭close文件，避免遗忘掉close方法 
"""
# 例1
# f = open("D:/dev/python/pythonProject1/07_基础——文件操作/文件/测试.txt", "r", encoding="utf-8")   # 读取文件
# 例2.1
# print(f.read(3))      # 通过read()方法读取文件内容
# # 例2.2
# print(f.readlines())   # 通过readlines()方法读取文件内容   每次读取光标所在位置后面的所有内容，换行的话会读取换行符
# 例2.3
# print(f"第一行内容：{f.readline()}")    # 通过readline()方法读取文件内容  每次调用读取一行
# print(f"第二行内容：{f.readline()}")
# print(f"第三行内容：{f.readline()}")
# 例2.4
# for line in open("D:/dev/python/pythonProject1/07_基础——文件操作/文件/测试.txt", "r", encoding="utf-8"):
#     print(line)
# 例2.5 & 例1
# f.close()  # 关闭文件
# 例2.6
# with open("D:/dev/python/pythonProject1/07_基础——文件操作/文件/测试.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line)
