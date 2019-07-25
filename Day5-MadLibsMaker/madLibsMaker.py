#create user input
t = input("Enter a time: ")
n = input("Enter a noun: ")
ad = input("Enter an adverb: ")
v = input("Enter a verb: ")
pl = input("Enter a place: ")

#create madlibs story

def multipleReplace(text, wordDict): 
	for key in wordDict: 
		text = text.replace(key, wordDict[key])
	return text

wordDict = {
	'breakfast': t,
	"an orange": n,
	'happily': ad,
	'escaped': v,
	'the kitchen door': pl}

str1 = """
One day before breakfast, an orange rolled off the counter and escaped its fate, bouncing happily through the kitchen door. Filled with hope, the egg followed.
"""

str2 = multipleReplace(str1, wordDict)

print(str2)
