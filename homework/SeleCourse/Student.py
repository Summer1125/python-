import os
import sys
class Student:
    def __init__(self,name,pwd,age,sex,course,record):
        self.name = name
        self.age = age
        self.sex = sex
        self.course = []
        self.record = {}
    def get_knowlage(self,course):
        '''学生上课学到上课内容'''
        pass
    def choise_course(self):
        '''学生自己选课'''
        pass
    def get_msg(self):
        '''学生查看自己的选课和上课记录，返回course和record'''
        pass
    def estimate(self):
        '''学生评价老师，差评老师扣款'''
        pass