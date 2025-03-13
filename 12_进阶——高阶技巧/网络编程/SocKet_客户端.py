import socket

socket_client = socket.socket()

socket_client.connect(("localhost", 8888))
while True:
    msg = input("请输入要发送的消息：")
    if msg == "ecit":
        break
    socket_client.send(msg.encode("utf-8"))
    recv_data = socket_client.recv(1024)
    print(f"服务端恢复的消息是：{recv_data.decode('utf-8')}")
socket_client.close()
