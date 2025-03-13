"""
有如下列表对象：
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast','best']
请：
    1.定义一个空集合
    2.通过for循环遍历列表
    3.在for循环中将列表的元素添加至集合
    4.最终得到元素去重后的集合对象，并打印输出
"""
my_set = set()
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast','best']
for num in my_list:
    my_set.add(num)
print(my_set)
