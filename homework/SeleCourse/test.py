# import pickle
# testFile = "test"
# fp = open(testFile,"ab+")
# a = {"name":"sss","pwd":"zzzzzzz","course":{}}
# b = {"name":"sszcf","pwd":"zzzzzsfwef","course":{}}
# data = pickle.dump(a,fp)
# data = pickle.dump(b,fp)
# fp.close()

# # ff = open(testFile,"rb")
# # for line in ff:
# #     data = ff.read()
# #     s = pickle.loads(data)
# #     print(s)
# a = {"name":"aaaa"}
# print(a)
# a["age"] = 20
# print(a)
class People:
    def __init__(self,name):
        self.name=name
        self.learn = {}
xm = People("xiaoming")
xm.learn["python"] = [2,"sfdfsdf"]
xm.learn["java"] = [2,"sfdfsdf"]
print(xm.learn)



import Student
xm = Student.Student('xiaoming')
print(xm)


在进行学生操作的时候，每个选项都保存一次。保存的代码有点问题。
pickle 的问题已经测试通过。
选课完成后，文件重写；
上课后文件重写；
