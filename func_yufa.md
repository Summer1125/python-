* 迭代器
	可迭代对象：只要对象本身内置了_iter_()方法，就可迭代
	需要迭代器的原因：
		1：迭代器提供了一种不依赖于索引的取值方式，这样就可以遍历那些没有索引的可迭代对象（字典，集合，文件）；
		2：迭代器与列表比较，迭代器是惰性计算，更节省内存
	缺点：
		无法获取迭代器的长度，使用不如列表索引取值灵活；
		迭代器是一次性的，只能往后取值，不能倒着取
	
	---查看可迭代对象与迭代器对象
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
	
	
* 捕捉异常
	d = {"a:1,"b":2,"c":3}
	i = iter(d)
	while True:
			try:
				print(next(i))
			except StopIteration：
				break

			
*生成器
	生成器就是一个函数，函数内包含有yield这个关键字。
	生成器是迭代器。print（isinstance(a,Iterator) 返回True。
	与return的区别：return只能返回一次，函数就结束了，而yeild能多次返回值。
	yield：把函数变成生成器，就是迭代器。
	
	生成器的作用：
		
	
