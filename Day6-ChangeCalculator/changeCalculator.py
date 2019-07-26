#create function for sub-units of change
def change(x): 
	x = x*100
	quart = int(x/25)
	dime = int((x-quart*25)/10)
	nickel = int((x-quart*25-dime*10)/5)
	penny = int(x-quart*25-dime*10-nickel*5)
	print(str(quart) + " Quarters, " + str(dime) + " Dimes, " + str(nickel) + " Nickels, " + str(penny) + " Pennies.")

while True: 
	pr = input("Price of item: ")
	mon = input("Amount given: ")
	chan = float(mon) - float(pr)
	change(chan)