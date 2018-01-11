# 进程线程
## 
    进程：不同的程序，比如说QQ和浏览器就是两个不同的进程
    线程：同一个程序的不用操作，比如word里面的读和写，可以用两个线程实现

    进程是资源管理单位，线程是最小执行单位。

## 并行和并发
## Python的多线程：由于GIL,导致同一进程只能有一个线程被运行。
## 操作系统进行切换的两种情况：
    出现IO操作；固定时间
## 对于计算密集型任务，Python的多线程并没有用；对于IO密集型任务，Python的多线程有意义。

## Python使用多核，可以通过开进程来实现，但是开销很大，并且切换复杂。着重点在协程+多进程上。


## python实现多进程的模块 threading
    t.join()：线程对象t未执行完，主线程不能执行。
    t.setDaemon(True):线程对象t是主线程的协程，主线程执行完了，t即使没有执行完也结束。

## 例子：
    import threading
    import time
    def music():
        print('start music')
        time.sleep(3)
        print('end music')

    def log():
        print('start log')
        time.sleep(5)
        print('end log')

    if __name__ == "__main__":
        t1 = threading.Thread(target=music,name = 'music')
        t2 = threading.Thread(target=log,name='log')

        t2.setDaemon(True)

        t1.start()
        t2.start()
        

        #t1.join()

    print('end main process')
# RLock()的使用
    在python多线程中，会存在线程A还没操作完一个变量，线程B就开始的情况。属于多个线程同时操作一段内存，
    这时候需要给进行操作的代码段加上锁（同步锁），来防止一段内存被多个线程调用。同步锁的使用是在threading
    模块的Lock()函数来实例化一个锁，但是同步锁可能会出现死锁的状况，用的比较多的就是RLock()，递归锁，包含
    同步锁的所有功能又不会死锁。
        import threading
        import time

        # mutexA = threading.Lock()
        # mutexB = threading.Lock()

        Rlock=threading.RLock()

        class MyThread(threading.Thread):

            def __init__(self):
                threading.Thread.__init__(self)

            def run(self):

                self.fun1()
                self.fun2()

            def fun1(self):

                Rlock.acquire()  # 如果锁被占用,则阻塞在这里,等待锁的释放

                print ("I am %s , get res: %s---%s" %(self.name, "ResA",time.time()))

                Rlock.acquire()  # count=2
                print ("I am %s , get res: %s---%s" %(self.name, "ResB",time.time()))
                Rlock.release()   #count-1

                Rlock.release()   #count-1 =0


            def fun2(self):
                Rlock.acquire()  # count=1
                print ("I am %s , get res: %s---%s" %(self.name, "ResB",time.time()))
                time.sleep(0.2)

                Rlock.acquire()  # count=2
                print ("I am %s , get res: %s---%s" %(self.name, "ResA",time.time()))
                Rlock.release()

                Rlock.release()   # count=0


        if __name__ == "__main__":

            print("start---------------------------%s"%time.time())

            for i in range(0, 10):

                my_thread = MyThread()
                my_thread.start()
