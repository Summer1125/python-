import socketserver
import os,json,struct

class FTPServer(socketserver.BaseRequestHandler):
    coding = 'utf-8'
    server_dir = 'fileServerLoad'
    max_packet_size = 1024
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    def handle(self):
        print(self.request)
        while True:
            cmdFile = self.request.recv(4)   #收命令和文件的字典长度
            print(len(cmdFile))
            cmdFile_len = struct.unpack('i', cmdFile)[0]
            cmdFile_Json = self.request.recv(cmdFile_len).decode(self.coding)  #收命令和文件的 json形式
            cmdFile_Dic = json.loads(cmdFile_Json)
            print(cmdFile_Dic)
            cmd = cmdFile_Dic['cmd']
            fileName = cmdFile_Dic['fileName']
            if hasattr(self,cmd):
                func = getattr(self,cmd)
                func(cmdFile_Dic)

    def put(self,args):
        file_name = args['fileName']
        file_path = os.path.normpath(os.path.join(
            self.BASE_DIR,
            self.server_dir,
            file_name))
        print("--->",file_path)
        #收取报头
        head_struct = self.request.recv(4)
        head_len = struct.unpack('i',head_struct)[0]
        #收报头的json
        head_json = self.request.recv(head_len).decode(self.coding)
        #报头字典
        head_dic = json.loads(head_json)
        print(head_dic)
        file_size = head_dic['fileSize']
        recv_size = 0
        with open(file_path,'wb') as fp:
            while recv_size < file_size:
                recv_data = self.request.recv(self.max_packet_size)
                fp.write(recv_data)
                recv_size += len(recv_data)
                print('--receive: %s  fileSize:%s'%(recv_size,file_size))
    def download(self,args):
        file_name = args['fileName']
        if not os.path.exists(file_name):
            print('%s cannot find!!'%file_name)
            return
        #写报头
        file_size = os.path.getsize(file_name)
        head_dic = {'cmd':args['cmd'],
                    'fileSize':file_size,
                    'fileName':file_name}
        #报头序列化
        head_json = json.dumps(head_dic)
        head_json_bytes = head_json.encode(self.coding)
        #报头的json长度打包成定长
        head_struct = struct.pack('i',len(head_json_bytes))

        self.request.send(head_struct)
        self.request.send(head_json_bytes)

        send_size = 0
        with open(file_name,'rb') as fp:
            for line in fp:
                self.request.send(line)
                send_size += len(line)
                print('--send:%s  fileSize:%s'%(send_size,file_size))
            else:
                print("%s download successful!")

if __name__ == "__main__":
    ftpserver = socketserver.ThreadingTCPServer(('127.0.0.1',8080),FTPServer)
    ftpserver.serve_forever()

























