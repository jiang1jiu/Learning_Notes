"""
目录：
    1.字典的定义
    2.字典数据的获取
    3.字典的嵌套
    4.从嵌套字典中获取数据
    5.字典的常用操作
    6.字典的特点
"""
"""
1.字典的定义
    同样使用{}，不过存储的元素是一个个的'键值对'(key: value)，如以下语法
        1.1，定义字典字面量
            {key: value, key: value, ..., key: value}
        1.2，定义字典变量
            my_dict = {key: value, key: value, ..., key: value}
        1.3，定义空字典
            my_dict = {}    #空字典定义方式1
            my_dict = dict()     #空字典定义方式2
    字典的key值不允许重复
2.字典数据的获取
    注意：
        字典和集合一样不可以使用下标索引
        但是字典可以通过key值来取得对应的value
    语法：
        字典1[key]
3.字典的嵌套
    字典的key和value可以是任意数据类型的 但是“key不能是字典”
    语法：
         my_dict = {
         key: {
            key：value， 
            key：value
         }, key: 
            {key：value}
         }
        详情见：
            05_基础——数据容器/本章学习截图（不适合写出来的那种）/字典的嵌套.png
4.从嵌套字典中获取数据
    语法：
        my_dict = {
         key1: {
            key2：value2， 
            key3：value3
         }, key4: 
            {key：value}
         }
    获取key1中key3的数据
    num = my_dict[key1][key3] 
5.字典的常用操作  
    5.1，新增元素
        语法：
            字典[key] = value
        结果：
            字典被修改，新增了元素
    5.2，更新(修改)元素
        语法：
            字典[key] = value
        结果：
           字典被修改，元素被更新
        注意：
            字典key值不可以重复，所以对已存在的key执行上述操作，
            就是更新value值，不存在就是新增
    5.3，删除元素
        语法：
            字典.pop(key)
        结果：
            获得指定key的value，同时字典被修改，指定key的数据被删除
    5.4，清空字典
        语法：
            字典.clear()
        结果：
            字典被修改，元素被清空。但是字典还存在结果为空 
    5.5，获取全部的key
        语法：
            字典.keys()
        结果：
            得到字典中的全部key
    5.6，遍历字典
        方法1：
            通过获取到全部key来完成遍历
            具体见：
                05_基础——数据容器/本章学习截图（不适合写出来的那种）/遍历字典---方法1.png 
        方法2：
            直接对字典进行for循环，每一次循环都是直接得到key
            具体见：
                05_基础——数据容器/本章学习截图（不适合写出来的那种）/遍历字典---方法2.png
    5.7，统计字典内的元素数量
        语法：
            len(字典) 
6.字典的特点
    1.可以容纳多个数据
    2.可以容纳不同类型的数据
    3.每一份数据是key:value键值对
    4.可以通过key获取到value，key不可重复(重复会被覆盖掉)
    5.不支持下标索引
    6.可以修改(增加或删除更新元素等)
    7.支持for循环，不支持while循环
"""
# 例2
my_dict = {"张三": 10, "李四": 15, "王五": 23}
print(f"例2，张三的成绩是{my_dict['张三']}")
# 例4
my_dict1 = {
    "张三": {
        "语文": 20,
        "数学": 30
    }, "李四": {
        "语文": 10,
        "数学": 50
    }
}
# 获取张三的数学成绩
score = my_dict1["张三"]["数学"]
print(f"例4，张三的数学成绩是：{score}")
# 例5.2
my_dict1["张三"]["数学"] = 1  # 把张三的数学成绩更新为1
score = my_dict1["张三"]["数学"]
print(f"例5.2，张三修改后的的数学成绩是：{score}")
# 例5.3
my_dict1.pop("李四")  # 删除李四的成绩  并且可以通过变量去接收key的value
print(f"例5.3，删除李四的成绩：{my_dict1}")
# 例5.4
my_dict1.clear()
print(f"例5.4，删除my_dict1词典{my_dict1}")   # 字典还在变成了空字典
my_dict1["王五"] = 10  # 验证字典是否存在
print(my_dict1)
# 例5.5
my_dict2 = {
    "张三": {
        "语文": 20,
        "数学": 30
    }, "李四": {
        "语文": 10,
        "数学": 50
    }
}
print(f"例5.5：{my_dict2.keys()}")
"""

"""