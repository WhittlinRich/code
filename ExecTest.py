print('\nExecutes arbitrary code.\nType Q to Quit.')

userInput = ''
quit = False

while not quit:
	prompt = "Enter code: "
	
	userInput = input(prompt)
	
	if userInput.lower() == 'q':
		quit = True
	else:
		code = userInput
		#print('Your input:', code)
		exec(code)
	
	if quit:
		print("Thank you! Come Again!")
	
