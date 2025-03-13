"""
题目：
    定义一个数字变量num，内容随意
    并使用range语句，获取从1到num的序列，使用for循环遍历它
    在遍历过程中，统计有多少偶数出现
"""
num = 0
for x in range(1,101):
    if x % 2 ==0:
        num += 1
print(f"1~100之间共有{num}个偶数")