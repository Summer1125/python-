
# 模块
    * for 循环、if、else都不能开辟自己的名称空间(作用域)
        x = 3
        for i in range(10):
            x = 55  
        print(x)#打印55
    * 能够开辟自己作用域的：函数、类、模块
## 时间模块(import time)
    模块就是.py文件
    * 时间戳：浮点型数字，从1970年1月1日0点0秒到现在的秒
        获取方式：time.time()
    * 时间字符串
        获取方式：time.strftime("%Y-%m-%d %X")
    * 时间元组（结构化时间）
        获取方式：c = time.localtime()
        time.struct_time(tm_year=2017, tm_mon=11, tm_mday=24, tm_hour=15, tm_min=45, tm_sec=34, tm_wday=4, tm_yday=328, tm_isdst=0)
        >>print(c.tm_year)
    总结：时间戳是计算机能够识别的时间，时间字符串是人能看懂的时间，时间元组是用来操作时间的。
### 几种时间形式的转换
    时间戳<--->结构化时间：localtime/smtime  mktime
    >>>time.localtime(3600*24)
    >>>time.gmtime(3600*24)

    >>>time.mktime(time.localtime)
    字符串时间<--->结构化时间：strftime/strptime
    >>>time.strftime("%Y-%m-%d %X",time.localtime())
    >>>time.strptime("2017-12-12","%Y-%m-%d")
### time.sleep()，括号内单位为秒。
### time.asctime()
### time.ctime()
