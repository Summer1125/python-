#输出1-100内的所有偶数
# -*-coding:UTF-8 -*-
for i in range (1,101):
	if i%2 == 0:
		print("even num:",i)

#使用while循环输入1 2 3...8 9 10
i=0
num=0
while i<10:
	num = input("please input number:")
	print(num)
	i += 1
	
#输出1-100内的所有奇数
# -*-coding:UTF-8 -*-
for i in range (1,101):
	if i%2 != 0:
		print("odd num:",i)

#求1-100所有数的和
sum=0
for i in range(1,101):
	sum += i

print("Sum=",sum)


#求1-2+3-4...99的所有的和
sum=0
for i in range(1,100):
	if i%2 == 0:
		i=-i
	sum += i
print("sum odd and even:",sum)
