# hashlib 摘要算法
    不同于加密算法，不可逆，md5只是其中一种方法。
    import hashlib
    m = hashlib.md5()
    m.update('hello'.encode("utf8"))
    print(m.hexdigest())
