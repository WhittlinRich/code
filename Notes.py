#math ####################

w = 3
h = 2
result = w * h
print(result)

squared = 5 ** 2
print(squared)

wholeOnly = 17 // 4
print(wholeOnly)


#console, refering to previous output
#  5 + 2
#  >>> 7
#  _ + 3
#  >>> 10


#strings ####################

print("\n## Begin Strings ##\n")
output = "don't"
output = 'don\'t'
print(output)

print("The word of the day is", output)
#The word of the day is don't
print(output, end=',')
print("No new line", end='')
print("Same line")
#don't,No new lineSame line

text = "First line\nSecond line"
print(text)

path = r"C:\new\folder"
print(path)

text = ('This is a long line of text '
				'joined with another long line')
print(text)

song = 3 * 'la' + 'laaa'
print(song)	#lalalalaaa

print("""\
A block of text
   with indent too
   -h hostname
END
""")

word = "Richard"
print(word[0])		#R
print(word[-1])		#d

print(word[2:4])	#ch
print(word[4:])		#ard
print(word[-3:])	#ard
print(len(word))


'''
This type of string quotation
can be used as a way to
create block comments
instead of using 
# this method of
# block commenting
'''


#lists ####################

print("\n## Begin Lists ##\n")
letters = ['a', 'b', 'c', 'd', 'e']
print(len(letters))	#5
print(letters[0])		#a
print(letters[-1])	#e
print(letters[-3:])	#c d e

newCopyOfLetters = letters[:]

moreLetters = letters + ['f', 'g']
print(moreLetters)

letters[1] = "Bee"
print(letters)

letters.append('f')
print(letters)

letters[1:4] = ['B', 'C', 'D']
print(letters)
# a B C D e f

letters[1:4] = []
print(letters)	# a e f

letters[:] = []	#empty
print(letters)

chars = ['a', 'b', 'c']
nums = [1, 2, 3]
combined = [chars, nums]
print(combined)				#[['a', 'b', 'c'], [1, 2, 3]]
print(combined[0])		#['a', 'b', 'c']
print(combined[0][1])	#'b'


#control flow ####################

print("\n## Begin Control Flow ##\n")

i=0
while i < 10:
	print(i, end=',')		#0,1,2,3,4,5,6,7,8,9,
	i = i + 1

print()	#new line
#single-line assignment
a, b = 0, 1
print(a, b)		#0, 1

x = 0
if x < 0:
	print("negative")
elif x == 0:
	print("zero")	
else:
	print("positive")

bird = 'chicken'	
if bird in ('sparrow', 'hawk', 'dove', 'chicken'):
	print("found", bird)
else:
	print('no', bird)

words = ['cat', 'dog', 'bird']
for w in words:
	print(w, len(w))

#loop over a copy of the list, created by a slice [:]
for w in words[:]:
	if len(w) > 3:
		words.insert(0, w)

print(words)	#['bird', 'cat', 'dog', 'bird']

for i in range(5):
	print(i)	# 0 1 2 3 4

for i in range(5, 10):
	print(i)	# 5 6 7 8 9

for i in range(0, 30, 5):
	print(i)	# 0 5 10 15 20 25

for i in range(len(words)):
	print(i, words[i])


for n in range(1, 10):
	if n < 5:
		print(n, "is less than 5")
	elif n == 5:
		print(n, "is 5")
		break
else:
	print(n, "only prints if theres no break")


for n in range(2, 10):
	if n % 2 == 0:
		print("even", n)
		continue	#skips whats next and starts again
	print("number", n)


def printNumber(n):
	"""Print a number."""
	print(n)

printNumber(8)
pr = printNumber
pr(7)

def getNumberList(n):
	"""Return a list of n numbers"""
	result = []
	i = 0
	while i < n:
		result.append(i)
		i += 1
	return result

numberList = getNumberList(5)
print(numberList)

