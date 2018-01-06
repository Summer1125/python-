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
            file_name = ll[1]
            #写命令和文件字典
            cmdFile_Dic = {'NOTHead':True,'cmd':cmd,'fileName':file_name}
            #json序列化
            cmdFile_json = json.dumps(cmdFile_Dic)
            cmdFile_json_bytes = cmdFile_json.encode(self.coding)
            #长度打包成定长
            cmdFile_struct = struct.pack('i',len(cmdFile_json_bytes))
            #发送长度
            self.socket.send(cmdFile_struct)
            #发送命令和文件名
            self.socket.send(cmdFile_json_bytes)
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
        print('11111111')
        #序列化并转成字节
        head_json = json.dumps(head_dic)
        head_json_bytes = head_json.encode(self.coding)
        #将长度打包
        print('2222222')
        head_struct = struct.pack('i',len(head_json_bytes))
        print(len(head_struct))
        print('33333')
        #发送报头长度
        self.socket.send(head_struct)
        print('4444444')
        #发送报头
        self.socket.send(head_json_bytes)
        print('55555')
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
        file_path = file_name+'.fromServer'#文件路径处理有些问题，临时这样
        with open(file_path,'wb') as fp:
            while recv_size < file_size:
                recv_data = self.socket.recv(self.max_packet_size)
                fp.write(recv_data)
                recv_size += len(recv_data)
                print('receiveSize:%s  fileSize:%s'%(recv_size,file_size))
            else:
                print("%s download successful!"%file_path)


ftpCLient = FTPClient('192.168.1.127',8080)
ftpCLient.run()