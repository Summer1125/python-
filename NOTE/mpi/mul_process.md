进程线程和IO多路复用
=================
## 
    `进程`：不同的程序，比如说QQ和浏览器就是两个不同的进程
    `线程`：同一个程序的不用操作，比如word里面的读和写，可以用两个线程实现

    ---进程是资源管理单位，线程是最小执行单位。

并行和并发
-------------
## Python的多线程：由于GIL,导致同一进程只能有一个线程被运行。
## 操作系统进行切换的两种情况：
    出现IO操作；固定时间
## 对于计算密集型任务，Python的多线程并没有用；对于IO密集型任务，Python的多线程有意义。

## Python使用多核，可以通过开进程来实现，但是开销很大，并且切换复杂。着重点在协程+多进程上。


## python实现多进程的模块 threading
    t.join()：线程对象t未执行完，主线程不能执行。
    t.setDaemon(True):线程对象t是主线程的协程，主线程执行完了，t即使没有执行完也结束。

## 例子：
```python
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
```
# RLock()的使用
    在python多线程中，会存在线程A还没操作完一个变量，线程B就开始的情况。属于多个线程同时操作一段内存，
    这时候需要给进行操作的代码段加上锁（同步锁），来防止一段内存被多个线程调用。同步锁的使用是在threading
    模块的Lock()函数来实例化一个锁，但是同步锁可能会出现死锁的状况，用的比较多的就是RLock()，递归锁，包含
    同步锁的所有功能又不会死锁。
```python
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
```
# event对象
   threading库中的Event对象是线程之间简单通讯的工具，例如，A线程需要B线程给一个命令才能继续往下执行。
   这时候用event.wait()将A线程暂停，B线程执行到需要的时候用xx.set()来修改A线程的阻塞状态，A线程得以继续执行。
   在 初始情况下,Event对象中的信号标志被设置为假。如果有线程等待一个Event对象, 而这个Event对象的标志为假,那么这个线程将会被<br>一直阻塞直至该标志为  真。一个线程如果将一个Event对象的信号标志设置为真,它将唤醒所有等待这个Event对象的线程。<br>如果一个线程等待一个已经被设置为真的Event对象,那么它将忽略这个事件, 继续执行

    `event.isSet()`：返回event的状态值；

    `event.wait()`：如果 event.isSet()==False将阻塞线程；

    `event.set()`： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；

    `event.clear()`：恢复event的状态值为False
```python
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
```
   threading.Event的wait方法还接受一个超时参数，默认情况下如果事件一致没有发生，wait方法会一直阻塞下去，而加入这个超时参数之后，如果阻塞时间超过这个参数设定的值之后，wait方法会返回。对应于上面的应用场景，如果Redis服务器一致没有启动，我们希望子线程能够打印一些日志来不断地提醒我们当前没有一个可以连接的Redis服务，我们就可以通过设置这个超时参数来达成这样的目的：

```python
def worker(event):
	while not event.is_set():
	logging.debug('Waiting for redis ready...')
	event.wait(2)
	logging.debug('redis ready, and connect to redis server and do some work [%s]', time.ctime())
	time.sleep(1)
```
    转自：http://www.cnblogs.com/yuanchenqi/articles/6755717.html#3881625
# multiprocessing 模块（实现并行）
   由于GIL的存在，python并不能实现真正意义上的多线程，要想充分利用多核CPU资源，可以通过多开进行的方法。
   multiprocessing包是Python中的多进程管理包。与threading.Thread类似。

## Process类调用
```python
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
```
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
`特点`：由于是单线程，不能再切换；不再有任何锁的概念.
下面这个例子只是能模拟实现并发，并不能监听程序中的IO操作
需要借助greenlet库实现，但实现的功能并不多。还有gevent模块。
```python
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
```
    
    总结：学好C的ＭＰＩ是关键！！！

# IO 模型
## `阻塞IO模型`
    特点：全程阻塞
    工作机制：类似于最简单的socket模型，server端在没有收到数据之前，一直在等待，直到拿到client发来的数据。
              这个过程有两个阶段，一个是waiting阶段，一个是等待操作系统在内核将数据拷贝过来的阶段。
## `非阻塞IO`
    特点：发送多次系统调用，在waiting 阶段不阻塞，这个阶段server端可以去做别的事情，等做完了，再查看数据
        有没有到，到的话就阻塞在拷贝数据的阶段，这个阻塞阶段很短。但是数据不是实时接收到的，也就是说可能Server
        端在做别的事情的时候数据已经到了，并没有第一时间拿到。
    两个阶段：waiting for data：非阻塞
                  copy data     :阻塞
    用到的函数：sock.setblocking(False)    其中sock是套接字对象
