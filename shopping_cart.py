products = [["iphone6",2000],
			["iphone7",3000],
			["iphone8",5000],
			["iphoneX",8000]]
lengh = len(products)
bag={}
salary=int(input("--->please input your salary:"))
balance=salary


while True:
	print("---> You can buy:")
	for i in range(lengh):
		print("                ",i+1,"  ",products[i][0],"\t",products[i][1],"￥")
	choise=input("please input your choise:").strip()
	if choise.isdigit():
		choise = int(choise)
		if choise >= 1 and choise <= lengh:
			if balance < products[choise-1][1]:
				diff = products[choise-1][1] - balance
				print("--->Sorry,you cannot afford %s!"%products[choise-1][0],"and you need %d more"%diff)
			else:
				if products[choise-1][0] in bag:	
					bag[products[choise-1][0]][1] += 1
				else:
					bag[products[choise-1][0]] = [products[choise-1][1],1]

				balance -= products[choise-1][1]
				print("---->Adding %s to the shopping cart....."%products[choise-1][0])
				print("--->What you have bought:",bag,"\n--->Balance: %d"%balance)
		else:
			print("unexistened products!")
	elif choise == "q":
		id_count = 1
		#total = 0
		print(bag)
		print("************Your shopping list*********")
		print("id    products    quantity    price    total")
		for key in bag:
			print("%s     %s       %s         %s     %s"%(id_count,
			                                              key,
			                                              bag[key][1],
			                                              bag[key][0],
			                                              bag[key][1]*bag[key][0]))
			id_count += 1
		print("----------------------------------------\nYour total cost:",salary-balance)
		print("Your current Balance:",balance)
		print("*****************end*******************")
		break
	else:
		print("----Wrong input!")


