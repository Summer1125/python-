
# socket套接字
  c/s架构：
  1，服务器能一直提供服务
  2，能根据ip和端口找到唯一的应用程序
  
# 简单socket套接字收发程序，实现在客户端输入小写，返回大写的功能，以打电话为例解释这一过程
 ## 服务端  server.py
    import socket
    phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)           #买手机
    phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)        #就是它，在bind前加，解决端口占用的报错
    phone.bind(('127.0.0.1',8080))                   #绑定手机卡

    phone.listen(5)                      #开机  ?5表示可以连接一个客户端

    print('starting....')
    while True: #链接循环
        conn,addr=phone.accept()            #等待电话链接

        print('电话线路是',conn)
        print('客户端的手机号是',addr)

        while True: #通信循环
            try:                              #应对windows系统下客户端出现崩溃，用异常处理
                data=conn.recv(1024)          #收消息  ?1024表示在缓存中一次所能读取的最大字节数
                #if not data:break             #linux系统下如果发送的是空，这样处理
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
# 粘包问题
## 解决粘包问题
### 服务端代码：
  
    import socket,struct,json
    import subprocess
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #就是它，在bind前加

    phone.bind(('127.0.0.1',8080))

    phone.listen(5)

    while True:
        conn,addr=server.accept()
        while True:
            cmd=conn.recv(1024)
            if not cmd:break
            print('cmd: %s' %cmd)

            res=subprocess.Popen(cmd.decode('utf-8'),
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            err=res.stderr.read()
            print(err)
            if err:
                back_msg=err
            else:
                back_msg=res.stdout.read()

            headers={'data_size':len(back_msg)}
            head_json=json.dumps(headers)
            head_json_bytes=bytes(head_json,encoding='utf-8')

            conn.send(struct.pack('i',len(head_json_bytes))) #先发报头的长度
            conn.send(head_json_bytes) #再发报头
            conn.sendall(back_msg) #最后发真实的内容

        conn.close()
    server.close()
    
   ### 客户端代码
    #coding:utf-8
    import socket
    import json
    import struct
    ip_port = ('192.168.1.136',9002)
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ip_port)

    while True:
        msg = input('>>>:').strip()
        if not msg:continue
        client.send(msg.encode('utf-8'))

        #收报头长度
        header_struct = client.recv(4)
        header_len = struct.unpack('i',header_struct)[0]
        #收报头
        header_bytes = client.recv(header_len)
        header_json = header_bytes.decode('utf-8')

        header_dic = json.loads(header_json)
        print(header_dic)
        #在报头字典里拿到数据长度
        data_size = header_dic['data_size']

        #最后收数据
        recv_size = 0
        recv_data = b''
        while recv_size < data_size:
            recv_data += client.recv(1024)
            recv_size += len(recv_data)

        print(recv_data.decode('gbk'))

    client.close()
# socketserver 实现并发
    以上代码的socket并不能实现一个服务器，多个客户端之间的通信，需要用socketserver模块来实现并发。
    该模块怎么用的见FTPserver.py和FTPclient.py的服务端和客户端之间的文件上传下载代码。其中客户端可以有很多个与服务端同时通信。
# 基于UDP的套接字通信
    http://www.cnblogs.com/linhaifeng/articles/6129246.html#_label14
