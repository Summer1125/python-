import socket,os,struct,json
class FTPServerDown:
	addressFamily = socket.AF_INET
	socketType = socket.SOCK_STREAM
	maxRecvSize = 8192
	queueSize = 5
	coding ='utf-8'
	allowReuseAddr = False
	serverDir = "fileDown"

	def __init__(self,serverAddr,serverPort,serverActive=True):
		self.serverAddr = serverAddr
		self.serverPort = serverPort
		self.socket = socket.socket(self.addressFamily,
									self.socketType)
		if serverActive:
			try:
				if self.allowReuseAddr:
					self.socket.setckopt(socket.SOL_SOCKET,
										socket.SO_REUSEADDR,1)
					self.socket.bind((self.serverAddr,self.serverport))
					print("---->bind successfully!!")
					self.socket.listen(self.queueSize)
			except:
				self.serverClose()
				raise
	def serverClose(self):
		self.socket.close()
	def serverAccept(self):
		return self.socket.accept()
	def run(self):
		while True:
			self.cont,self.clientAddr = self.serverAccept()
			print("from client: ",self.clientAddr)
			while True:
				try:
					cmdRecvBytes = self.cont.recv(self.maxRecvSize)
					cmdRecv = cmdRecvBytes.decode(self.coding)
					print('---->',cmdRecv)
					cmd = cmdRecv[0]
					fileName = cmdRecv[1]
					if hasattr(self,cmd):
						func = getattr(self,cmd)
						func(fileName)  #put!!!!!
				except Exception:
					break
	def download(self,args):
		fileName = args
		if not os.path.exists(fileName):
			print("file %s cannot find!!!"%fileName)
		dataSize = os.path.getsize(fileName)
		headDic = {'fileName':fileName,"dataSize":dataSize}
		headJson = json.dumps(headDic)
		headJsonBytes = headJson.encode(self.coding)

		headStruct = struct.pack('i',len(headJsonBytes))
		self.cont.send(headJsonBytes)

		sendSize = 0
		with open(fileName,'rb') as fp:
			while sendSize < dataSize:
				for line in fp:
					self.cont.send(line)
					sendSize += len(line)
					print("senddata: ",sendSize)
			else:
				print("%s download %s successfully!"%(self.clentAddr,fineName))







		
















