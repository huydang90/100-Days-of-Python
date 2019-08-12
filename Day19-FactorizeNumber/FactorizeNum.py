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

try: 
	x = int(user_int)
	factorize(x)
except: 
	print("Please input integer!")
	