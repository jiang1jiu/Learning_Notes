"""
自定义工具包
主程序
包—— my_utils
"""
from my_utils.str_util import str_reverse, substr
from my_utils.file_util import print_file_info, append_to_file

print("欢迎使用我的自定义工具包\n")
print("这个工具包支持以下操作：\n")
print("1,将字符串反转并返回\n")
print("2.按照下标对字符串进行切片\n")
print("3.打开一个文件并输出文件类的内容\n")
print("4.打开或者创建一个文件然后将你选择的内容保存到那个文件中\n")
num = int(input("请选择你要进行的操作："))
if num == 1:
    str_1 = input("请输入你要进行反转的内容：")
    str_reverse(str_1)
elif num == 2:
    str_1 = input("请输入你要切片的内容：")
    num_1 = int(input("开始的下标是："))
    num_2 = int(input("结束的下表是："))
    substr(str_1, num_1, num_2)
elif num == 3:
    f = input("请输入你要打印内容的文件夹：")
    print_file_info(f)
elif num == 4:
    f = input("请输入你要追加内容的文件夹：")
    text = input("要追加的内容是：")
    append_to_file(f, text)
else:
    print("没有这个选项哦")

