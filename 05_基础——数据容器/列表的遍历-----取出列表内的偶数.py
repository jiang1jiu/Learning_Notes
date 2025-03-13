"""
定义一个列表,内容是: [1,2,3,4,5,6,7,8,9,10]
    遍历列表，取出列表内的偶数，并存入一个新的列表对象中
    使用while循环和for循环各操作一次
"""
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# while版
index = 0
num1 = []
# while index < len(num):
#     a = num[index]
#     if a % 2 == 0:
#         num1.append(a)
#     index += 1
# print(f"这个数组里面的偶数有{num1}这些")
# for版
for i in num:
    if i % 2 == 0:
        num1.append(i)
print(f"这个数组里面的偶数有{num1}这些")
