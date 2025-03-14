"""
目录：
    1.数据容器的总结对比
        1.1，数据容器的分类
        1.2，数据容器特点对比
    2.数据容器的通用操作
        2.1，遍历
        2.2，通用统计功能
        2.3，数据容器之间的类型转换
        2.4，排序功能
    3.字符串大小比较
"""
"""
1.数据容器的总结对比
    1.1，数据容器的分类
        本章学习截图/数据容器的分类.png
    1.2，数据容器特点对比
        本章学习截图/数据容器特点对比.png
2.数据容器的通用操作
    2.1，遍历
        首先，在遍历上：
            5类数据容器都支持for循环遍历
            列表、元组、字符串支持while，但.循环，集合、字典不支持（因为无法下标索引)
        尽管遍历的形式各有不同，但是，它们都支持遍历操作。
    2.2，通用统计功能
        len(容器)  统计容器的元素个数
        max(容器)  统计容器的最大元素
        min(容器)  统计容器的最小元素
    2.3，数据容器之间的类型转换
        1，list(容器)   将给定容器转换为列表
            注意：
                字符串转列表是把字符串中的每一个元素都取出来，单独作为列表的每一个元素
                字典转列表会忽略value只留下key
        2，str(容器)    将给定容器转换为字符串
            注意：
                字典转字符串value也会保留
        3，tuple(容器)  将给定容器转换为元组 
            注意：
                字符串转列表是把字符串中的每一个元素都取出来，单独作为列表的每一个元素
                字典转列表会忽略value只留下key
        4，set(容器)    将给定容器转换为集合
             注意：
                集合具有无序性，去重性
                字符串转列表是把字符串中的每一个元素都取出来，单独作为列表的每一个元素
                字典转列表会忽略value只留下key
    2.4，排序功能
        语法：
            sorted(容器)    给指定容器进行“正序”排序
            sorted(容器,reverse=True)    给指定容器进行“倒序”排序
        注意：
            排序之后会变成列表对象
            字典排序会丢失value
3.字符串大小比较
    概念：
        在字符串中所有的字符，如：
            大小写英文单词
            数字
            特殊符号(!、|、@、#、空格等)
        都有其对应的ASCII码值
        字符串进行比较是基于数字的码值大小进行比较
    字符串比较是按位比较，也就是一位一位进行比较（从前向后依次比较），只要有一位大，那么整体就大    
    
"""
# 例2.4 排序
num = [3, 6, 7, 8, 1]
# 正序
sorted(num)
print(f"对{num}进行正序排序：{sorted(num)}")
print(f"对{num}进行倒序排序：{sorted(num, reverse=True)}")
