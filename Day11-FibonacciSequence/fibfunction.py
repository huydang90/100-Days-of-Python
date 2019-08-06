n = input("Enter your desired Fibonacci sequence length: ")
n = int(n)
	
def fib(n):
	count = 0
	base = 0 
	new = 0 
	while count < n-1: 
		if base == 0: 
			print(0)
			print(1)
			base += 1
			count += 1
		elif base == 1 and new == 0: 
			new = new + base
			base = new
			count += 1 
			print(new)
		else: 
			new = new + base
			base = new - base
			count += 1
			print(new)

fib(n)
			
	
	