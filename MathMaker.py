import random
import console

console.set_color(0.0, 0.0, 0.0)
print('\n\nSolve math problems.')

totalQuestions = 4
userInput = input("How many would you like? ")
if userInput.isdigit():
	totalQuestions = int(userInput)

totalCorrect = 0
totalWrong = 0

minRangeTop = 1
maxRangeTop = 10
minRangeBot = 1
maxRangeBot = 10

sign = "+"


for i in range(totalQuestions):
	randomTop = random.randrange(minRangeTop, maxRangeTop + 1)
	randomBottom = random.randrange(minRangeBot, maxRangeBot + 1)
	result = eval(str(randomTop) + " " + sign + " " + str(randomBottom))
	
	padding = "   "
	if result < 10:
		padding = "    "
	
	print("\n{0:5d}\n{1} {2:3d}\n-----".format(randomTop, sign, randomBottom))
	console.set_color(0.2, 0.2, 1.0)
	userInput = input(padding)
	console.set_color(0.0, 0.0, 0.0)
	
	if userInput.isdigit():
		
		if userInput.strip() == str(result):
			totalCorrect += 1
			console.set_color(0.0, 0.8, 0.0)
			print("Correct!")
		else:
			totalWrong += 1
			console.set_color(1.0, 0.0, 0.0)
			print('Incorrect.')

		console.set_color(0.0, 0.0, 0.0)
		
	else:
		print('Input is not a valid number.')


print("Your score: {0} out of {1}".format(totalCorrect, totalQuestions))
print(round((totalCorrect/totalQuestions) * 100), "%")
if(totalCorrect == totalQuestions):
	print("Perfect score!")
