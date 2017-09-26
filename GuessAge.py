age = 23
count = 0
while count < 3:
	guess_age = int(input("please input your answer:"))
	if guess_age < age:
		print("your answer is smaller!!!")
	elif guess_age > age:
		print("your answer is bigger!!!")
	else:
		print("you got it!!!")
		break
	count +=1
	if count == 3:
		answer = input("do you want to continue?y/n:")
		if answer == "y":
			count=0
		else:
			exit
