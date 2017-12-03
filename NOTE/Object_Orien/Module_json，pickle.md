# json 模块，是不同编程语言传递数据时候的桥梁
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
# pickle 模块
    用法语json一样，属于python之间传递数据时候用的一种序列化模块，可以序列化任意格式的数据。
