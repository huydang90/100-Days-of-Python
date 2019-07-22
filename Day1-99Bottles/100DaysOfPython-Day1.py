#create function to print out lyrics
def beer(num): 
	while num > 0: 
		print(str(num) + " bottles of beer on the wall, " + str(num) + " bottles of beer.")
		num -= 1
		print("Take one down and pass it around, " + str(num) + " bottles of beer on the wall\n")
		if num == 1: 
			print(str(num) + " bottle of beer on the wall, " + str(num) + " bottle of beer.")
			print("Take one down and pass it around, no more bottles of beer on the wall\n")
			print("No more bottles of beer on the wall, no more bottles of beer.")
			print("Go to the store and buy some more, " + str(num+98) + " bottles of beer on the wall")
			exit()
beer(99)