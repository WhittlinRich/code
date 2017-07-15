import canvas
import random
from math import pi
from math import sin, cos, radians


w = h = 500
canvas.set_size(w, h)
originX = w/2
originY = h/2

canvas.set_fill_color(0.8, 0.6, 0.1)
border = 10
canvas.fill_ellipse(border, border, w - border*2, h - border*2)
canvas.set_fill_color(1.0, 0.8, 0.3)
canvas.fill_ellipse(15, 15, w-30, h-30)
canvas.set_fill_color(0.0, 0.0, 0.0)
canvas.fill_ellipse(originX - 5, originY - 5, 10, 10)

for i in range(12):
	canvas.save_gstate()
	canvas.translate(250, 250)
	canvas.rotate(-2 * pi / 12.0 * i)
	canvas.set_fill_color(0.3, 0.3, 0.3, 0.6)
	fontSize = 40
	fontName = 'Helvetica-Bold'
	number = str(12 if i == 0 else i)
	width, height = canvas.get_text_size(number, fontName, fontSize)
	canvas.draw_text(number, -width/2, 190, fontName, fontSize)
	canvas.restore_gstate()



'''
for i in range(12):
	canvas.save_gstate()
	canvas.set_fill_color(0.3, 0.3, 0.3, 0.6)
	fontSize = 40
	fontName = 'Helvetica-Bold'
	number = str(12 if i == 0 else i)
	width, height = canvas.get_text_size(number, fontName, fontSize)
	hour = i
	angle = -2 * pi / 12.0 * (hour - 3)
	length = 210
	rads = radians(angle)
	x = int(cos(angle) * length) + originX
	y = int(sin(angle) * length) + originY
	canvas.draw_text(number, x - 16, y - 22, fontName, fontSize)
	canvas.restore_gstate()
'''	

						
def drawHand(width, length, angle):
	rads = radians(angle)
	endX = int(cos(angle) * length) + originX
	endY = int(sin(angle) * length) + originY
	canvas.set_line_width(width)
	canvas.draw_line(originX, originY, endX, endY)			

canvas.set_stroke_color(0.0, 0.0, 0.0, 0.6)
hourHandLength = 140
minuteHandLength = 190

def setTime(hour, minute):
	hour += minute / 60
	hourAngle = -2 * pi / 12.0 * (hour - 3)
	drawHand(7, hourHandLength, hourAngle)
	
	adjustedMinute = (minute / 60) * 12
	minuteAngle = -2 * pi / 12.0 * (adjustedMinute - 3)
	drawHand(3, minuteHandLength, minuteAngle)


hour = random.randint(1, 12)
minute = random.randrange(0, 59, 5)
setTime(hour, minute)
#setTime(7, 45)


userInput = input("What time is it? ")
if userInput == str(hour) + ":" + str(minute).zfill(2):
	print("Correct!")
else:
	print("Incorrect.")
