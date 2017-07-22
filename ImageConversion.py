import ui
from PIL import Image as ImageP
import io
import random

mainWindow = ui.View()
mainWindow.name = 'Image Conversion'
mainWindow.background_color = 'white'
mainWindow.width = 700 #ui.get_screen_size().width
mainWindow.height = 700 #ui.get_screen_size().height


def pil2ui(pil_img):
	with io.BytesIO() as buffer:
		pil_img.save(buffer, format='PNG')
		return ui.Image.from_data(buffer.getvalue())

path = "../Images/"		
quarter = pil2ui(ImageP.open(path + "quarter.png").resize((70,70), ImageP.ANTIALIAS))
dime = pil2ui(ImageP.open(path + "dime.png").resize((50,50), ImageP.ANTIALIAS))
nickel = pil2ui(ImageP.open(path + "nickel.png").resize((60,60), ImageP.ANTIALIAS))
penny = pil2ui(ImageP.open(path + "penny.png").resize((55,55), ImageP.ANTIALIAS))


picture1 = ui.ImageView()
picture1.width = 70
picture1.height = 70	
picture1.image = quarter
		
mainWindow.add_subview(picture1)

#mainWindow.present('fullscreen')
mainWindow.present('sheet')
