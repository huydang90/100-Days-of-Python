
def fix(): 
	"""Create new file that fix error in story"""
	story = open('story.txt', 'r')

	count = 0
	for line in story: 
		
		#find independent i 
		if line.find('i ') != -1: 
			line = line.replace('i ', 'I ')
			count += 1
			if line.find('Sam-i-am') != -1: 
				line = line.replace('Sam-i-am', 'Sam-I-am')
				count += 1
		FixedStory = open("fixedstory.txt", 'w+')
		FixedStory.write(line)
		FixedStory.close()
		FixedStory = open("fixedstory.txt", 'r')
		for line in FixedStory: 
			print(line)
	print("There are " + str(count) + " mistakes") 
							
fix()
