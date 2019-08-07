from random import choice 
		
	
def hangman(): 
	words = ['life', 'edition', 'hangman', 'germany', 'ventilator', 'python', 'practice']
	word = choice(words)
	wordchain = ['_'] * len(word)
	count = 0
	chance = 7	

	while count <= chance: 
		chanceleft = chance - count
		let = input("Please enter your guess letter: ")
		if let in word: 
			ind = word.index(let)
			wordchain[ind] = let
			print(wordchain, " Good guess!")
		else: 
			print("Wrong! Try again")
			count += 1
		guessword = ''.join(wordchain)
			
		if guessword == word: 
			print("You win! The word is: " + word) 
			break
		if count > chance: 
			print("You lose! The word is: " + word)
			break

hangman()