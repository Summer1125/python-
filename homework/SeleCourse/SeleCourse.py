#!-*- coding: utf-8 -*-
import pickle
import admin
import Student
import loggin

flag = True
while flag:
    loggin.putmsg1()
    choise = input(">>").strip()
    if choise == "1":
        loggin.putmsg2()
        option = input(">>>").strip()
        if option == '1':
            pass
        elif option == "2":
            pass
        elif option == "3":
           pass
        elif option == "4":
           break
        else:
            print("输入有误，请重新选择编号")
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
            print("输入有误，请重新选择编号")
    elif choise == "3":
        break
    else:
        print("输入有误，请输入对应编号！")

