import os
import sys
class Teacher: 
    def __init__(self,name,age,course):
        self.name = name                                 #教师姓名
        self.age = age                                   #教师年龄
        self.__salary = 0                                #教师工资，私有成员
        self.course = {}                                 #课程，字典形式，包含课时，学分
    def get_salary(self,num):
        """计算老师的课时费，本课程的课时费乘以时间"""
        self.__salary += self.course["money"] * num

    def tell_sly(self):
        '''返回老师的课时费'''
        return self.__salary
