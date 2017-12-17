#!-*- coding: utf-8 -*-
import sys,os
import pickle
import admin
import Student
import loggin
flag = True
courseFile = "course.txt"
while flag:
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
            courseName = admin.Course(courseName,courseTime,courseCost,courseTeacher)      #实例化一个课程对象
            courseName.courseContent = get2                                                #将管理员设置的上课内容传给对象
            # print(courseName)
            courseName.saveCourse(courseFile)                                              #保存这门课程
        elif option == "2":
            break
        else:
            print("ERROE:输入有误，请重新选择编号")
    elif choise == "2":
        studentName,flag = loggin.studentLoggin()           #学生验证登录
        if flag == True:
            loggin.putmsg3()
            Student = Student.Student(studentName)
            print(Student)
            option = input(">>>>").strip()                  #登陆成功，弹出选项
            if option == "1":#选课
                Student.seleCourse()
            elif option == "2":#查看上课记录
                pass
            elif option == "3":#查看已选的课程
                pass
            elif option == "4":#评分
                pass
            elif option == "5":#退出
                break
            else:
                print("ERROR:输入有误，请重新选择编号")
        else:
            sys.exit("ERROR:密码多次输入错误")
            break
    elif choise == "3":
        break
    else:
        print("ERROR:输入有误，请输入对应编号！")