## `IO多路复用`
    特点：监听多个连接；实现并发；全程阻塞
    实现模块：select
    工作机制：用select.select()来监听server端的套接字sock和连接到server端的client套接字coon,当有一个新的连接进来
              的时候sock就会变化，这时有一个新的conn被监听，当一个conn与server端说话的时候，conn就会发生变化，这时
              server端就可以与这一个client端交流了，在交流的过程中，别的client即使发消息也是阻塞的。直到一个client
              通话结束，然后接收到下一个client的数据，这样实现并发。

### server 端代码
```python
import socket
import select

ip_port = ('192.168.1.127',8080)
sock = socket.socket()
sock.bind(ip_port)
sock.listen(5)
sock.setblocking(False)
socks = [sock,]　　　　　　　＃初始化监听列表
while True:
  r,w,e = select.select(socks,[],[],)　　＃开始监听
  print('r:',r)
  for obj in r:
      if obj == sock:　　　＃如果是有新的client连接进来，server端的套接字对象会变化
	conn,addr = obj.accept()
	  socks.append(conn) #将新连接进来的client套接字放到监听列表
      else:   #如果有消息发动过来，对应的那个client的套接字对象会变化，开始通信
	  data = obj.recv(1024)
	  if not data:break
	  print("---recvData:%s"%data.decode('utf-8'))
	  send_data = input('>>>:').strip()
	  obj.send(send_data.encode('utf-8'))
```
			  
### 客户端代码（可以开多个，最多五个）
```python
import socket

ip_port = ('192.168.1.127',8080)
sock = socket.socket()
sock.connect(ip_port)

while True:
data = input('>>>:').strip()
sock.send(data.encode('utf-8'))
recv_data = sock.recv(1024)
if not data:break
print(recv_data.decode('utf-8'))
sock.close()
```
### 以上代码存在的问题
  当开了多个客户端的时候，其中有一个client关闭，server端就会报错，是因为在windows系统能下需要捕捉异常，
  在捕捉到异常之后，就把这个已经关闭的client的socket对象在监听列表中删除。
  在linux则认为发了一个空信号过来，因此需要加一个是否为空的判断。所以在server端的代码改成：
```python
import socket
import select

ip_port = ('192.168.1.127',8080)
sock = socket.socket()
sock.bind(ip_port)
sock.listen(5)
sock.setblocking(False)
socks = [sock,]
while True:
r,w,e = select.select(socks,[],[],)
print('r:',r)
for obj in r:
    if obj == sock:
	conn,addr = obj.accept()
	socks.append(conn)
    else:
	try:
	    data = obj.recv(1024)
	    print("---recvData:%s"%data.decode('utf-8'))
	    send_data = input('>>>:').strip()
	    obj.send(send_data.encode('utf-8'))
	except Exception:
	    socks.remove(obj)
    # 在linux下用if not data：continue来处理
```
## `异步IO`
    特点：全程无阻塞
# 总结
	前三个都属于同步IO，只要是全程非阻塞的才是异步的。
	阻塞IO：阻塞住对应的进程直到操作完成
	非阻塞IO：在内核还在准备数据的时候直接返回，没有数据的时候返回EROROE。
	同步IO：同步IO操作会引起进程阻塞，直到进程结束，只要有阻塞就是同步。
	异步IO：全程无阻塞。


	同步：阻塞IO，非阻塞IO，IO多路复用
	异步：异步IO

## 套接字对象的本质：文件描述符
	  sock::sock <socket.socket fd=224, 
	  family=AddressFamily.AF_INET, 
	  type=SocketKind.SOCK_STREAM, 
	  proto=0, laddr=('127.0.0.1', 8800)>


	  对于文件描述符（套接字对象）：
	  1 是一个非零整数，不会变
	  2 收发数据的时候，对于接收端而言，数据先到内核空间，然后copy到用户空间，同时，内核空间数据清除。


## 实现IO多路复用,不同的平台有不同的机制：
	  windows: select
	  linux: select,poll,epoll
	  其中最简单的机制就是select，最好的是epoll,poll算是两者之间的过渡，基本不用。


	  select的缺陷：
	  1、每次调用select都要将所有的fd(文件描述符)拷贝到内核空间，导致效率下降。
	  2、在找出哪一个fd变化时，用的是最基本的遍历的方式，来遍历查看每个fd是否有数据访问；(这一点很重要)
	  3、监听的套接字对象个数有限制，最大是1024
	  poll:
	  在select上面做的改进就是最大连接数没有限制了
	  epoll:
	  里面设置了三个函数来改进。
	  1、第一个函数：创建epoll句柄：将所有的fd(文件描述符)拷贝到内核空间，但是只拷贝一次。
	  2、回调函数：某一个函数或者某一个动作成功完成之后就会自动触发的函数。
	     为所有的fd绑定一个回调函数，一旦有数据访问则触发该回调函数，回调函数将fd放到链表中；
	  3、检查链表是否为空


	  对比select和epoll：
	  举个例子，考试交卷，select相当于监考老师挨个问考生“你要不要交卷？”，这样挨个问下来，如果有
	  的话就把卷子拿走（卷子相当于数据）。epoll则是在每个考生那里装了一个按钮，谁做完了就自己按下，
	  监考老师就知道你要交卷子，过去把卷子拿走，效率就提高了。
