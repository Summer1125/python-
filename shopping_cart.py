#goods=["iphone6","iphone7","iphone8","iphoneX"]
#price=[1000,3000,5000,8000]
products = [["iphone6",2000],
			["iphone7",3000],
			["iphone8",5000],
			["iphoneX",8000]]
lengh = len(products)
bag=[]

salary=int(input("--->please input your salary:"))
balance=salary


while True:
	print("---> You can buy:\n")
	for i in range(lengh):
		print(i+1,"  ",products[i][0],"\t",products[i][1],"￥")
	choise=input("please input your choise:").strip()
	if choise.isdigit():
		choise = int(choise)
		if choise >= 1 and choise <= lengh:
			if balance < products[choise-1][1]:
				diff = products[choise-1][1] - balance
				print("--->Sorry,you cannot afford %s!"%products[choise-1][0],"and you need %d more"%diff)
			else:
				bag.append(products[choise-1])
				balance -= products[choise-1][1]
				print("---->Adding %s to the shopping cart.....\n"%products[choise-1][0])
				print("--->What you have bought:",bag,"\n--->Balance: %d"%balance)
		else:
			print("inexistencd products!")
	elif choise == "q":
		print("--->Your shopping list:",bag,"\n--->Your balance:",balance)
		break
	else:
		print("----Wrong input!")

#print("--->Your shopping list:",bag,"\n--->Your balance:",balance)

