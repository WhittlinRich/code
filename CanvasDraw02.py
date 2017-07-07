import canvas
import random
from math import pi

w = h = 500
canvas.set_size(w, h)


canvas.set_fill_color(0.4, 0, 0)
canvas.fill_ellipse(0, 0, w, h)
canvas.set_fill_color(0.8, 0, 0)
canvas.fill_ellipse(20, 20, w-40, h-40)


#gradient circles
r = 1.0
x = 50
y = 50
width = 400
height = 400
#canvas.translate(50, 50)
for i in range(30):
	canvas.set_fill_color(r, 0.0, 0.0, 0.5)
	canvas.fill_ellipse(x, y, width, height)
	r -= 0.03
	x += 5
	y += 5
	width -= 10
	height -= 10
	
		
#random dots		
canvas.begin_updates()
for i in range(12):
	canvas.save_gstate()
	canvas.translate(250,250)
	canvas.rotate(-2 * pi / 12.0 * i)			
	for j in range(0, 20):
		randomIntX = random.randrange(0, 40)
		randomIntY = random.randrange(0, 40)
		randomColor = random.random()
		x = randomIntX
		y = randomIntY
		canvas.set_fill_color(randomColor, randomColor, randomColor, 0.2)
		canvas.fill_ellipse(x, y, 4, 4)			
	canvas.restore_gstate()
canvas.end_updates()	


#overlaping rectangles in circle
for i in range(12):
	canvas.save_gstate()
	canvas.set_fill_color(0.4, 0.4, 0.8, 0.1)
	canvas.translate(250,250)
	canvas.rotate(-2 * pi / 12.0 * i)			
	canvas.fill_rect(0, 0, 40, 40)
	canvas.restore_gstate()
	

#fanning-out 	
canvas.set_stroke_color(0.3, 0.3, 0.3, 0.6)
originX = w/2
originY = h/2
	
for i in range(1, 500, 5):
	x1 = originX
	y1 = originY
	x2 = i
	y2 = 0
	canvas.draw_line(x1, y1, x2, y2)
	
for i in range(1, 500, 5):
	x1 = originX
	y1 = originY
	x2 = i
	y2 = canvas.get_size()[0]
	canvas.draw_line(x1, y1, x2, y2)
	

#crossing lines of circles
canvas.set_fill_color(0.2, 0.3, 0.2, 0.5)
	
for i in range(40, 460, 20):
	x = i + 5
	y = originY - 5
	canvas.fill_ellipse(x, y, 10, 10)	
	
for i in range(40, 460, 20):
	x = originX - 5
	y = i + 5
	canvas.fill_ellipse(x, y, 10, 10)


#small diamonds in circle
for i in range(12):
	canvas.save_gstate()
	canvas.set_fill_color(0.4, 0.4, 0.8, 0.4)
	canvas.translate(250,250)
	canvas.rotate(-2 * pi / 12.0 * i)			
	canvas.fill_rect(110, 110, 20, 20)
	canvas.restore_gstate()
	
for i in range(12):
	canvas.save_gstate()
	canvas.set_fill_color(0.4, 0.4, 0.8, 0.4)
	canvas.translate(250,250)
	canvas.rotate(-2 * pi / 12.0 * i)			
	canvas.fill_rect(115, 115, 10, 10)
	canvas.restore_gstate()	
			

#outer ovals
width = 35
height = 15
for i in range(12):
	canvas.save_gstate()
	canvas.translate(250, 250)
	canvas.rotate(-2 * pi / 12.0 * i)
	canvas.set_fill_color(0.2, 0.4, 0.3)
	canvas.fill_ellipse(-width/2, 232, width, height)
	canvas.restore_gstate()
	

width = 30
height = 10
for i in range(12):
	canvas.save_gstate()
	canvas.translate(250, 250)
	canvas.rotate(-2 * pi / 12.0 * i)
	canvas.set_fill_color(0.1, 0.2, 0.2)
	canvas.fill_ellipse(-width/2, 234, width, height)
	canvas.restore_gstate()
	
