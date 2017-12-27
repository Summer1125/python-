import socket
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('192.168.1.127',8080))
phone.listen(5)
print('start....')

while True:
    conct,addr = phone.accept()
    print(conct,addr)
    while True:
        try:
            data = conct.recv(1024)
            print('data:',data)
            conct.send(data.upper())
        except Exception:
            break
    conct.close()
phone.close()