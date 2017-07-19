from PIL import Image
import random


print('\nCounting Coins.')

path = "../Images/"
quarter = Image.open(path + "quarter.png").resize((70,70), Image.ANTIALIAS)
dime = Image.open(path + "dime.png").resize((50,50), Image.ANTIALIAS)
nickel = Image.open(path + "nickel.png").resize((60,60), Image.ANTIALIAS)
penny = Image.open(path + "penny.png").resize((55,55), Image.ANTIALIAS)

coins = {25:quarter, 10:dime, 5:nickel, 1:penny}
coinAmount = 0


def displayCoins():
	totalCoins = random.randint(2, 6)
	global coinAmount
	coinAmount = 0
	for i in range(totalCoins):
		value, coinImage = random.choice(list(coins.items()))
		coinAmount += value
		coinImage.show()
	

totalCorrect = 0
totalWrong = 0
totalQuestions = 5
userInput = input("How many questions would you like? ")
if userInput.isdigit():
	totalQuestions = int(userInput)


for i in range(totalQuestions):
	displayCoins()
	userInput = input("How much? ")
	if userInput.isdigit() and int(userInput) == coinAmount:
		totalCorrect += 1
		print("Correct!")
	else:
		totalWrong += 1
		print("Incorrect.")



print("Your score: {0} out of {1}".format(totalCorrect, totalQuestions))
print(round((totalCorrect/totalQuestions) * 100), "%")
if(totalCorrect == totalQuestions):
	print("Perfect score!")
		
