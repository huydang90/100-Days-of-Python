'''
Goal

I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it right side up and it gives an answer by way of a floating die with responses written on it. You can create one in python. You must:

Allow the user to enter their question

Display an in progress message( i.e. "thinking")

Create 20 responses, and show a random response

Allow the user to ask another question or quit

Bonus Using whatever module you like, add a gui. Your gui must have:

A box for users to enter the question

At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)

'''
import random
import time

answer = ["Your future is undetermine", "Could be", "Never", 
"Life is a mystery", "Yes, you're in luck", "Try again next time", "Nope", 
"You're asking the wrong question", "Maybe", "It could be", "Try and see what happens",
"Follow your dreams", "Think more rationally", "Think more deeply", "No way", 
"Buy something nice day", "Treat yourself", "Do more for others", 
"Find your true North", "Know yourself"]


def question(): 
	question = input("Enter your question: ")
	print("...thinking")
	time.sleep(3)
	print(random.choice(answer))
	end()

def end(): 
	user_choice = input("Thank you for your question. Do you want to play again?")
	if user_choice.lower() == 'yes': 
		question()
	else: 
		exit()

print("Welcome to the magic 8-ball")
question()
