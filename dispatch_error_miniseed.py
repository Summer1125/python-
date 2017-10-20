# miniseed数据的除错程序

# err_file = "D:\Program File(x86)\MATLAB\AH_data\error.txt"
# indata = "D:\Program File(x86)\MATLAB\AH.201502010514.miniseed"
# outdata = "D:\Program File(x86)\MATLAB\New_AH.201502010514.miniseed"
# recorsize = 4096
err_file = "E:\python_prj\error.txt"
indata = "E:\python_prj\in.txt"
outdata = "E:\python_prj\out.txt"
recorsize = 10

skip = 0
index = 0
errors = []

with open(err_file) as err_fp:
	if (err_fp == None):
		print("there is no such file")
	else:
		for err in err_fp:
			errors.append(err)


in_fp = open(indata)
out_fp = open(outdata,'a')

print(errors[-1])
if(in_fp==None):
	print("there is no such file")


while skip <= int(errors[-1]):      
	print(skip)        
	offset = skip * recorsize
	in_fp.seek(offset,0)
	if (skip == int(errors[index])):
		skip += 1
		index +=1
		continue
	skip += 1
	buf = in_fp.read(recorsize)
	if buf == '':
		break
	out_fp.write(buf)
in_fp.close()
out_fp.close()



