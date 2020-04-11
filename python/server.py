#coding=utf-8
#!/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
#host = socket.gethostname()
host = '0.0.0.0'
port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)
print ("开始服务……",host, port)
while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()      

    print("对方地址: %s" % str(addr))
    while(1):
        recv_msg = clientsocket.recv(1024)
        print (recv_msg.decode('utf-8'))
        msg=input() + "\r\n"
        clientsocket.send(msg.encode('utf-8'))
    #clientsocket.close()
