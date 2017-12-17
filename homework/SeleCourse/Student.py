import os
import sys
import admin
import pickle
courseFile = "course.txt"
class Student:
    def __init__(self,name):
        self.studentName = name
        self.studentFile = self.studentName+".pk"
        self.studentAge = 18
        self.courseList = []
        self.courseRecords = {}
        self.courseTimes = 0
    def seleCourse(self):
        '''学生自己选课，打印可以选的课程，学生根据序号选择，添加到学生文件里'''
        print("可选课程：")
        courseAll = []
        count = 1
        with open(courseFile) as fp:                        #打开课程文件，遍历课程名，生成课程名的list
            for line in fp:
                course = line.strip().split()
                courseName = course[0]
                courseAll.append(courseName)
        for i in courseAll:                                #打印课程名单
            print("%d:  %s\n"%(count,i))
        choise = int(input(">>>").strip())                       #学生根据提示选课
        choiseCourse = courseAll[choise-1]
        if choiseCourse in self.courseList:
            print("%s已经在您的课程表"%choiseCourse)
        self.courseList.append(choiseCourse)
        print("----选课成功：%s"%(choiseCourse))           #将课程添加到学生自己的属性records中

    def getKnowledge(self):
        '''学生上课学到上课内容,该课程的上课次数加1，Course是课程类
            打开课程文件，根据输入的那门课读取哪一行对应的上课内容，保存到courseRecord中'''
        print("上什么课？")
        count  = 1
        for i in self.courseList:
            print("\t%d: %s"%(count,i))
            count += 1
        choise = input("选择上什么课>>").strip()
        choiseCourse = slef.coursesList[choise-1]
        with open(courseFile) as fp:        #打开课程文件，读取里面对应的课程内容
            for line in fp:
                course = line.strip().split()
                if choiseCourse == course[0]:
                    self.courseRecords[choiseCourse][1] = course[-1]     #学到内容
                    self.courseRecords[choiseCourse][0] += 1             #这门课次数加一

    @property
    def Records(self):
        '''学生查看自己的选课和上课记录，返回course和record'''
        pass
    def estimate(self,comment):
        '''学生评价老师，差评老师扣款'''
        pass
    def saveStudentMsg(self):                           #pickle序列化保存文件
        # for i in self.courseList:                       #循环所有课程名字，以{'python':[次数，内容]}的形式保存课程记录
        #     self.courseRecord[i] = [self.courseTimes,i.courseContent]#!!!!!!!!!有问题
        saveFomat = {"name":self.studentName,
                     "age":self.studentAge,
                     "List":self.courseList,
                     "record":self.courseRecords}
        fp = open(self.studentFile,"wb")
        data_pk = pickle.dump(saveFomat,fp)
        fp.close()
    # def readStudentMsg(self):
    #     fp = open(self.studentFile)
    #     data = fp.read()
    #     Msg = pickle.loads(data)
    #     print(Msg)
    #     return Msg
xm = Student('xiaoming')
# xm.studentAge = 10
# xm.courseList = ['python','java']
# # xm.courseRecords['python'][0]=[1,'xiaomingxuele python']
# xm.saveStudentMsg()
fp = open(xm.studentFile,'rb')
data = fp.read()
msg = pickle.loads(data)
print(msg)