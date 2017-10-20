
import time
def timmer(func):
	def wrapper(*args,**kwargs):
		start = time.time()
		# print(func)
		func(*args,**kwargs)
		end = time.time()
		print("time = %s"%(end-start))
	return wrapper

def auth2(choise="file"):
	def auth(func):
		def wrapper(*args,**kwargs):
			if choise == "file":
				name = input(">>UserName:").strip()
				password = input(">>password:").strip()
				if name == "jack" and password == '123':
					print("auth successful")
					res = func(*args,**kwargs)
				else:
					print("auth error")
			else:
				print(choise)
		return wrapper
	return auth

@timmer
@auth2(choise = "file")
def index():
	print("welcome index page")


@timmer
@auth2()
def home():
	print("welcome home page")

index()
home()
