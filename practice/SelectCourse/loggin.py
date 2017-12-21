#!-*- coding: utf-8 -*-
msg1 = '''\n\n\t\t\t*********欢迎进入选课系统************
    \t\t\t请选择登录方式：
        \t\t\t1、管理员
        \t\t\t2、学生
        \t\t\t3、退出
\t\t\t**********************************\n'''
msg2 = '''\n\n\t\t\t*********管理员系统************
    \t\t\t请选择操作：
        \t\t\t1、添加课程
        \t\t\t2、退出
\t\t\t**********************************\n'''
msg3 = '''\n\n\t\t\t*********学生选课系统************
    \t\t\t请选择操作：
        \t\t\t1、选课
        \t\t\t2、上课
        \t\t\t3、查看听课记录
        \t\t\t4、给教师打分
        \t\t\t5、退出
\t\t\t**********************************\n'''
def putmsg1():
    print(msg1)
def putmsg2():
    print(msg2)
def putmsg3():
    print(msg3)

def studentLoggin():
    '''学生输入用户名和密码，与文件中存储的用户名和密码比对，成功则登录，并返回用户名和密码'''
    count = 0
    while count < 3:
        fp = open("user_pwd.txt")
        inputName = input("\n----用户名:").strip()
        for line in fp:
            userName,password= line.split()
            if inputName == userName:
                psw = input("\n----密码：").strip()
                if psw == password:
                    # print("-----------登录成功-----------")
                    return userName,True
                else:
                    count += 1
                    print("ERROR:用户名或密码错误，请重试")
                    if count == 3:
                        return userName,False
        fp.close()
    