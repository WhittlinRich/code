from datetime import date

print('Determines age.')

def getInt(prompt):
	while True:
		try:
			x = int(input(prompt))
			return x
		except ValueError:
			print("Oops! Please enter a valid number.")	

year = getInt("What year were you born? ")
month = getInt("What month were you born? ")
day = getInt("What day were you born? ")

#year = 1975
#month = 7
#day = 3

now = date.today()

timeStr = now.strftime('Today is %A, %B %d %Y')
print(timeStr)	#Wednesday July 05, 2017

born = date(year, month, day)
print("You were born on a", born.strftime('%A.'))

age = now.year - born.year - ((now.month, now.day) < (born.month, born.day))
print("You are {} years old today!".format(age))

