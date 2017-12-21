import os
import sys
import pickle
courseFile = "course.txt"

class Teacher:
    def __init__(self,name):
        self.teacherName = name                                 #教师姓名
        self.teacherFile = "teacher_" + name + '.pk'            #存教师信息的文件
        self.teacherAge = 22                                    #教师年龄
        self.classFee = 0
        self.salary = 0                                       #教师工资，私有成员
        self.course = ''                               #课程
    def readTeacherMsg(self,filePath):
        fp = open(filePath,'rb')
        data = fp.read()
        if data == b'':
            print("------没有该老师的信息------\n")
        else:
            Msg = pickle.loads(data)
            # print(Msg)
            self.teacherName = Msg["name"]
            self.teacherAge = Msg['age']
            self.salary = Msg['salary']
            self.course = Msg['course']
            self.classFee = Msg["classfee"]
        fp.close()
    def saveTeacherMsg(self,filePath):
        saveFormat = {"name":self.teacherName,
                      "age":self.teacherAge,
                      "classfee":self.classFee,
                      "salary":self.salary,
                      "course":self.course,}
        fp = open(filePath,'wb')
        data_pk = pickle.dump(saveFormat,fp)
        fp.close()
    def getSalary(self,times):
        """计算老师的课时费，本课程的课时费乘以次数"""
        self.readTeacherMsg(self.teacherFile)
        self.salary +=  self.classFee * times
        self.saveTeacherMsg(self.teacherFile)
        return self.salary
    def beEvaluated(self,level):
        self.readTeacherMsg(self.teacherFile)
        if level == "A":
            self.salary += 100
            print("\n\t\t\t~~~~~~评分成功，%s奖励100元~~~~~~\n"%self.teacherName)
        if level == "B":
            self.salary += 50
            print("\n\t\t\t~~~~~~评分成功，%s奖励50元~~~~~~\n"%self.teacherName)
        if level == "C":
            self.salary -= 100
            print("\n\t\t\t~~~~~~评分成功，%s扣除100~~~~~~\n"%self.teacherName)
        self.saveTeacherMsg(self.teacherFile)
        print(("\t\t\t%s目前的总课时费：%d")%(self.teacherName,self.salary))

    def creatFile(self):
        if os.path.exists(self.teacherFile) == False:
            print("教师文件不存在，新建一个")
            fp = open(self.teacherFile,'wb')
            fp.close()

class Course:
    def __init__(self,name,time,cost,teacher):
        self.courseName = name
        self.courseTime = time
        self.courseCost = cost
        self.courseTeacher = teacher
        self.courseContent = ""
    def saveCourse(self,courseFile):
        courseSaveFormat = "%s %s %s %s %s\n"\
                            %(self.courseName,
                             self.courseTime,
                             self.courseCost,
                             self.courseTeacher,
                             self.courseContent)
        fp = open(courseFile,"a+")
        fp.write(courseSaveFormat)
        fp.close()
    def readCourse(self,courseFile):###没写完，功能没想好
        fp = open(courseFile,"r")
        for line in fp:
            data = fp.read()
            print(data)
        fp.close()

# python = Course("python","3","2","jack")
# python.courseContent = "learn_python"
# python.saveCourse(courseFile)
# python.readCourse(courseFile)