# selectors 模块
## 是在select模块基础上的封装，建议使用这个来实现IO多路复用！！！！！上面的select知道什么原理就行，面试用的。
  --会根据平台自动选择IO多路复用的机制，在window下面就是select，在linux就是epoll。

  代码展示怎么用selector模块，其中client端不变！！！
##server端代码：
```python
import selectors
import socket

ip_port = ('192.168.1.127',8800)
sock = socket.socket()
sock.bind(ip_port)
sock.listen(5)

sock.setblocking(False)

sel = selectors.DefaultSelector()   #根据平台选择最佳的IO多路复用机制，例如在linux选择epoll

def read(conn,mask):
try:
    data = conn.recv(1024)
    print('recvData:',data.decode('utf-8'))
    send_data = input('>>>:').strip()
    conn.send(send_data.encode('utf-8'))
except Exception:
    sel.unregister(conn)

def accept(sock,mask):
conn,addr = sock.accept()
print("---conn:",conn)
sel.register(conn,selectors.EVENT_READ,read)  # 注册事件

sel.register(sock,selectors.EVENT_READ,accept)   # 注册事件


print('waiting....')
while True:
events = sel.select()
for key,mask in events:
    func = key.data    #accept、read函数
    obj = key.fileobj  #conn
    func(obj,mask)
```
# 队列 queue，   是一种数据类型
* 队列有三种模式：
  `先进先出（FIFO）`，`先进后出(LIFO)`，`设置优先级`<br>
  最常用的：先进先出模式！！！<br>
* 实现模块： import queue
## 优点：线程是安全的，不会出现互斥锁和死锁的情况
## 创建一个队列对象
```python
q = queue.Queue(maxsize = 10)      #默认是FIFO模式
```
## 往队列里面放值
```python
q.put(111)
q.put('hello')
q.put(222)
```
## 将一个值在队列中取出
```python
a = q.get()
b = q.get()
print(a,b)
```
### 注意：
    * 调用put()方法在队列的尾部插入一个值，put()有两个参数，第一个是必须填的插入的值，
    第二个block默认是True，当队列满了的时候就阻塞住不报错，直到有地方拿走了值空出来，
    才会继续执行。当设置`q.put(111,block=False)`的时候，这时候满了的状态下插入值就会报错full。

    * get()方法也是一样，默认block=True，里面是空的时候，如果取值了就阻塞住直到有值。
    `q.get(block=False)`,如果这时候队列里没有值，就报empty的错。
### 三种队列的生成方式：
    FIFO:q = queue.Queue(10)
    LIFO:q = queue.LifoQueue(10)
    pq = queue.PriorityQueue(10)
## 常用的方法：
```python
q.qsize()    #返回队列的大小

q.empty()    #队列为空，返回True

q.full()     #队列满了，返回True
q.join()/q.task_done()     #两个搭配使用，q.jion()监视所有item并阻塞主线程，直到所有item都调
                            用了task_done之后主线程才继续向下执行。这么做的好处在于，假如一个
                            线程开始处理最后一个任务，它从任务队列中拿走最后一个任务，此时任务
                            队列就空了但最后那个线程还没处理完。当调用了join之后，主线程就不会
                            因为队列空了而擅自结束，而是等待最后那个线程处理完成了。
                            q.task_done() 从场景上来说，处理完一个get出来的item之后，调用task_done
                            将向队列发出一个信号，表示本任务已经完成.     
```
## q.join()和q.task_done()代码实例：
```python
import queue


q=queue.Queue(5)

q.put(111)
q.put(222)
q.put(22222)

while not q.empty():
  a=q.get()
  print(a)
q.task_done()

b=q.get()
print(b)
q.task_done()

q.join()

print("ending")
```
## 补充：优先级模式的使用
```python

q=queue.PriorityQueue()

q.put([4,"hello4"])
q.put([1,"hello"])
q.put([2,"hello2"])

print(q.get())
print(q.get())
```
# 生产者消费者模型
```python
import time,random
import queue,threading

q = queue.Queue()
def Producer(name):
    count = 0 
    while count < 10:
        print("making.......")
        time.sleep(random.randrange(3))
        q.put(count)
        print("producer %s  has produced %s "%(name,count))

        count += 1

        print('ok....')
def Consumer(name):
    count = 0
    while count < 10:
        time.sleep(random.randrange(4))
        if not q.empty():
            data = q.get()
            #q.task_done()
            #q.join()
            print(data)
            print("\033[32;1mConsumer %s has eat %s"%(name,data))
        else:
            print("------no  data anymore")
        count += 1

p1 = threading.Thread(target=Producer,args=('A',))
c1 = threading.Thread(target=Consumer,args=('B',))

p1.start()
c1.start()

```


