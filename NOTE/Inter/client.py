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