def sayHello(name, amount=3, greeting='Hi there'):
	if amount < 1:
		raise ValueError('invalid amount')
	for i in range(amount):
		print(greeting, name)


sayHello("Rich")
sayHello("Jim", 1, 'Welcome')
#sayHello("Sam", 0)		#raises error: invalid amount
sayHello(amount=2, name='Alf')

#getting input from user at console 
prompt = "Please enter a number: "
#userInput = input(prompt)
#print("You entered", userInput)


#data structures ####################

print("\n## Begin Data Structures ##\n")

foods = ["pizza", "apple", "banana", "steak"]
colors = ["red", "orange", "yellow", "green"]

foods.append("chicken")	#add to the end
foods.extend(colors)		#append a list to the list
foods.insert(0, "fish")	#insert at position
foods.remove("banana")	#remove matching item
item = foods.pop()			#remove and return last item
item = foods.pop(4)			#remove and return specified item
foods.clear()						#clear entire list
index = colors.index("green")	#returns index of item or error
total = colors.count("green")	#returns total times found
colors.sort()						#sort alphabetical or customized
colors.reverse()				#reverse order
colorsCopy = colors.copy()	#makes a shallow copy
print(colors)

#for efficient back-end removal
stack = [1, 2, 3]
stack.append(4)
print(stack)
stack.pop()
stack.pop()
print(stack)

#for more efficient front-end removal, use deque
from collections import deque
queue = deque(["John", "Tom", "Charlie"])
queue.append("Matt")
queue.append("Mike")
firstLeaves = queue.popleft()
secondLeaves = queue.popleft()
print(firstLeaves, secondLeaves)


#list comprehensions
#example using longer code:
squares = []
for x in range(10):
	squares.append(x**2)
print(squares)

#same result using less code:
squares = [x**2 for x in range(10)]
print(squares)

myNumbers = [10, 20, 30]
myDoubledNumbers = [x*2 for x in myNumbers]
print(myDoubledNumbers)	#[20, 40, 60]

myNumbers = [-1, 3, 5, 6, -8]
myPositiveNumbers = [x for x in myNumbers if x >= 0]
print(myPositiveNumbers)	#[3, 5, 6]

myPositiveNumbers = [abs(x) for x in myNumbers]
print(myPositiveNumbers)	#[1, 3, 5, 6, 8]

fruits = ['banana  ', '  apple', ' cherry ']
cleanedFruit = [item.strip() for item in fruits]
print(cleanedFruit)		#removed surrounding whitespace

myListOfSquaredNumbers = [(x, x**2) for x in range(3)]
print(myListOfSquaredNumbers)		#[(0, 0), (1, 1), (2, 4)]


#del
myNumbers = [10, 20, 30, 40, 50]
del myNumbers[0]	#removes item at specified index
del myNumbers[2:4]	#removes a slice
print(myNumbers)	#[20, 30]
del myNumbers[:]	#deletes all items
del myNumbers 		#deletes entire variable


#tuples (cannot alter item values)
aTuple = 123, 456, 789
print(aTuple[0])	#123
emptyTuple = ()
singleTuple = 'one',
x, y, z = aTuple
print(x, y, z)	# 123, 456, 789


#sets (contains no duplicates)
basket = {'apple', 'apple', 'banana', 'banana', 'peach'}
print(basket)		#{'banana', 'apple', 'peach'}
result1 = 'apple' in basket
result2 = 'fish'	in basket
print(result1, result2)	# True False

#creation of an empty set:
basket2 = set()

uniqueLetters1 = set('alabama')
uniqueLetters2 = set('llamas')
print(uniqueLetters1, uniqueLetters2)
#{'l', 'm', 'a', 'b'} {'l', 'm', 'a', 's'}
difference = uniqueLetters1 - uniqueLetters2
print(difference)		#{'b'}

union = uniqueLetters1 | uniqueLetters2
print(union)				#{'a', 'b', 'l', 'm', 's'}

