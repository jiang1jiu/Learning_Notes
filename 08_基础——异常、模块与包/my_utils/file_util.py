"""
文件处理相关工具
"""

# 接收打印文件内容

def print_file_info(file_name):
    f = None  # 定义一个空变量
    try:
        f = open(file_name, "r", encoding="utf-8")
        print(f"当前文件下的内容是：\n{f.read()}")
    except Exception as e:
        print(f"找不到这个文件，是不是输错了？错误原因{e}")
    finally:
        if f:   # 判断f是否有内容，有就往下执行
            f.close()



def append_to_file(file_name, data):
    """
    打开文件并追加内容
    :param file_name: 指定文件的路径
    :param data: 要追加的数据
    :return: None
    """
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(data)
        print("内容追加完成")




if __name__ == '__main__':
    print_file_info("../文件/2.txt")
