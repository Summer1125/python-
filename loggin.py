#-*-coding:utf-8-*-
# （1）用户输入帐号密码进行登陆
# （2）用户信息保存在文件内
# （3）用户密码输入错误三次后锁定用户
import getpass
import os
import sys
count = 0
flag = True
temp = " "


if not os.path.exists("locked_file.txt"):
	f = open(locked_file,"w")
	f.close()

while count < 3:
	name = input(">>UserName:").strip()
	lock_fp = open("locked_file.txt")
	for line in lock_fp:
		if name == line.strip():
			sys.exit("User %s has been locked!"%name)
	lock_fp.close()


	user_fp = open("user_file.txt","r+")
	for line in user_fp:
		msg = line.split()
		user = msg[0]
		pw = msg[1]
		if name == user:
			passwd = getpass.getpass(">>Password:").strip()
			if passwd == pw:
				sys.exit("*******WELCOM!******")
			else:
				print("try again~")
				count += 1
			break
	if count >= 3:
		print("User %s has been locked"%name)
		lock_fp = open("locked_file.txt","a")
		lock_fp.write("\n"+name)
		lock_fp.close()
	user_fp.close()
