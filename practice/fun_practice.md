# 写函数，计算传入数字参数的和。（动态传参）
```python
	def SUM(x,y):
		return x+y
	print(SUM(11,22))
```
# 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
```python
	def modify(fileName,content):
		with open (fileName) as fp:
			for line in fp:
				if content in line:
					line = 'aaaaaaa'
```
# 写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
```python
	def check(iter):
		for i in iter:
			if i=='':
				print("error item")
				return False
```
# 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
```python

	dic = {"k1": "v1v1", "k2": [11,22,33,44]}
	# PS:字典中的value只能是字符串或列表
	def check_len(dic):
		res={}
		for key in dic:
			if len(dic[key]) > 2:
				res[key]=dic[key][0:2]
			else:
				res[key] = dic[key]
			return res
	print(check_len(dic))
```
# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组，例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃A’)]
```python
	s = ['红心','草花','黑桃','方片']
	def pock():
		pock=[]
		for i in range(2,11):
			for j in s:
				tu = (j,i)
				pock.append(tu)
		num_expend=['J','Q','K','A']
		for i in num_expend:
			for j in s:
				tu = (j,i)
				pock.append(tu) 
		print(pock)
		print(len(pock))
	pock()
```
# 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}，例如:min_max(2,5,7,8,4)，返回:{‘max’:8,’min’:2}
```python
	def min_max(*args,**kwargs):
		dic_return={}
		min_value=args[0]
		max_value=args[0]
		for i in args:
			if i < min_value:
				min_value = i
			if i > max_value:
				max_value = i
		return {'max':max_value,'min':min_value}
	print(min_max(2,5,7,8,4))
```
# 写函数，专门计算图形的面积
# 其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
# 调用函数area(‘圆形’,圆半径) 返回圆的面积
# 调用函数area(‘正方形’,边长) 返回正方形的面积
# 调用函数area(‘长方形’,长，宽) 返回长方形的面积
```python
	def area(*args):
		def rectangle(l,w):
			area = l * w
			return area
		def square(l):
			area = l ** 2
			return area
		def circle(r):
			area = 3.14 *(r ** 2)
			return area
		if args[0] == "rectangle":
			print('rectangle area=%s'%rectangle(args[1],args[2]))
		elif args[0] == "square":
			print('square area=%s'%square(args[1]))
		elif args[0] == "circle":
			print('circle area=%s'%circle(args[1]))
		else:
			print("wrong input")
	area('circle',1)
	area('rectangle',3,4)
	area('square',2)
```
# 写函数，传入一个参数n，返回n的阶乘
```python
	def cal(n):
		res=1
		for i in range(1,n+1):
			res *= i
		return res
	print(cal(7))
```
# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
```python
	current_loggin = {"name":None,'status':False}
	def auth(func):
		def wrapper(*args,**kwargs):
			
			if current_loggin['name'] and current_loggin['status']:
				res = func(*args,**kwargs)
				return res
			else:
				name = input(">>userName:").strip()		
				with open("user_file.txt") as fp:
					for line in fp:
						usr,pwd = line.split()
						if name == usr:
							passwd = input(">>password:").strip()
							if passwd == pwd:
								print("logged in!")
								res = func(*args,**kwargs)
								current_loggin["name"]=name
								current_loggin['status']=True
								return res
							else:
								print("auth error!")
		return wrapper

	@ auth
	def home():
		print("welcome to home page ")
	@auth
	def index():
		print("welcome to index page")
	home()
	index()
```
# 生成器和迭代器
# 生成器和迭代器的区别？
# 生成器有几种方式获取value？next和for循环
# 通过生成器写一个日志调用方法， 支持以下功能
	# 根据指令向屏幕输出日志
	# 根据指令向文件输出日志
	# 根据指令同时向文件&屏幕输出日志
	# 以上日志格式如下
	# 2017-10-19 22:07:38 [1] test log db backup 3
	# 2017-10-19 22:07:40 [2]    user alex login success 
	# #注意：其中[1],[2]是指自日志方法第几次调用，每调用一次输出一条日志
	# 代码结构如下
	#  def logger(filename,channel='file'):
	#     """
	#     日志方法
	#     :param filename: log filename
	#     :param channel: 输出的目的地，屏幕(terminal)，文件(file)，屏幕+文件(both)
	#     :return:
	#     """
	#     ...your code...
	#  #调用
	#  log_obj = logger(filename="web.log",channel='both')
	#  log_obj.__next__()
	#  log_obj.send('user alex login success')
```python
	import datetime
	def logger(filename,channel='file'):
		count = 1
		log = yield
		time = datetime.datetime.now()
		msg = '%s [%s] %s'%(time,count,log)
		if channel == 'file':
			with open(filename,'a') as fp:
				fp.write(msg)
		elif channel == 'teminal':
			print(msg)
		count += 1
	log_obj = logger('out.txt',channel='teminal')
	log_obj.__next__()
	log_obj.send('user alex login success')
```
# 用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
```python
	name=['alex','wupeiqi','yuanhao','nezha']
	g = map(lambda item:item+'_sb',name)
	print(list(g))
```
# 用filter函数处理数字列表，将列表中所有的偶数筛选出来
```python
	num = [1,3,5,6,7,8]
	f = filter(lambda i:i%2==0,num)
	print(list(f))
```
# 如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
# 计算购买每支股票的总价
# 用filter过滤出，单价大于100的股票有哪些
```python
	portfolio = [
	    {'name': 'IBM', 'shares': 100, 'price': 91.1},
	    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
	    {'name': 'FB', 'shares': 200, 'price': 21.09},
	    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
	    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
	    {'name': 'ACME', 'shares': 75, 'price': 115.65}
	]
	g = map(lambda dic:dic['shares']*dic['price'],portfolio)
	for i in g:
		print(i)
	f = filter(lambda dic:dic['price']>100,portfolio)
	for i in f:
		print(i['name'])
```

