
# logging 模块
    import logging
    该模块用于处理日志，有以下等级，其中默认级别是warning，默认打印到屏幕
    CRITICAL = 50 #FATAL = CRITICAL
    ERROR = 40
    WARNING = 30 #WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0 #不设置

## 怎么用？？？
    logging.debug('debug')
    logging.info('info')
    logging.warning('warn')
    logging.error('error')
    logging.critical('critical')

    这时在屏幕会打印如下信息：（因为默认是的warning，低于它的不会打印）
    WARNING:root:warn
    ERROR:root:error
    CRITICAL:root:critical
## logging.basicConfig()的方式配置日志文件，这是函数的形式来设置，简单，但是只能指定一个输出端，不推荐。
    import logging
    logging.basicConfig(filename = 'log_module.log',
                        format = "%(asctime)s  [%(lineno)s] %(message)s",
                        datefmt = "%Y-%m-%d",
                        level = 10)
    logging.debug("debug message")
    logging.info("info mesaage")
    logging.warning("warning message")
    logging.error("error message")
    logging.critical("critical message")

    可以在logging.basicConfig()函数中设置各项参数来控制日志的格式，参数有：
    filename    日志输出到哪个文件
    filemode    指定以什么形式，r/w/a/r+等等
    format      指定日志的显示格式
    datefmt     时间格式
    level       设置等级，例如level = logging.DENBUG，或level= 10
    stream      创建StreamHandler

### format的格式
    %(name)s        Logger的名字，并不是用户名

    %(levelno)s     数字形式的日志级别

    %(levelname)s   文本形式的日志级别

    %(pathname)s    调用日志输出函数的模块的完整路径名，可能没有

    %(filename)s    文件名

    %(module)s      模块名

    %(funcName)     函数名

    %(lineno)       输出函数的语句所在的代码行

    %(created)f      当前时间，用UNIX标准的表示时间的浮点数表示

    %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数

    %(asctime)s      字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒

    %(thread)d：线程ID。可能没有

    %(threadName)s：线程名。可能没有

    %(process)d：进程ID。可能没有

    %(message)s：用户输出的消息
## 以logging.getLogger()对象的方式来设置日志
    logger = logging.getLogger()-----------------------产生日志对象
    fh = logging.FileHandler("log.log")----------------产生文件输出对象
    sh = logging.StreamHandler()-----------------------产生终端输出对象

    logger.setLevel(logging.DEBUG)---------------------设置日志等级
    formate = logging.Formatter("%(asctime)s  %(message)s",
                                datefmt = "%Y-%m-%d",)---设置日志显示格式
    logger.addHandler(fh)--------------------------------将文件输出绑定到日志上，也就是说要指定把日志输出到文件了
    logger.addHandler(sh)---------------------------------将文件输出绑定到终端上，也就是说要指定把日志打印在屏幕了

    fh.setFormatter(formate)-----------------------------将日志的格式给文件
    sh.setFormatter(formate)-----------------------------将日志的格式给屏幕
    sh.setLevel(10)--------------------------------------设置屏幕输出的等级

    logger.info("info.....")-----------------------------开始输出日志

    以上格式基本固定，一般是把上面做个一个函数的形式，返回对象，这时候调用函数就行了。如下：
    def logger():
        logger = logging.getLogger()
        fh = logging.FileHandler("log.log")

        logger.setLevel(logging.DEBUG)
        formate = logging.Formatter("%(asctime)s  %(message)s",
                                    datefmt = "%Y-%m-%d",)
        logger.addHandler(fh)
        fh.setFormatter(formate)

        return logger
    ###调用
    logger = logger()
    logger.info("info.....")
