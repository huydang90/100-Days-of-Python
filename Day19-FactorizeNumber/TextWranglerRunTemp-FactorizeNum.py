def factorize(x): 
	"""
	Return factors of a given number
	x: int
	"""
	factors = []
	for i in range(1, x + 1): 
		if x % i == 0: 
			factors.append(i)
	print(factors)

user_int = input("Please enter your number: ")
while True: 
	try: 
		if user_int == 'done': 
			break
		x = int(user_int)
		factorize(x)
		
	except: 
		print("Please input integer!")
	