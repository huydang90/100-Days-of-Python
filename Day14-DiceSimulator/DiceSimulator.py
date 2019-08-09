import random 
from decimal import Decimal

while True: 
	sides = input("Your desired number of sides: ")
	roll = input("How many times should the dice be rolled? ")
	try: 
		sides = int(sides)
		roll = int(roll)
	except: 
		print("Please input real number!")
		continue 
	dict = {}
	count = 0 
	dice_num = None

	while count < roll: 
		dice_num = random.randint(1,sides)
		if dice_num not in dict: 
			dict[dice_num] = 1
		else: 
			dict[dice_num] += 1
		count += 1
	
	for key, val in dict.items(): 
		i = round(Decimal((val/roll)*100), 2)
		print("Dice number %s appears %s times which is %s percent of the time" %(key, val, i))
