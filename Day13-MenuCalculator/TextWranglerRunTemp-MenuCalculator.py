import pprint

menu = {
		"Chicken Strips - 1" : 3.50,
		"French Fries - 2" : 2.50,
		"Hamburger - 3": 4.00,
		"Hotdog - 4" : 3.50,
		"Large Drink - 5" : 1.75,
		"Medium Drink - 6" : 1.50,
		"Milk Shake - 7" : 2.25,
		"Salad - 8" : 3.75,
		"Small Drink - 9" : 1.25 
}

menu_traverse = {
		"1" : 3.50,
		"2" : 2.50,
		"3": 4.00,
		"4" : 3.50,
		"5" : 1.75,
		"6" : 1.50,
		"7" : 2.25,
		"8" : 3.75,
		"9" : 1.25 
}


#loop so multiple order can be made 
while True: 
	print("Please look at the menu and order your food by number: ")
	pprint.pprint(menu)
	#input number strings as order 
	chosen = input("Your order: ")

#calculate order and print out cost + items and price 
	chosen = list(chosen)
	total = 0
	for item in chosen: 
		if item in menu_traverse: 
			total += menu_traverse[item]
	print("Total price: " + str(total))		
