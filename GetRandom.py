import random

print('Generates a random number from 1 to MAX.')

userInput = ''
quit = False

while not quit:
	prompt = "Enter maximum range: "
	
	userInput = input(prompt)
	
	if userInput.lower() == 'q':
		quit = True
	
	if userInput.isdigit():
		maxRange = int(userInput)
		randomInt = random.randrange(1, maxRange + 1)
		print('Your random # with max range of', maxRange, ' is: ', randomInt)
	elif quit:
		print("Thank you! Come Again!")
	else:
		print('Please enter a valid number or Q to quit')
	
