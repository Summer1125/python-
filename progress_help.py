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
