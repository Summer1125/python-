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
a = {"name":"aaaa"}
print(a)
a["age"] = 20
print(a)
a.append("sex","male")
print(a)