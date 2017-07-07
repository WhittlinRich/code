import canvas
import random
from math import pi

w = h = 500
canvas.set_size(w, h)

canvas.set_aa_enabled(True)
canvas.set_fill_color(0.4, 0, 0)
canvas.fill_ellipse(0, 0, w, h)
canvas.set_fill_color(0.8, 0, 0)
canvas.fill_ellipse(20, 20, w-40, h-40)

#canvas.draw_text("Computer Generated Art", 65, 440, font_size=33)

originX = w/2
originY = h/2
	

for i in range(1, 300, 5):
	x1 = originX
	y1 = originY
	x2 = 100 + i
	y2 = 0
	canvas.draw_line(x1, y1, x2, y2)
	
for i in range(1, 500, 5):
	x1 = originX
	y1 = originY
	x2 = i
	y2 = canvas.get_size()[0]
	canvas.draw_line(x1, y1, x2, y2)
	

canvas.set_fill_color(0, 0.7, 0)
	
for i in range(40, 460, 20):
	x = i + 5
	y = originY - 5
	canvas.fill_rect(x, y, 10, 10)	
	
for i in range(40, 460, 20):
	x = originX - 5
	y = i + 5
	canvas.fill_rect(x, y, 10, 10)
		
canvas.set_fill_color(0.5, 0, 0, 0.5)

for i in range(12):
	canvas.save_gstate()
	canvas.set_fill_color(0.4, 0.4, 0.8, 0.4)
	canvas.translate(250,250)
	canvas.rotate(-2 * pi / 12.0 * i)			
	canvas.fill_rect(0, 0, 120, 120)
	canvas.restore_gstate()


canvas.begin_updates()
for i in range(12):
	canvas.save_gstate()
	canvas.translate(250,250)
	canvas.rotate(-2 * pi / 12.0 * i)			
	for j in range(0, 80):
		randomIntX = random.randrange(0, 160)
		randomIntY = random.randrange(0, 160)
		randomColor = random.random()
		x = randomIntX
		y = randomIntY
		canvas.set_fill_color(randomColor, randomColor, randomColor, 0.4)
		canvas.fill_ellipse(x, y, 4, 4)			
	canvas.restore_gstate()
canvas.end_updates()


width = 20
height = 20	
for i in range(12):
	canvas.save_gstate()
	canvas.translate(250, 250)
	canvas.rotate(-2 * pi / 12.0 * i)
	canvas.set_fill_color(0.3, 0.6, 0.3)
	canvas.fill_rect(-width/2, 220, width, height)
	canvas.restore_gstate()

