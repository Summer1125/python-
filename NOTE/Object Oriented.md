
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
	对比继承来说也是用来减少代码重用的，组合描述的是一种‘有’的关系。
	老师有课程，学生有成绩....
	class Course:
		def __init__(self,name,price,period):
			self.name=name
			self.price=price
			self.period=period
	class Teacher:
		def __init__(self,name,course):
			self.name=name
			self.course=course
	class Student:
		def __init__(self,name,course):
			self.name=name
			self.course=course
	python=Course("python",100,'3m')
	t = Teacher('egg',python)
	s = Student('Ale',python)

	print(s.course.name)
	print(t.course.period)
	print(t.course.price)
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

# 新式类的继承原理
	在查找属性时遵循：广度优先
	查看继承顺序：print(F.__mro__)
	mro，算出继承关系的列表。
# 新式类的继承原理
	在查找属性时遵循：广度优先
	查看继承顺序：print(F.__mro__)
	mro，算出继承关系的列表。
# super函数的用法
	super(自己的类，self).父类的函数名
	super只能用于新式类
	
	class People:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def speak(self):
		pass
	class Chinese(People):
		def __init__(self,name,age,language='chinese'):
			super().__init__(name,age)
		def speak(self,x):
			super().speak()
			print('x')
				
	
	
# 多态与多态性
	多态是同一种事物的多种形态。
	多态性：定义统一的接口，可以传入不同类型的值，但是调用的逻辑都一样，执行的结果却不一样。
	多态性依赖于：1、继承；
	class Animal:
	def run(self):
		pass
	def speak(self):
		pass
	class People(Animal):
		def run(self):
			print('renzaizou')

	class Pig(Animal):
		def run(self):
			print("pig is walking")
	peo1 = People()
	pig1 = Pig()

	def func(obj):
		obj.run()
	func(peo1)
	func(pig1)
# 封装
	class A:
	__x = 1
	def __test():
		print('form A')
	#print(A.__x)会报错，因为__x变成了_A__x的形式
	print(A.__dict__)
	a = A()
	a.__x也是调不到的
	__名字，这种语法，只在定义的时候才会有变形的效果，如果类或者对象已经产生了，就不会有变形效果。
		
	
	外部想访问x的值，可以这样：
	class A:
	def __init__(self):
		self.__x=1
	def tell(self):
		print(self.__x)

	a = A()
	a.tell()
	问题：为什么下面的return不行？？
	class A
	__x = 1
	def __test():
		print('form A')
	def tell(self):
		return __x
	
	父类中以__开头函数不会被子类覆盖，例如：
	class A:
	def __fa(self):
		print("from A")
	def test(self):
		self.__fa()

	class B(A):
		def __fa(self):
			print('from B')
	b = B()
	b.test()
# property
    property是一种特殊的属性，访问它时会执行

    import math
    class Circle:
        def __init__(self,radius):
            self.radius = radius

        @property
        def area(self):
            return math.pi*self.radius**2

        @property
        def perimeter(self):
            return 2*math.pi*self.radius
    c = Circle(10)
    print(c.radius)
    print(c.area)
    print(c.perimeter)

   补充：
    class People:
    def __init__(self,name):
        self.name= name
    @property
    def name(self):
        return self.__Name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("名字必须是字符串")
        self.__Name = value

    @name.deleter
    def name(self):
        del self.__Name

    p = People('swefegf')
    print(p.name)
    p.name = 'egg'

    print(p.name)

    del p.name
    # print(p.name)

