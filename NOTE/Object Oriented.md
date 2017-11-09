
# 面向对象
	定义类
	class Garen:
		camp=‘demacia’
		def __init__(self,nickname):
			self.nick=nickname
		def attack(self,enemy):
			print(“%s attack %s”%(self.nick,enemy))
# 类：
  实例化：    g = Garen()
  引用类的变量： print(Garen.camp)
  引用类的函数： Garen.attack(1321414)    需要传一个参数进去
# 使用一个对象：
  g1 = Geren()
  print(g1.camp)
  g2 = Geren()
  引用名字：对象名.变量名
  引用绑定方法：对象名.绑定方法
# 可以对类和对象的变量进行增删改查！！！
  查：print(Geren.camp)
  删：del Geren.camp
  增：Geren.x = 1
  改：Geren.camp = 'aaa'

  对象g1有同样的使用方法。
 
# 查看类的命名空间
	print(Geren.__dict__)
# 查看对象的命名空间
	print(g1.__dict__)

# 类的变量通常定义成不可变类型

# 继承和派生
	class A:pass
	class B:pass
	class C(A):pass
	class D(A,B):pass
	
	--查看继承：print(D.__bases__)
	
	class Hero:
		def __init__(self,nickname,life_value):
			self.nickname = nickname
			self.life_value	= life_value
		def attack(self,enemy):
			print("attack from Hero")
	class Garen(Hero):
		def __init__(self,nickname,life_value,script):
			Hero.__init__(self,nickname,life_value)
			self.script = script
		def attack(self,enemy):
			Hero.attack	(self,enemy)
			print('attack from garen')
		camp = "ggggg"
	class Riven(Hero):
		camp = 'rrrrr'

	g = Garen('garen',20,'hello world')
	r = Riven('riven',30)
	print(g.attack(r))
	print(g.script)
	
# 组合
# 接口与归一化设计
	python中没有接口，用继承的关系来解决，有接口是为了让使用者有统一的用法
# 主动抛出异常
	raise Attributeerror('..........')
# 抽象类
	import abc
	class Animal(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def run(self):
		pass
	与普通类额外的特点：加了装饰器的函数，子类必须实现它们
