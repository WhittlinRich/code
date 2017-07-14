import speech

print('\n\nSpell words.')

with open('SpellingWords.txt', 'r') as file:
	wordList = file.readlines()

totalCorrect = 0
totalWrong = 0
totalWords = len(wordList)
		
						
for word in wordList:
	speech.say(word)
	userInput = input("Word: ")
	if userInput == word.strip():
		totalCorrect += 1
		speech.say("Correct!")
	else:
		totalWrong += 1
		speech.say("Nope.")


print("Your score: {0} out of {1}".format(totalCorrect, totalWords))
print(round((totalCorrect/totalWords) * 100), "%")
if(totalCorrect == totalWords):
	print("Perfect score!")
	speech.say("Great job!")
else:
	speech.say("Good job.")
