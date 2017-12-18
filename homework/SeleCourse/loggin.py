#!-*- coding: utf-8 -*-
msg1 = '''*********欢迎进入选课系统************
    请选择登录方式：
        1、管理员
        2、学生
        3、退出
**********************************'''
msg2 = '''*********管理员系统************
    请选择操作：
        1、添加课程
        2、退出
**********************************'''
msg3 = '''*********学生选课系统************
    请选择操作：
        1、选课
        2、上课
        3、查看听课记录
        4、给教师打分
        5、退出
**********************************'''
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
        inputName = input("用户名:").strip()
        for line in fp:
            userName,password= line.split()
            if inputName == userName:
                psw = input("密码：").strip()
                if psw == password:
                    # print("-----------登录成功-----------")
                    return userName,True
                else:
                    count += 1
                    print("用户名或密码错误，请重试")
                    if count == 3:
                        return userName,False
        fp.close()
    