intersection = uniqueLetters1 & uniqueLetters2
print(intersection)	#{'l', 'm', 'a'}

symmetricDifference = uniqueLetters1 ^ uniqueLetters2
print(symmetricDifference)	#{'b', 's'}

uniqueLettersDifference = {x for x in 'alabama' if x not in 'llamas'}
print(uniqueLettersDifference)	#{'b'}


#dictionaries - unordered unique-key/value pairs
emptyDictionary = {}

contacts = {'rich':749, 'mom':407}
contacts['jim'] = 207
print(contacts)	#{'mom': 407, 'rich': 749, 'jim': 207}
print(contacts['mom'])	#407

del contacts['mom']
print(contacts)	#{'rich': 749, 'jim': 207}

keys = list(contacts.keys())
print(keys)	#['rich', 'jim']
keys = sorted(contacts.keys())
print(keys)	#['jim', 'rich']

result = 'rich' in contacts
print(result)	#True
result = 'rich' not in contacts
print(result)	#False

contacts2 = dict([('rich',749), ('jim',207), ('mom',407)])
print(contacts2)	#{'mom': 407, 'rich': 749, 'jim': 207}

contacts3 = dict(rich=749, jim=207, mom=407)
print(contacts3)	#{'mom': 407, 'rich': 749, 'jim': 207}

numbersAndSquares = {x: x**2 for x in (2, 4, 6)}
print(numbersAndSquares)	#{2: 4, 4: 16, 6: 36}


#looping
contacts = {'rich':749, 'mom':407, 'jim':207}
for name, number in contacts.items():
	print(name, number)
# mom 407  rich 749  jim 207

fruits = ['apple', 'banana', 'oranges']
for i, item in enumerate(fruits):
	print(i, item)
# 0 apple  1 banana  2 oranges

names = ['jim', 'rich', 'mom']
ages = [5, 41, 36]
for name, age in zip(names, ages):
	print('{0} is {1} years old.'.format(name, age))
	
#jim is 5 years old.
#rich is 41 years old.
#mom is 36 years old.

for i in reversed(range(1, 10)):
	print(i)	# 9 8 7 6 5 4 3 2 1

basket = ['apple', 'orange', 'apple', 'pear', 'banana']
for fruit in sorted(set(basket)):
	print(fruit)	#apple banana orange pear
	
#loop over a copy instead of original
import math
rawData = [1, 2, 3, 4, 5, 6]
filteredData = []
for value in rawData:
	if not value % 2 == 0:
		filteredData.append(value)	
		
print(filteredData)	#[1, 3, 5]



#modules ####################

print("\n## Begin Modules & Packages ##\n")

# myModule.py
# print(__name__)		#module/file name

# import myModule
# myModule.functionName()
# myFunction = myModule.functionName
# myFunction()

#	value = myModule.variableName

# from myModule import myFunction1, myFunction2
# myFunction1()

# not the best-practice, but possible:
# from myModule import *
# myFunction1()

# if actively altering modules, can reload with
# imp.reload(myModule)

#lists all currently defined names - variables, modules, functions, etc
# print(dir())


#packages

#in myFolder, place an empty file named:
# __init__.py

# import myFolder.mySubfolder.myModule
# myFolder.mySubfolder.myModule.myFunction()
# from myFolder.mySubfolder import myModule
# myModule.myFunction()
# from myFolder.mySubfolder.myModule import myFunction
# myFunction()

#preferred method of import is:
# from myFolder.mySubfolder import myModule
# myModule.myFunction()

#to refer to modules in same package,
#use full path like any other import
#or use relative import
# from . import myModule
# from .. import myOtherModule



#output ####################

print("\n## Begin Output ##\n")

s = "Hello\n"
print(repr(s))	#prints as inerpreter-readable

for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print("\n")

numberTxt = str(12)
print(numberTxt.zfill(4))