# event对象
   threading库中的Event对象是线程之间简单通讯的工具，例如，A线程需要B线程给一个命令才能继续往下执行。
   这时候用event.wait()将A线程暂停，B线程执行到需要的时候用xx.set()来修改A线程的阻塞状态，A线程得以继续执行。
   在 初始情况下,Event对象中的信号标志被设置为假。如果有线程等待一个Event对象, 而这个Event对象的标志为假,那么这个线程将会被一直阻塞直至该标志为  真。一个线程如果将一个Event对象的信号标志设置为真,它将唤醒所有等待这个Event对象的线程。如果一个线程等待一个已经被设置为真的Event对象,那么它将忽略这个事件, 继续执行

    event.isSet()：返回event的状态值；

    event.wait()：如果 event.isSet()==False将阻塞线程；

    event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；

    event.clear()：恢复event的状态值为False

        import threading
        import time
        import logging

        logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

        def worker(event):
            logging.debug('Waiting for redis ready...')
            event.wait()
            logging.debug('redis ready, and connect to redis server and do some work [%s]', time.ctime())
            time.sleep(1)

        def main():
            readis_ready = threading.Event()
            t1 = threading.Thread(target=worker, args=(readis_ready,), name='t1')
            t1.start()

            t2 = threading.Thread(target=worker, args=(readis_ready,), name='t2')
            t2.start()

            logging.debug('first of all, check redis server, make sure it is OK, and then trigger the redis ready event')
            time.sleep(3) # simulate the check progress
            readis_ready.set()

        if __name__=="__main__":
            main()

   threading.Event的wait方法还接受一个超时参数，默认情况下如果事件一致没有发生，wait方法会一直阻塞下去，而加入这个超时参数之后，如果阻塞时间超过这个参数设定的值之后，wait方法会返回。对应于上面的应用场景，如果Redis服务器一致没有启动，我们希望子线程能够打印一些日志来不断地提醒我们当前没有一个可以连接的Redis服务，我们就可以通过设置这个超时参数来达成这样的目的：

        def worker(event):
            while not event.is_set():
                logging.debug('Waiting for redis ready...')
                event.wait(2)
            logging.debug('redis ready, and connect to redis server and do some work [%s]', time.ctime())
            time.sleep(1)
    转自：http://www.cnblogs.com/yuanchenqi/articles/6755717.html#3881625
# multiprocessing 模块（实现并行）
   由于GIL的存在，python并不能实现真正意义上的多线程，要想充分利用多核CPU资源，可以通过多开进行的方法。
   multiprocessing包是Python中的多进程管理包。与threading.Thread类似。

        # Process类调用
        from multiprocessing import Process
        import time
        def f(name):

            print('hello', name,time.ctime())
            time.sleep(1)

        if __name__ == '__main__':
            p_list=[]
            for i in range(3):
                p = Process(target=f, args=('alvin:%s'%i,))
                p_list.append(p)
                p.start()
            for i in p_list:
                p.join()
            print('end')

        # 继承Process类调用
        from multiprocessing import Process
        import time

        class MyProcess(Process):
            def __init__(self):
                super(MyProcess, self).__init__()
                # self.name = name

            def run(self):

                print ('hello', self.name,time.ctime())
                time.sleep(1)


        if __name__ == '__main__':
            p_list=[]
            for i in range(3):
                p = MyProcess()
                p.start()
                p_list.append(p)

            for p in p_list:
                p.join()

            print('end')
   ## process类
        构造方法：

        Process([group [, target [, name [, args [, kwargs]]]]])

        　　group: 线程组，目前还没有实现，库引用中提示必须是None； 
        　　target: 要执行的方法； 
        　　name: 进程名； 
        　　args/kwargs: 要传入方法的参数。

        实例方法：

        　　is_alive()：返回进程是否在运行。

        　　join([timeout])：阻塞当前上下文环境的进程程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。

        　　start()：进程准备就绪，等待CPU调度

        　　run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。

        　　terminate()：不管任务是否完成，立即停止工作进程

        属性：

        　　daemon：和线程的setDeamon功能一样

        　　name：进程名字。

        　　pid：进程号。
# 协程
特点：由于是单线程，不能再切换；不再有任何锁的概念.
下面这个例子只是能模拟实现并发，并不能监听程序中的IO操作
需要借助greenlet库实现，但实现的功能并不多。还有gevent模块。
    from gevent import monkey
    monkey.patch_all()
    import gevent
    from urllib import request
    import time

    def f(url):
        print('GET: %s' % url)
        resp = request.urlopen(url)
        data = resp.read()
        print('%d bytes received from %s.' % (len(data), url))

    start=time.time()

    gevent.joinall([
            gevent.spawn(f, 'https://itk.org/'),
            gevent.spawn(f, 'https://www.github.com/'),
            gevent.spawn(f, 'https://zhihu.com/'),
    ])

    # f('https://itk.org/')
    # f('https://www.github.com/')
    # f('https://zhihu.com/')

    print(time.time()-start)

    总结：还是学好C的MPI吧！！
    
