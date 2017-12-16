import os
import sys
import admin
courseFile = "course.txt"
studentFile = ""#用户名，年龄，课程{课程名，内容},
class Student:
    def __init__(self):
        self.studentName = name
        self.studentAge = age
        self.coursesList = []
        self.courseRecords = {}
        self.studentFile = ''
        self.studentTimes = 0
    def choise_course(self):
    '''学生自己选课，打印可以选的课程，学生根据序号选择，添加到学生文件里'''
        print("可选课程：")
        courseList = []
        count = 1
        with open(courseFile) as fp:                        #打开课程文件，遍历课程名，生成课程名的list
            for line in fp:
                course = line.strip().split()
                courseName = course[0]
                courseList.append(courseName)
        for i in courseList:                                #打印课程名单
            print("%d  %s"%(count,courseList))
        choise = input(">>>").strip()                       #学生根据提示选课
        if courseList[choise-1] in self.records:
            print("%s已经在您的课程表"%courseList[choise-1])
        self.studentCourses.append(courseList[choise-1])           #将课程添加到学生自己的属性records中

    def get_knowlage(self,Course):
        '''学生上课学到上课内容,该课程的上课次数加1，Course是课程类'''
        self.courseRecords[Course.courseName][1] = Course.courseContent 
        self.courseRecords[Course.courseName][0] += 1
    @property
    def courseRecords(self):
        '''学生查看自己的选课和上课记录，返回course和record'''
        pass
    def estimate(self,comment):
        '''学生评价老师，差评老师扣款'''
        pass
    def saveStudentMsg(self):                           #pickle序列化保存文件
        self.studentFile = self.studentName+".pk"

        for i in self.courseList:
                                           #循环所有课程名字，以{“java”:[次数，内容]，'python':[次数，内容]}的形式保存各个课程的记录
            self.courseRecord[i] = [self.studentTimes,i.courseContent]
        saveFomat = {"name":self.studentName,
                     "age":self.studentAge,
                     "courseList":self.courseList,
                     "record":self.courseRecords}
        fp = open(self.studentFile,"wb")
        data_pk = pickle.dump(saveFomat,fp)
        fp.close()
# xm = Student()
# xm.studentName = "小明"
# xm.studentAge = 10
# xm.courseList = ['python','java']
# xm.courseRecords['python']=[1,'sdefwefgwgwrgnrhgp']
# xm.courseRecords["java"] = [2,'jwejfgjgpwg']
# xm.saveStudentMsg()
