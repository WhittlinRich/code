import canvas
import random
from math import pi

canvasWidth = canvasHeight = 500
canvas.set_size(canvasWidth, canvasHeight)


x = 10
y = 10
w = 50
h = 50
r = b = g = 1.0

for i in range(8):
	for j in range(8):
		r -= 0.01
		b = 0.0
		g = 0.0
		canvas.set_fill_color(r, b, g)
		canvas.fill_rect(x, y, w, h)
		y += 60
	x += 60
	y = 10


x = 15
y = 15
w = 40
h = 40

colors = [(0.545, 0.271, 0.075), (0.545, 0.000, 0.000), (1.000, 0.647, 0.000), (0.933, 0.910, 0.667),
(0.000, 0.392, 0.000), (0.529, 0.808, 0.922), (000, 0.000, 0.545)]

for i in range(8):
	for j in range(8):
		color = random.choice(colors)
		r = color[0]
		b = color[1]
		g = color[2]
		canvas.set_fill_color(r, b, g)
		canvas.fill_rect(x, y, w, h)
		y += 60
	x += 60
	y = 15



x = 20
y = 20
w = 30
h = 30

for i in range(8):
	for j in range(8):
		r = random.uniform(0.5, 0.9)
		b = random.uniform(0.5, 0.9)
		g = random.uniform(0.5, 0.9)
		canvas.set_fill_color(r, b, g)
		canvas.fill_rect(x, y, w, h)
		y += 60
	x += 60
	y = 20


x = 25
y = 25
w = 20
h = 20

for i in range(8):
	for j in range(8):
		r = random.random()
		b = random.random()
		g = random.random()
		canvas.set_fill_color(r, b, g)
		canvas.fill_rect(x, y, w, h)
		y += 60
	x += 60
	y = 25



