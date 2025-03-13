"""
定义一个元组，内容是：（'周杰轮'，11，['football'，'music']），记录的是一个学生的信息（姓名、年龄、爱好)
请通过元组的功能（方法），对其进行
    1,查询其年龄所在的下标位置
    2. 查询学生的姓名
    3. 删除学生爱好中的football
    4.增加爱好: coding到爱好list内
"""
id = ('周杰轮', 11, ['football', 'music'])
# 1
print(f'年龄的下标位置是{id.index(11)}')
# 2
print(f"这个学生的姓名是:{id[0]}")
# 3
del id[2][0]
print(id)
# 4
id[2].append('coding')
print(id)
