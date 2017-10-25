文件内容：
apple 10 3
computer 5000 1
phone 3000 2
pen 10 10


with open("hello.txt") as fp:
	l = (line.split() for line in fp)
	dic = ({"name":i[0],"price":i[1],"count":i[2]} for i in l)
	money = (int(i['price'])*int(i['count']) for i in dic)
	print(next(money))	

	print(sum(money))
