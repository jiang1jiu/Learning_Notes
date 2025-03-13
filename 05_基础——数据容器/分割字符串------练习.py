"""
练习案例：分割字符串给定一个字符串："itheima itcast boxuegu"
    1.统计字符串内有多少个"it"
    2.字符将字符串内的空格,全部替换为字符:"|"
    3.并按照" "进行字符串分割,得到列表
"""
my_str = "itheima itcast boxuegu"
# 1.
a = my_str.count("it")
print(f"字符串{my_str}中有{a}个it字符")
b = my_str.replace(" ","|")
print(f"字符串{my_str}空格被替换后，结果是{b}")
c = b.split("|")
print(f"字符串{b}按照'|'分隔后，结果是{c}")