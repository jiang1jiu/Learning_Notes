"""
字符串相关工具
"""
# 反转字符串
def str_reverse(s):
    str_num = str()
    for i in s:
        str_num = i + str_num
    print(f"你输入的内容是：{s}\n反转之后是：{str_num}")

# 对字符串进行切片
def substr(s, x, y):
    mun = s[x:y]
    print(f"对{s}从第{x}位下标开始到{y}下标结束的切片内容是：{mun}")


