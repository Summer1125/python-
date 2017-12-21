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
            get1 = input("\n----请输入“课程名称，周期(月)，课时费(元)，授课老师”：").strip()
            get2 = input("\n----请输入该课程的内容：").strip()
            courseName,courseTime,courseCost,courseTeacher = get1.split(",")
            Course = admin.Course(courseName,courseTime,courseCost,courseTeacher)      #实例化一个课程对象
            Course.courseContent = get2                                                #将管理员设置的上课内容传给对象)
            Course.saveCourse(courseFile)                                              #保存这门课程
            print("\n～～～成功添加课程%s～～～\n"%(Course.courseName))

            Tech = admin.Teacher(courseTeacher)                                         #实例化一个老师
            Tech.course = courseName
            Tech.creatFile()                                                            #创建保存该老师信息的文件
            Tech.saveTeacherMsg(Tech.teacherFile)                                       #保存教师信息
            # Tech.readTeacherMsg(Tech.teacherFile)
            break
        elif option == "2":
            break
        else:
            print("ERROR:输入有误，请重新选择编号")
    elif choise == "2":
        userName, status = loggin.studentLoggin()                                       # 学生验证登录
        while flag2:
            if status == True:
                loggin.putmsg3()
                Stud = student.Student(userName)                                        #实例化一个学生
                Stud.creatFile()                                        #监测属于学生的文件是否存在。不存在则创建一个

                option = input("选择操作>>>>").strip()                  #登陆成功，弹出选项
                if option == "1":                                       #选课
                    Stud.seleCourse()
                    Stud.saveStudentMsg()
                    continue
                elif option == "2":                                     #上课
                    learnCourse,times = Stud.getKnowledge()             #返回课程名称和总次数
                    Stud.saveStudentMsg()                               #保存上课记录
                    Stud.readStudentMsg(Stud.studentFile)

                    with open(courseFile) as fp:                        #根据课程名称找到对应的教师
                        for line in fp:
                            courseMsg = line.split()
                            if learnCourse == courseMsg[0]:
                                teacherName = courseMsg[-2]
                    Teach = admin.Teacher(teacherName)                  #实例化一个教师对象
                    Teach.getSalary(times)                              #本次上课结束后，老师的工资相应增加
                    Teach.readTeacherMsg(Teach.teacherFile)
                elif option == "3":                                     #查看课程记录
                    Stud.readStudentMsg(Stud.studentFile)
                    Stud.Records
                elif option == "4":                                     #评分
                    techName,level = Stud.estimate()
                    Teach = admin.Teacher(techName)
                    Teach.beEvaluated(level)                            #教师根据评价奖惩，并保存信息到文件
                    # Teach.readTeacherMsg(Teach.teacherFile)
                elif option == "5":                                     #退出
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