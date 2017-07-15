import canvas
import random
from math import pi
from math import sin, cos, radians

print('\nTelling Time.')

w = h = 500
canvas.set_size(w, h)
clockWidth = clockHeight = 300
centerX = w/2
centerY = h/2
clockX = centerX - clockWidth/2
clockY = centerY - clockHeight/2
border = 10


def drawClockBackground():
	canvas.set_fill_color(0.8, 0.6, 0.1)
	canvas.fill_ellipse(clockX - border, clockY - border, clockWidth + border*2, clockHeight + border*2)
	canvas.set_fill_color(1.0, 0.8, 0.3)
	canvas.fill_ellipse(clockX, clockY, clockWidth, clockHeight)
	canvas.set_fill_color(0.0, 0.0, 0.0)
	canvas.fill_ellipse(centerX - 5, centerY - 5, 10, 10)
		

def drawNumbers2():
	for i in range(12):
		canvas.save_gstate()
		canvas.translate(centerX, centerY)
		canvas.rotate(-2 * pi / 12.0 * i)
		canvas.set_fill_color(0.3, 0.3, 0.3, 0.6)
		fontSize = 30
		fontName = 'Helvetica-Bold'
		number = str(12 if i == 0 else i)
		width, height = canvas.get_text_size(number, fontName, fontSize)
		canvas.draw_text(number, -width/2, 115, fontName, fontSize)
		canvas.restore_gstate()


def drawNumbers():
	for i in range(12):
		canvas.save_gstate()
		canvas.set_fill_color(0.3, 0.3, 0.3, 0.6)
		fontSize = 30
		fontName = 'Helvetica-Bold'
		number = str(12 if i == 0 else i)
		width, height = canvas.get_text_size(number, fontName, fontSize)
		hour = i
		angle = -2 * pi / 12.0 * (hour - 3)
		length = clockWidth * 0.43
		rads = radians(angle)
		x = int(cos(angle) * length) + centerX
		y = int(sin(angle) * length) + centerY
		canvas.draw_text(number, x - width/2, y - height/2, fontName, fontSize)
		canvas.restore_gstate()
		
def drawMajorTickmarks2():
	for i in range(12):
		canvas.save_gstate()
		canvas.set_fill_color(0.3, 0.3, 0.3, 0.6)		
		width = height = 5
		angle = -2 * pi / 12.0 * (i - 3)
		length = clockWidth * 0.52
		rads = radians(angle)
		x = int(cos(angle) * length) + centerX
		y = int(sin(angle) * length) + centerY
		canvas.draw_rect(x - width/2, y - height/2, width, height)
		canvas.restore_gstate()		


def drawMajorTickmarks():
	for i in range(12):
		canvas.save_gstate()
		canvas.translate(centerX, centerY)
		canvas.rotate(-2 * pi / 12.0 * i)
		canvas.set_fill_color(0.4, 0.4, 0.4, 0.6)
		width = 2
		height = 7
		canvas.set_line_width(3)
		canvas.draw_rect(-width/2, clockWidth * 0.505, width, height)
		canvas.restore_gstate()
		
def drawMinorTickmarks():
	for i in range(60):
		canvas.save_gstate()
		canvas.translate(centerX, centerY)
		canvas.rotate(-2 * pi / 60.0 * i)
		canvas.set_fill_color(0.4, 0.4, 0.4, 0.6)
		width = 1
		height = 5
		canvas.set_line_width(1)
		canvas.draw_rect(-width/2, clockWidth * 0.505, width, height)
		canvas.restore_gstate()		
				
								
def drawHand(width, length, angle):
	rads = radians(angle)
	endX = int(cos(angle) * length) + centerX
	endY = int(sin(angle) * length) + centerY
	canvas.save_gstate()
	canvas.set_stroke_color(0.0, 0.0, 0.0, 0.6)
	canvas.set_line_width(width)
	canvas.draw_line(centerX, centerY, endX, endY)			
	canvas.restore_gstate()

def setTime(hour, minute):
	hourHandLength = clockWidth * 0.33 #90
	minuteHandLength = clockWidth * 0.48 #112
	
	hour += minute / 60
	hourAngle = -2 * pi / 12.0 * (hour - 3)
	drawHand(7, hourHandLength, hourAngle)
	
	adjustedMinute = (minute / 60) * 12
	minuteAngle = -2 * pi / 12.0 * (adjustedMinute - 3)
	drawHand(3, minuteHandLength, minuteAngle)



totalCorrect = 0
totalWrong = 0
totalQuestions = 5
minuteStep = 5

userInput = input("How many would you like? ")
if userInput.isdigit():
	totalQuestions = int(userInput)

userInput = input("Increments of 1 or 5? ")
if userInput.isdigit() and int(userInput) == 1:
	minuteStep = 1

for i in range(totalQuestions):
	
	drawClockBackground()
	drawNumbers()
	drawMajorTickmarks()
	drawMinorTickmarks()
	
	hour = random.randint(1, 12)
	minute = random.randrange(0, 59, minuteStep)
	setTime(hour, minute)
	#setTime(7, 45)	
	

	userInput = input("What time is it? ")
	if userInput == str(hour) + ":" + str(minute).zfill(2):
		totalCorrect += 1
		print("Correct!")
	else:
		totalWrong += 1
		print("Incorrect.")


print("Your score: {0} out of {1}".format(totalCorrect, totalQuestions))
print(round((totalCorrect/totalQuestions) * 100), "%")
if(totalCorrect == totalQuestions):
	print("Perfect score!")