numberTxt = str(12)
print(numberTxt.rjust(4))

formatted = 'The {} said {}'.format('cat', 'meow')
print(formatted)
formatted = 'The {1} said {0}'.format('cat', 'meow')
print(formatted)
formatted = '{animal} said {sound}'.format(animal='cat', sound='meow')
print(formatted)

contacts = {'rich':749, 'mom':407, 'jim':207}
for name, number in contacts.items():
	print('{0:6} ==> {1:6d}'.format(name, number))
	
contacts = {'rich':749, 'mom':407, 'jim':207}
formatted = 'rich: {0[rich]:d}; mom: {0[mom]:d};'.format(contacts)	
print(formatted)

contacts = {'rich':749, 'mom':407, 'jim':207}
formatted = 'rich: {rich:d}; mom: {mom:d};'.format(**contacts)	
print(formatted)

result = 2.10 * 3.12
formatted = 'This is the result: %2.2f' % result
print(formatted)


'''
#files
# w - write new file
# a - append to end
# r - read only
# r+ - read/write
# rb+ - binary read/write

print('\nFiles\n')

file = open('test_rich.txt', 'w')
charCount = file.write('   Hello world  ')

print('Current position: ', file.tell())
file.seek(0)	#goto beginning

aNumber = 1.2
stringValue = str(aNumber)
file.write(stringValue)

file.close()


file = open('test_rich.txt', 'r')
contents = file.read()
print(contents)

file = open('test_rich.txt', 'r')
line = file.readline()
nextLine = file.readline()
print(line)

file = open('test_rich.txt', 'r')
allLines = file.readlines()
print(allLines)

file = open('test_rich.txt', 'r')
for line in file:
	print(line)

print(file.closed)	#False
file.close()

#good practice and automatically closes file
with open('test_rich.txt', 'r') as file:
	contents = file.read()

print(contents)
print(file.closed)	#True


#json
print('\nJSON\n')

import json

basket = ['apple', 'orange', 'apple', 'pear', 'banana']
contacts = {'rich':749, 'mom':407, 'jim':207}

jsonString = json.dumps(basket)
print(jsonString)

file = open('test_json.txt', 'w')
json.dump(contacts, file)
file.close()

with open('test_json.txt', 'r') as file:
	basket2 = json.load(file)
	
print(basket2['rich'])	#749


#Errors and Exceptions ####################

print("\n## Begin Errors and Exceptions ##\n")


while True:
	try:
		x = int(input("Enter Number: "))
		break
	except ValueError:
		print("Oops! Try again...")

print("Your number: ", x)

#related functionality:
# else, finally, raise

'''

#classes ####################

print("\n## Begin classes ##\n")


class MyClass:
	"""A simple example class"""
	i = 12345
	def getGreeting(self):
		return 'hello world'

#static access
print(MyClass.i)	#12345

#create a new instance
x = MyClass()
print(x.i)	#12345
print(x.getGreeting())	#hello world

greet = x.getGreeting
print(greet())					#hello world

class Coordinates:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
coord = Coordinates(2, 4)
print("location: {}, {}".format(coord.x, coord.y))
# location: 2, 4

#doesn't need a declaration within the class
coord.z = 10
coord.z += 5
print(coord.z)	#15
del coord.z


class Dog:
	kind = 'canine'			#class variable: shared by all instances
	def __init__(self, name):
		self.name = name	#instance variable: unique to each instance
		self.tricks = []
	
	def add_trick(self, trick):
		self.tricks.append(trick)

d = Dog("Fido")
d.add_trick("fetch")
b = Dog("Buddy")
print(d.name, d.kind, d.tricks)

#inheritance
class Puppy(Dog):
	def printName(self):
		print(self.name)
	
p = Puppy("Spot")
print(p.kind)	
p.printName()


class Employee:
	pass
	
john = Employee()
john.name = "John Doe"
john.dept = "HR"
john.salary = 350000


