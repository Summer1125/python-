def eater(name):
	print("%s start to eat"%name)
	food_list = []
	while True:
		food = yield food_list
		print("%s get the %s,eating"%(name,food))
		food_list.append(food)
	


e = eater("jack")
next(e)
e.send("apple")
e.send("banana")
e.send("orange")
print(next(e))

##给协程函数初始化装饰器
def init(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        next(res)
        return res
    return wrapper

@init #eater = init(eater)
def eater(name):
    print("%s start to eat "%name)
    food_list=[]
    while True:
        food = yield food_list
        print("%s get %s ,eating"%(name,food))
        food_list.append(food)

e = eater("Jack")
print(e.send("apple"))
print(e.send("banana"))
