import os
import time

def init(func):
	def wrapper(*args,**kwargs):
		res = func(*args,**kwargs)
		next(res)
		return res
	return wrapper
@init
def search(target):
	while True:
		dir_path=yield
		print("开始生成绝对路径")
		time.sleep(2)
		g = os.walk(dir_path)
		for i in g:
			for j in i[2]:
				file_path = "%s\%s"%(i[0],j)
				# print(file_path)
				target.send(file_path)
@init
def opener(target):
	# '打开文件'
	while True:
		file_path= yield
		print("打开这个路径")
		time.sleep(2)
		with open (file_path) as f:
			target.send((file_path,f))
@init
def cat(target):
	# '读取文件内容'
	while True:
		file_path,f = yield
		print("读取内容")
		time.sleep(2)
		for line in f:
			target.send((file_path,line))

@init
def grep(target,partten):
	# '筛选'
	while True:
		file_path,line = yield
		print("开始筛选")
		time.sleep(2)
		if partten in line:
			print(file_path)
def printer():
	while True:
		file_path,line = yield
		print(file_path)
	
g = search(opener(cat(grep(printer,"python"))))
g.send("E:\search")
