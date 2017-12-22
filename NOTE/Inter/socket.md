
# socket套接字
  c/s架构：
  1，服务器能一直提供服务
  2，能根据ip和端口找到唯一的应用程序
  
# 简单socket套接字收发程序，实现在客户端输入小写，返回大写的功能，以打电话为例解释这一过程
 ## 服务端  server.py
    import socket
    phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)                            #买手机
    phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)                         #就是它，在bind前加，解决端口占用的问题
    phone.bind(('127.0.0.1',8080))                                                    #绑定手机卡

    phone.listen(5)                                                          #开机  ?5是最多可以接多少个客户端

    print('starting....')
    while True:                                                       #链接循环
        conn,addr=phone.accept()                               #等待电话链接

        print('电话线路是',conn)
        print('客户端的手机号是',addr)

        while True:                                                    #通信循环
            try:                                             #应对windows系统出现客户端无故崩溃的现象
              data=conn.recv(1024)                          #收消息  ?1024是每次做多接收多少字节
              #if not data:break #应对linux系统出现接收到空消息的情况
                print('客户端发来的消息是',data)

                conn.send(data.upper())
            except Exception:
                break

        conn.close()

    phone.close()
## 客户端
    import socket
    phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    phone.connect(('127.0.0.1',8080))

    while True: #通信循环
        msg=input('>>: ').strip()
        if not msg:continue
        phone.send(msg.encode('utf-8'))
        print('has send===========>')
        data=phone.recv(1024)
        print('has recv===========>')
        print(data)

    phone.close()