#implementing an iterator for a class
class Reverse:
	"""Iterator for looping backwards"""
	def __init__(self, data):
		self.data = data
		self.index = len(data)
	def __iter__(self):
		return self
	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]	

rev = Reverse('Rich')
for char in rev:
	print(char)	# h c i R


#using a generator to create an iterator
def reverse(data):
	for index in range(len(data)-1, -1, -1):
		yield data[index]
		
for char in reverse('Rich'):
	print(char)	# h c i R



#Standard Library ####################

print("\n## Begin Standard Library ##\n")

#import shutil
#shutil.copyfile('test_copy.txt', 'test_copy2.txt')
#shutil.move('test_copy2.txt', 'test_copy2.txt')

import glob
fileList = glob.glob('*.py')
print(fileList)
# ['Notes.py', 'test.py']

import sys
print("\n", sys.argv, "\n")

sys.stderr.write('Warning, log file not found\n')

#exiting a script
# sys.exit()

#regular expressions
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# ['foot', 'fell', 'fastest']
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
# 'cat in the hat'

#but if simpler needs, use string methods:
'tea for too'.replace('too', 'two')
#'tea for two'


#math

import math
result = math.sqrt(36)

import random
result = random.choice(['apple', 'pear', 'banana'])
print(result)

sample = random.sample(range(100), 10)
print(sample)
# [78, 97, 2, 87, 38, 75, 92, 82, 93, 74]

print(random.random())			#0.26584849652641807
randomInt = random.randrange(6)
print(randomInt)	#4

import statistics
data = [1, 2, 3, 4, 5]
print(statistics.mean(data))			#3.0
print(statistics.median(data))		#3
print(statistics.variance(data))	#2.5


#internet access

from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
	for line in response:
		line = line.decode('utf-8')
		if 'EST' in line or 'EDT' in line:
			print(line)

# Jul. 03, 10:25:06 PM EDT   Eastern Time


#date/time

from datetime import date
now = date.today()
print(now)	# 2017-07-03

timeStr = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(timeStr)
# 07-03-17. 03 Jul 2017 is a Monday on the 03 day of July.

birthday = date(1975, 12, 20)
age = now - birthday
print("Age:", round(age.days/365, 1))


#data compression
import zlib
data = b'witch which has which witches wrist watch'	#b makes it bytes
print(len(data))				#41
compressed = zlib.compress(data)
print(len(compressed))	#37
uncompressed = zlib.decompress(compressed)
print(uncompressed)


#Code timing for performance
from timeit import Timer
length = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(length)


#more formatted output
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]

pprint.pprint(t, width=30)

import textwrap
doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
print(textwrap.fill(doc, width=40))

#templating
from string import Template
t = Template('${village}folk send $$10 to $cause.')
output = t.substitute(village='Nottingham', cause='the ditch fund')
print(output)	#Nottinghamfolk send $10 to the ditch fund.
print("\n")


#Multi-Threading
import threading

class AsyncDoer(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.i = 1
	def run(self):
		while self.i<5:
			print(self.i)
			self.i += 1

background = AsyncDoer()
background.start()
print("\nThis is the main program.", end='')
background.join()
print("Main program waited until background completed.")

'''
1
This is the main program.
2
3
4
Main program waited until background completed.
'''

print("\n")


#logging

import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


#arrays
from array import array
a = array('H', [4000, 10, 700, 22222])
total = sum(a)
print(total)	#26932
print(a[1])		#10

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print(d.popleft())	#task1
print(d)	#deque(['task2', 'task3', 'task4'])

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)
#[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]


#money with decimals
#5% tax on 70 cents
from decimal import *
decimalResult = round(Decimal('0.70') * Decimal('1.05'), 2)
print(decimalResult)	#0.74
floatResult = round(0.70 * 1.05, 2)
print(floatResult)		#0.73 - incorrect for money

