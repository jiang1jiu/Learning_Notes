import time
import threading


"""
1. threading模块的使用
    thread_obj=threading.Thread(target=func)创建线程对象
    thread_obj.start() 启动线程执行
"""
def sing(msg):
    """
    唱歌函数，无限循环打印消息。

    参数:
    msg (str): 要打印的消息。

    返回:
    无
    """
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    """
    跳舞函数，无限循环打印消息。

    参数:
    msg (str): 要打印的消息。

    返回:
    无
    """
    while True:
        print(msg)
        time.sleep(1)

# 多线程需要传参的话可以通过：args参数通过元组(按参数顺序)的方式传参或使用kwargs参数用字典的形式传参


if __name__ == '__main__':
    # 创建一个唱歌的线程
    sing_thread = threading.Thread(target=sing, args=("我在唱歌，啦啦啦...",))
    # 创建一个跳舞的线程
    dance_thread = threading.Thread(target=dance, args=("我在跳舞，啦啦啦....",))
    # 让线程运行
    sing_thread.start()
    dance_thread.start()

