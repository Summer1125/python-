# 定义函数
	def func():
		‘函数的描述信息’
		函数体
		return
   用 func._doc_命令来查看函数的描述信息
   定义空函数：
		def func():
			pass
 空函数的目的用来设计框架，定义空函数非常有用！！！
# 函数的调用
 	无参函数的调用
	有参函数的调用，一般有返回值，a = func(x,y)
# 函数的返回值
- 	不写返回值的时候，python返回None
- 	返回多个值的时候，以元组的形式返回
		def func():
			return 1,2,3
	a,b,c = func()的写法可以分别拿到返回值里面的值，这种形式常用
- 函数只要执行了return，函数结束
# 函数的参数
- *args
	要放在位置参数的后面，存储除了位置参数之外剩下的值，以元组的形式。

- **kwargs
	按照关键字传值，放在位置传值的后面，存储除了输入的位置参数后多余的参数，以字典的形式
	顺序：def func(x,*args,**kwargs)
# 命名空间与作用域
- 命名空间的查询
	globals()   locals()
# 函数的嵌套
# 函数对象与闭包
	内部定义的函数，该函数包含对外部作用域而非全局作用域名字的引用
# 装饰器
- 	无参装饰器
- 	有参装饰器
- 	装饰器的语法
		@func(*args,**kwargs)   #index = func(index)
		def index():
			pass
- 装饰器的实现方式：闭包函数
	def timmer(func):
		def wrapper(*args,**kwargs):
			res = func(*args,**kwargs)
  			return res
		return wrapper
- 装饰器不能打印原函数的帮助信息，解决办法：
       from functools import wraps
       在定义wrapper（）函数之前添加 @wraps(func)

# 迭代器
-	可迭代对象：只要对象本身内置了_iter_()方法，就可迭代
-	需要迭代器的原因：
		1：迭代器提供了一种不依赖于索引的取值方式，这样就可以遍历那些没有索引的可迭代对象（字典，集合，文件）；
		2：迭代器与列表比较，迭代器是惰性计算，更节省内存
-	缺点：
		无法获取迭代器的长度，使用不如列表索引取值灵活；
		迭代器是一次性的，只能往后取值，不能倒着取
	
-	查看可迭代对象与迭代器对象
		from collections import Iterable,Iterator
		s = 'hello'
		l = [1,2,3]
		t = (1,2,3)
		d = {'a':1}
		set1 = {1,2,3,4}
		f = open('a.txt')
		上面几种类型都有_iter_()方法，都可以迭代。（s._iter_()）
		有_next_()方法，就是迭代器，上面类型只有ｆ有。
		print(isinstance(s,Iterable))   查看是否可迭代
		print(isinstance(s,Iterator))	查看是否是迭代器，返回True的话就是。
	
	
# 捕捉异常
	d = {"a:1,"b":2,"c":3}
	i = iter(d)
	while True:
			try:
				print(next(i))
			except StopIteration：
				break

			
# 生成器
-	生成器就是一个函数，函数内包含有yield这个关键字。
-	生成器是迭代器。print（isinstance(a,Iterator) 返回True。
-	与return的区别：return只能返回一次，函数就结束了，而yeild能多次返回值。
-	yield：把函数变成生成器，就是迭代器。
	
-	生成器的作用：
# 协程函数
	就是给yield 生成的迭代器send一个或一些值
		
	
