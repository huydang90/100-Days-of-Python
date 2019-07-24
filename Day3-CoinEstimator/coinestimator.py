def convert(x):
	x = x*454
	
def result(pn, nk, dim, quart): 
	wrappn = 0
	wrapnk = 0
	wrapdim = 0
	wrapquart = 0
	if pn == 0: 
 		wrappn = 0
	else: 
 		wrappn = int(pn/(50*2.5))
	if nk == 0: 
 		wrapnk = 0
	else: 
 		wrapnk = int(nk/(40*5))
	if dim == 0: 
 		wrapdim = 0
	else: 
 		wrapdim = int(dim/(50*2.268))
	if quart == 0: 
 		wrapquart = 0
	else: 
 		wrapquart = int(quart/(40*5.67))
	total = (pn*0.01)/2.5 + nk*0.05/5 + dim*0.1/2.268 + quart*0.25/5.67
	print("You have " + str(wrappn) + " pennies wrappers, " + str(wrapnk) + " nikels wrappers, " + str(wrapdim) + " dimes wrapper, " + str(wrapquart) + " quarter wrappers.")
	print("The estimated total value of your stash: USD " + str(total))

def coin():
	wtype = input("Weight in pounds or grams?")
	pn = float(input("Pennies weight: "))
	nk = float(input("Nickels weight: "))
	dim = float(input("Dimes weight: "))
	quart = float(input("Quarters weight: "))
	if (wtype.lower() == "grams") or (wtype.lower() == "gram"):
		result(pn, nk, dim, quart)
	elif (wtype.lower() == "pounds") or (wtype.lower() == "pound"): 
		convert(pn)
		convert(nk)
		convert(dim)
		convert(quart)
		result(pn, nk, dim, quart)
	else: 
		print("Please input the right value: either pounds or grams")
		
coin()
