import ui
import random

# main window ##################################

mainWindow = ui.View()
mainWindow.name = 'Random Drawing'
mainWindow.background_color = 'white'
windowWidth = 540
windowHeight = 540
mainWindow.width = windowWidth 
mainWindow.height = windowHeight
canvasWidth = 500
canvasHeight = 500
border = 10

# ui components ################################

imageView_drawing = ui.ImageView()
imageView_drawing.width = canvasWidth
imageView_drawing.height = canvasHeight
imageView_drawing.center = (windowWidth/2, windowHeight/2 - 20)
imageView_drawing.border_width = 1


button_draw = ui.Button()
button_draw.width = 70
button_draw.height = 32
button_draw.center = (windowWidth/2, windowHeight - 20)
button_draw.title = "Draw"
button_draw.border_color = "#dcdcdc"
button_draw.border_width = 1


#UI Actions ##########################################

def button_draw_tapped(sender):
	image = drawRandom()
	#image.show()
	imageView_drawing.image = image
	

#init ##########################################

button_draw.action = button_draw_tapped


#functions ##########################################

	
def getRandomColor():
	return random.randint(1, 100) / 100.0
		

def drawRandom():
	with ui.ImageContext(canvasWidth, canvasHeight) as imageContext:
		
		rect = ui.Path.rect(border, border, canvasWidth - border*2, canvasHeight - border*2)
		ui.set_color("white")
		rect.fill()
		
		shapeType = random.choice(("rect", "oval"))
		
		for i in range(40000):
			x = random.randint(-10, canvasWidth - 10)
			y = random.randint(-10, canvasHeight - 10)
			w = random.randint(2, 20)
			h = random.randint(2, 20)
			
			if(shapeType == "rect"):
				shape = ui.Path.rect(x, y, w, h)
			else:
				shape = ui.Path.oval(x, y, w, h)
					
			r = getRandomColor()
			g = getRandomColor()
			b = getRandomColor()
			fillColor = (r, g, b)
			ui.set_color(fillColor)
			shape.fill()

			drawColor = (r-0.1, g-0.1, b-0.1)
			ui.set_color(drawColor)
			shape.stroke()
		
				
		return imageContext.get_image()



#main ##########################################

mainWindow.add_subview(imageView_drawing)
mainWindow.add_subview(button_draw)
mainWindow.present('sheet')

################################################
