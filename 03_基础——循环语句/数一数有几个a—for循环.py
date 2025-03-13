"""
题目：
    定义字符串变量name,内容为: "itheima is a brand of itcast"
    通过for循环,遍历此字符串,统计有多少个英文字母: "a"
"""
num = 0
sentence = "itheima is a brand of itcast"
for x in sentence:
    if x == "a":
        num +=1
print(f"itheima is a brand of itcast中共含有{num}个a")

        