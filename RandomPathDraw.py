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
	image = draw_random()
	#image.show()
	imageView_drawing.image = image

#init ##########################################

button_draw.action = button_draw_tapped

fillColor = "red"
drawColor = "#ca2424"


#functions ##########################################

def getRandomLength():
	return random.randint(border, canvasWidth - border * 2)
	
	
def getRandomColor():
	return random.randint(1, 100) / 100.0
	

def draw_random():
	with ui.ImageContext(canvasWidth, canvasHeight) as imageContext:
		
		rect = ui.Path.rect(border, border, canvasWidth - border*2, canvasHeight - border*2)
		ui.set_color("white")
		rect.fill()
		
		path = ui.Path()
		center = ui.Point(250, 250)
		path.move_to(center.x, center.y)		
		
		drawLoop = random.randint(3, 100)
		
		for i in range(drawLoop):
			path.line_to(getRandomLength(), getRandomLength())
		
		path.close()
		
		r = getRandomColor()
		g = getRandomColor()
		b = getRandomColor()
		fillColor = (r, g, b)
		ui.set_color(fillColor)
		path.fill()
		
		drawColor = (r-0.1, g-0.1, b-0.1)
		ui.set_color(drawColor)
		path.stroke()
		
		return imageContext.get_image()



#main ##########################################

mainWindow.add_subview(imageView_drawing)
mainWindow.add_subview(button_draw)
mainWindow.present('sheet')

################################################
