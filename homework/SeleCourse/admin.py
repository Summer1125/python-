import os
import sys
import pickle
courseFile = "course.txt"
class Teacher:
    def __init__(self,name,age,course):
        self.teacherName = name                                 #教师姓名
        self.teacherAge = age                                   #教师年龄
        self.__salary = 0                                #教师工资，私有成员
        self.teacherCourse = {}                                 #课程，字典形式，包含课时，学分
    def get_salary(self,num):
        """计算老师的课时费，本课程的课时费乘以时间"""
        self.__salary += self.course["money"] * num
    @property
    def salary(self):
        '''返回老师的课时费'''
        return self.__salary
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
    def getContent(self):
        return self.courseContent
    def readCourse(self,courseFile):###没写完，功能没想好
        fp = open(courseFile,"r")
        for line in fp:
            data = fp.read()
            print(data)
        fp.close()

# python = Course("python","3","2","jack")
# python.courseContent = "学到python内容"
# python.saveCourse(courseFile)
# python.readCourse(courseFile)








