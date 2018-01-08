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
