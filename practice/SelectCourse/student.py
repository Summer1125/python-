import os
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
        print("\t\t\t可选课程：")
        courseAll = []
        count = 1
        with open(courseFile) as fp:                        #打开课程文件，遍历课程名，生成课程名的list
            for line in fp:
                course = line.strip().split()
                courseName = course[0]
                courseAll.append(courseName)
        for i in courseAll:                                     #打印课程名单
            print("\t\t\t%d:  %s\n"%(count,i))
            count += 1
        choise = int(input(">>>").strip())                       #学生根据提示选课
        choiseCourse = courseAll[choise-1]
        self.readStudentMsg(self.studentFile)
        if choiseCourse in self.courseList:
            print("\n\t\t\t%s已经在你的课程表！"%choiseCourse)
        else:
            self.courseList.append(choiseCourse)
            print("~~~~~~选课成功：%s~~~~~~"%(choiseCourse))           #将课程添加到学生自己的属性records中

    def getKnowledge(self):
        '''学生上课学到上课内容,该课程的上课次数加1，Course是课程类
            打开课程文件，根据输入的那门课读取哪一行对应的上课内容，保存到courseRecord中'''
        print("\n\t\t\t----选择上什么课？")
        count  = 1
        self.readStudentMsg(self.studentFile)
        # print(self.courseList)
        for i in self.courseList:
            print("\t\t\t\t%d    %s"%(count,i))
            count += 1
        choise = int(input(">>>>>").strip())
        choiseCourse = self.courseList[choise-1]
        with open(courseFile) as fp:                    #打开课程文件，读取里面对应的课程内容
            for line in fp:
                course = line.strip().split()
                
                if choiseCourse == course[0]:
                    if choiseCourse in self.courseRecords.keys():
                        print("\n\t\t\t这门课上过了，上课次数加1")
                        # print(self.courseRecords)
                        self.courseRecords[choiseCourse][0] += 1
                        times = self.courseRecords[choiseCourse][0]       
                    else:
                        print("\n\t\t\t这门课还没上过，现在开始上课~~~~")
                        self.courseRecords[choiseCourse] = [1,course[-1]]
                        print(self.courseRecords)
                        print(self.courseList)
                        times = self.courseRecords[choiseCourse][0]
            # print("cccccccc",choiseCourse,times)
        return choiseCourse,times
    @property
    def Records(self):
        '''学生查看自己的上课记录，返回course和record'''

        self.readStudentMsg(self.studentFile)               #读学生文件
        if self.courseRecords == {}:
            print("------>还没有上课记录<------")
        else:
            msg = "\n\t\t\t已选课程\t次数"
            print(msg)
            for key in self.courseRecords:
                print("\t\t\t%s\t\t%s"%(key,self.courseRecords[key][0]))
    def estimate(self):
        '''学生评价老师，ABC三级'''
        teacherName,level = input("\n\n----输入教师姓名和等级(name,level(A/B/C))：").strip().split(',')
        return teacherName,level
    def creatFile(self):
        if os.path.exists(self.studentFile) == False:
            print("新建一个学生文件")
            fp = open(self.studentFile,"wb")
            fp.close()
    def saveStudentMsg(self):                           #pickle序列化保存文件
        saveFormat = {"name":self.studentName,
                     "age":self.studentAge,
                     "List":self.courseList,
                     "record":self.courseRecords}
        fp = open(self.studentFile,"wb")
        data_pk = pickle.dump(saveFormat,fp)
        fp.close()
    def readStudentMsg(self,filePath):
        fp = open(filePath,'rb')
        data = fp.read()
        if data == b'':
            print("\n------>你还没有选课<------")
        else:
            Msg = pickle.loads(data)
            # print(Msg)
            self.studentName = Msg["name"]
            self.studentAge = Msg["age"]
            self.courseList = Msg["List"]
            self.courseRecords = Msg['record']
        fp.close()


