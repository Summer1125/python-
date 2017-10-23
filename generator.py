import time
def tail(path_file):
	with open(path_file) as fp:
		fp.seek(0,2)
		while True:
			data = fp.readline()
			if data == '':
				time.sleep(0.5)
			else:
				yield data

def grep(part,lines):
	for l in lines:
		if part in l:
			print(l)

g = tail("E:\python_prj\hello.txt")
grep("error",g)
