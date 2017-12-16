#!-*- coding: utf-8 -*-
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
            get = input("请输入“课程名称，周期，课时费，授课老师”：").strip()
            courseName,courseTime,courseCost,courseTeacher = get.split(",")
            # print(courseName,courseTime,courseCost,courseTeacher)
            courseName = admin.Course(courseName,courseTime,courseCost,courseTeacher)      #实例化一个课程对象
            # print(courseName)
            courseName.save_course(courseFile)
        elif option == "2":
            pass
        elif option == "3":
           pass
        elif option == "4":
           break
        else:
            print("ERROE:输入有误，请重新选择编号")
    elif choise == "2":
        loggin.putmsg3()
        option = input(">>>>").strip()
        if option == "1":
            pass
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            pass
        elif option == "5":
            break
        else:
            print("ERROR:输入有误，请重新选择编号")
    elif choise == "3":
        break
    else:
        print("ERROR:输入有误，请输入对应编号！")