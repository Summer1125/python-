#!-*- coding: utf-8 -*-
import admin
msg1 = '''*********欢迎进入选课系统************
    请选择登录方式：
        1、管理员
        2、学生
        3、退出
**********************************'''
msg2 = '''*********管理员系统************
    请选择操作：
        1、添加课程
        3、退出
**********************************'''
msg3 = '''*********学生选课系统************
    请选择操作：
        1、选课
        2、查看上课记录
        3、查看已选课程
        4、给教师打分
        5、退出
**********************************'''
def putmsg1():
    print(msg1)
def putmsg2():
    print(msg2)
def putmsg3():
    print(msg3)

def StdLoggin():
    '''学生输入用户名和密码，与文件中存储的用户名和密码比对，成功则登录，并返回用户名和密码'''
    fp = open("user_pwd.txt")
    studentName = ("用户名:").strip()
    for line in fp:
        username,password= line.split()
        if studentName == username:
            psw = ("密码：").strip()
            if psw == password:
                print("-----------登录成功-----------")
                return username
            else:
                print("用户名或密码错误，请重试")
    