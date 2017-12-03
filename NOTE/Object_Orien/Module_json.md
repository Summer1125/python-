# json 模块
    本模块就包含两个方法：
    json.dumps()    序列化
    json.loads()    反序列化


    import json
    s = {"name":"egg","age":122}
    ss = json.dumps(s)
    print(ss)
    with open("a.txt","w") as fp:
        fp.write(ss)
    with open("a.txt") as fp2:
        data = fp2.read()

    data2 = json.loads(data)
    print(data2)
