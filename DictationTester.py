import speech

print('\n\nSay words.')

with open('DictationTesterInput.txt', 'r') as file:
	wordList = file.readlines()

totalCorrect = 0
totalWrong = 0
totalWords = len(wordList)
isMatched = False		
						
for word in wordList:
	isMatched = False
	while not isMatched:
		speech.say(word)
		userInput = input("\nSay " + word.strip() + ": ")
		if userInput.lower() == word.strip().lower():
			isMatched = True
			totalCorrect += 1
			print("Correct!")
		else:
			totalWrong += 1
			print("Not a match. Try Again.")
		

print("Your score: {0} out of {1}".format(totalCorrect, totalWords))
print(round((totalCorrect/totalWords) * 100), "%")
if(totalCorrect == totalWords):
	print("Perfect score!")
	
