#!-*- coding: utf-8 -*-
import sys,os
import pickle
import admin
import student
import loggin
flag1 = True
flag2 = True
courseFile = "course.txt"
while flag1:
    loggin.putmsg1()
    choise = input(">>").strip()
    if choise == "1":
        loggin.putmsg2()
        option = input(">>>").strip()
        if option == '1':
            get1 = input("请输入“课程名称，周期，课时费，授课老师”：").strip()
            get2 = input("请输入该课程的内容：").strip()
            courseName,courseTime,courseCost,courseTeacher = get1.split(",")
            # print(courseName,courseTime,courseCost,courseTeacher)
            Course = admin.Course(courseName,courseTime,courseCost,courseTeacher)      #实例化一个课程对象
            Course.courseContent = get2                                                #将管理员设置的上课内容传给对象
            # print(courseName)
            Course.saveCourse(courseFile)                                              #保存这门课程
            print("～～～成功添加课程%s～～～"%(Course.courseName))
            break
        elif option == "2":
            break
        else:
            print("ERROR:输入有误，请重新选择编号")
    elif choise == "2":
        userName, status = loggin.studentLoggin()  # 学生验证登录
        while flag2:
            if status == True:
                loggin.putmsg3()
                Stud = student.Student(userName)        #实例化一个学生
                Stud.creatFile()                         #监测属于学生的文件存在么。不存在就创建

                option = input("选择操作>>>>").strip()                  #登陆成功，弹出选项
                if option == "1":                               #选课
                    Stud.seleCourse()
                    Stud.saveStudentMsg()
                    continue
                elif option == "2":                             #上课
                    Stud.getKnowledge()
                    stud.saveStudentMsg()
                elif option == "3":                             #查看课程记录
                    Stud.readStudentMsg(Stud.studentFile)
                elif option == "4":                             #评分
                    pass
                elif option == "5":                             #退出
                    sys.exit("～成功退出～")
                else:
                    print("ERROR:输入有误，请重新选择编号")
            else:
                sys.exit("ERROR:密码多次输入错误")
                break
    elif choise == "3":
        break
    else:
        print("ERROR:输入有误，请输入对应编号！")