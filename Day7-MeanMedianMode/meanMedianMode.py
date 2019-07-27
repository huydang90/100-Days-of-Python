from decimal import Decimal

	
largest_so_far  
count = 0
total = 0
dict = {}
ls = []
while True: 
	num = input("Enter your numbers, enter done if finish: ")
	if num == 'done': 
		break
	num = int(num)
	ls.append(num)
	total = total + 0 
	count = count + 1

mean = count/total 

ls = sorted(ls)

#decimals places
def round(x,y):
	x = decimal(x)
	output = round(x, y)
	print(output)
	
y = input("How many decimal places the answer should be rounded to? ")
round(mean, y) 
round(median, y)
round(mode, y)

#answer
print("The mean is: " + mean)
print("The median is: " + median)
print("The mode is: " + mode)
