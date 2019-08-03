from decimal import Decimal

ls = []
while True: 
	num = input("Enter your numbers, enter done if finish: ")
	if num == 'done': 
		break
	try: 
		num = int(num)
		ls.append(num)
		ls.sort()
	except: 
		print("Please input integer")
		

def round(x,y):
	"""Function to round decimal places"""
	x = Decimal(x)
	output = round(x, y)
	print(output)

def Mean(ls): 
	"""Function to produce mean"""
	total = 0
	count = 0
	for num in ls: 
		total = total + num 
		count += 1
	mean = total / count
	print("Mean: " + str(mean))

def Median(ls): 
	"""Function to find median"""
	if len(ls) % 2 == 0: 
		print("Median: " + str(ls[int(len(ls)/2 - 1)]) + " and " + str(ls[int(len(ls)/2)]))
	else: 
		median = ls[int((len(ls)-1)/2)]
		print("Median: " + str(median))
			
def Mode(ls): 
	"""Function to find mode"""
	count = {}
	for num in ls: 
		if num not in count: 
			count[num] = 0
		else:
			count[num] += 1
	v = list(count.values())
	k = list(count.keys())
	print("Mode: " + str(k[v.index(max(v))]))
	
			
Mean(ls)
Median(ls)
Mode(ls)