import socket

# 创建一个socket对象
socket_server = socket.socket()
# 绑定到本地主机的8888 端口
socket_server.bind(("localhost", 8888))
# 开始监听，允许最多1个连接
socket_server.listen(1)
# listen方法内接受一个整数传参数，表示对接受的连接量
conn, address = socket_server.accept()
# accept方法返回的是二元元组(链接对象， 客户端地址信息)
# 可以通过 变量1，变量2 = socket_server.accept()的形式，直接接受二元元组内的两个元素
# accept()方法，是阻塞的方法，等待客户端的链接，如果没有链接，就卡在这一行不向下执行了
print(f"接收到了客户端的信息，客户端信息是，{address}")
while True:
    data = conn.recv(1024).decode("utf-8")
    # recv接受的参数是缓冲区大小，一般给1024即可
    # recv方法的返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码，将字节数组转换为字符串对象
    print(f"客户端发的消息是，{data}")
    msg = input("请输入你要回复的消息：")
    if msg == "exit":
        break
    conn.send(msg.encode("utf-8"))
# 关闭客户端连接
conn.close()
# 关闭服务器端的socket对象
socket_server.close()









