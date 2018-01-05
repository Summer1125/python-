import socket,os,json,struct
class FTPClient:
    server_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    max_packet_size = 1024
    coding = 'utf-8'
    file_dir = "fileClientLoad"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    def __init__(self,server_addr,server_port,active = True):
        self.server_addr = server_addr
        self.server_port = server_port
        self.socket = socket.socket(self.server_family,self.socket_type)
        if active:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise
    def client_connect(self):
        self.socket.connect((self.server_addr,self.server_port))
    def client_close(self):
        self.socket.close()
    def run(self):
        while True:
            input_data = input('>>:').strip()
            ll = input_data.split()
            cmd = ll[0]
            fine_name = ll[1]
            if hasattr(self,cmd):
                func = getattr(self,cmd)
                func(ll)
            else:
                print('wrong input!')

    def put(self,args):
        cmd = args[0]
        file_name = args[1]
        if not os.path.exists(file_name):
            print('%s cannot find!!!'%file_name)
        file_size = os.path.getsize(file_name)
        #写报头
        head_dic = {'cmd':cmd,
                    'fileName':file_name,
                    'fileSize':file_size}
        #序列化并转成字节
        head_json = json.dumps(head_dic)
        head_json_bytes = head_json.encode(self.coding)
        #将长度打包
        head_struct = struct.pack('i',len(head_json_bytes))
        print(len(head_struct))
        #发送报头长度
        self.socket.send(head_struct)
        #发送报头
        self.socket.send(head_json_bytes)
        #发数据
        send_size = 0
        with open(file_name,'rb') as fp:
            for line in fp:
                self.socket.send(line)
                send_size += len(line)
                print('sendsize:%s fileSize:%s'%(send_size,file_size))
            else:
                print("------->upload successful!")

    def download(self,args):
        cmd  = args[0]
        file_name = os.path.basename(args[1])
        #收报头长度,
        head_struct = self.socket.recv(4)
        head_len = struct.unpack('i',head_struct)[0]
        #收报头的bytes，转行成json
        head_json = self.socket.recv(head_len).decode(self.coding)
        #报头字典反序列化
        head_dic = json.loads(head_json)
        print(head_dic)
        file_size = head_dic['fileSize']
        file_path = os.path.normpath(os.path.join(
            self.BASE_DIR,
            self.file_dir,
            file_name))

        #接收文件
        recv_size = 0
        with open(file_path,'rb') as fp:
            if recv_size < file_size:
                recv_data = self.socket.recv(self.max_packet_size)
                recv_size += len(recv_data)
                print('receiveSize:%s  fileSize:%s'%(recv_size,file_size))
            else:
                print("%s download successful!"%file_path)


ftpCLient = FTPClient('127.0.0.1',8080)
ftpCLient.run()