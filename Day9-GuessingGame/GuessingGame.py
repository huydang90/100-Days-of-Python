import random

print("""We have chosen a number between 0 and 100. Try to guess what that number is. We will let you know if it is smaller or bigger!""")

def guess():
	x = random.randint(0,100)
	count = 0 
	while True: 
		user_guess = input("Enter your number: ")
		try: 
			user_guess = int(user_guess)
		except: 
			print("Please input integer")
	
		if x < user_guess: 
			print("Your number is bigger!")
			count += 1
		elif x > user_guess: 
			print("Your number is smaller!")
			count += 1
		else: 
			print("Congratulations! You guess correctly!") 
			print("You have used " + str(count) + " guesses.")
			restart()
	
def restart():
	"""Restart game if user wants to play again"""
	re = input("Do you want to play again? ")
	if re.lower() == 'yes': 
		guess()
	else: 
		quit()
		
guess()

	
	