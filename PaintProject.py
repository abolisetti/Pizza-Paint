#PaintProject.py
#Arvind Bolisetti
#This is a paint program, meant to perform many of the same functions as MS Paint.
#Theme: Pizza. You can make a pizza with the blank pizza and the other ingredients.
#List of draw tools: Pencil, Eraser, Brush, Marker, and Blur.
#List of shapes: Filled, Unfilled Rectangle and Ellipse, Line, Rhombus, Pentagon, Hexagon, Four point star, Five point star, Six point star, and lightning bolt.
#List of complex tools: Floodfill
#List of screen filters: sepia, invert, grayscale, xray, and tint.
#Number of stamps: 22
#Other: Save, Load, Redo, Undo, Clear, and Canvas Fill.

from pygame import *#All the different imports
from random import *
from math import *
from tkinter import *
import os

#screen = display.set_mode((1100, 800))

running = True

init()

inf = display.Info()
w, h = inf.current_w, inf.current_h
os.environ['SDL_VIDEO_WINDOW_POS'] = '25, 75'#What it does is that it makes it so that the program always opens at a specific part of the computer so
                                             #that you dont have to drag it to move around everytime you work on it. If ur comp is too small you can also use it to work on parts u cant see.
                                             #cant use it for real because it messes up the save and load tools.

screen = display.set_mode((1100, 800))
display.set_caption("Pizza Paint")

root = Tk()#Removes tk window                                 
root.withdraw()

white=(255, 255, 255, 255)
black=(0, 0, 0, 255)#All these have alpha values so that marker and ellipse tool can work.
red=(255, 0, 0, 255)
green=(0, 0, 255, 255)#Used green at first, but felt like using blue after. Did not want to change the name in everything so I just changed color of it
color=black

tool=""#Need to have tool defined as nothing here.
tooltext="You got nothing selected right now."#At first all the tooltext variables were to be explanations for the user but I couldn't figure out how to blit text.
x, y=0, 0#X and Y are the start coordinates of all shape tools such as line, rhombus, etc.
#--------------------------------Image Images-----------------------------------
#These images are blit here because if they were placed later they would cover the other images and rects.
background = image.load("Images/pizzaBack.jpg")
background = transform.smoothscale(background, (1100, 880))
screen.blit(background, (0, 0))

logo = image.load("Images/logo.png")
screen.blit(logo, (320, 0))

ingredients = image.load("Images/ingredients.png")
ingredients = transform.smoothscale(ingredients, (320, 243))
screen.blit(ingredients, (780, 2))

toolbox = image.load("Images/toolbox.png")
toolbox = transform.smoothscale(toolbox, (126, 610))
screen.blit(toolbox, (2, 2))
#--------------------------------Tools------------------------------------------
#Tool Rects
toolboxRect=Rect(19, 59, 92, 651)#These toolbox rects and blitbox rects are so that when you change the tools, it will blit these rectangles.  
blitboxRect=Rect(799, 59, 282, 200)#It takes a picture of them before everything starts, and then blits on to screen when u change tools.
colorboxRect=Rect(0, 615, 1100, 185)

pencilRect=Rect(20, 60, 40, 40)#All tools are usually called what they are + Rect. This allows for easy copy and pasting when getting icons.
eraserRect=Rect(70, 60, 40, 40)
brushRect=Rect(20, 110, 40, 40)

dropRect=Rect(20, 160, 40, 40)
sprayRect=Rect(70, 160, 40, 40)

rectRect=Rect(20, 210, 40, 40)
filledRectRect=Rect(70, 210, 40, 40)
ellipseRect=Rect(20, 260, 40, 40)
filledEllipseRect=Rect(70, 260, 40, 40)
lineRect=Rect(20, 310, 40, 40)

rhombusRect=Rect(70, 310, 40, 40)
pentagonRect=Rect(20, 360, 40, 40)
hexagonRect=Rect(70, 360, 40, 40)

horizontalArrowRect=Rect(20, 410, 40, 40)
verticalArrowRect=Rect(70, 410, 40, 40)

fourStarRect=Rect(20, 460, 40, 40)
fiveStarRect=Rect(70, 460, 40, 40)
sixStarRect=Rect(20, 510, 40, 40)

boltRect=Rect(70, 510, 40, 40)

floodfillRect=Rect(20, 560, 40, 40)
blurRect=Rect(70, 560, 40, 40)

markerRect=Rect(70, 110, 40, 40)

#Other Rects
clearRect=Rect(790, 495, 70, 35)#These other rects are all buttons except bucket. Its calle bucket but its actaully the fill canvas tool. I had it as bucket to begin with
bucketRect=Rect(790, 545, 70, 35)#and it was hard to change so I left as is.
saveRect=Rect(900, 495, 70, 35)
loadRect=Rect(900, 545, 70, 35)
undoRect=Rect(1010, 495, 70, 35)
redoRect=Rect(1010, 545, 70, 35)

#Bitmap Rects
##First Row
#Same row, y+40
#Same column, x+45
blankPizzaRect=Rect(800, 60, 80, 80)
realPizzaRect=Rect(800, 150, 80, 80)

pepperoniRect=Rect(885, 60, 35, 35)
mushroomRect=Rect(885, 105, 35, 35)

blackOliveRect=Rect(925, 60, 35, 35)
greenPepperRect=Rect(925, 105, 35, 35)

baconRect=Rect(965, 60, 35, 35)
fishRect=Rect(965, 105, 35, 35)

greenOliveRect=Rect(1005, 60, 35, 35)
pineappleRect=Rect(1005, 105, 35, 35)

shrimpRect=Rect(1045, 60, 35, 35)
tomatoRect=Rect(1045, 105, 35, 35)#105+35+10=150

##Second Row
cheeseRect=Rect(885, 150, 35, 35)
cucumberRect=Rect(885, 195, 35, 35)

egg1Rect=Rect(925, 150, 35, 35)
egg2Rect=Rect(925, 195, 35, 35)

flatThingRect=Rect(965, 150, 35, 35)
greenChilliRect=Rect(965, 195, 35, 35)

meat1Rect=Rect(1005, 150, 35, 35)
meat2Rect=Rect(1005, 195, 35, 35)

redChilliRect=Rect(1045, 150, 35, 35)
sausageRect=Rect(1045, 195, 35, 35)

#Color Rects
paletteRect=Rect(130, 620, 650, 100)#These rects are for the 2 palettes, the current color, and the two color options
currentColorRect=Rect(10, 730, 110, 40)
grayscaleRect=Rect(130, 730, 650, 40)
randomColorRect=Rect(790, 730, 140, 40)
rainbowRect=Rect(940, 730, 140, 40)

#Filter Rects
sepiaRect=Rect(790, 620, 50, 100)#These are screen filters
xrayRect=Rect(970, 620, 50, 100)
invertRect=Rect(850, 620, 50, 100)
grayRect=Rect(1030, 620, 50, 100)
tintRect=Rect(910, 620, 50, 100)

#Canvas Rects
canvasRect=Rect(130, 60, 650, 550)
draw.rect(screen, black, canvasRect, 5)
draw.rect(screen, white, canvasRect, 0)

#draw.rect(screen, white, toolboxRect, 0)
#-------------------------------------------------------------------------------
def floodfill():
    mx, my=mouse.get_pos()
    newColor=color
    
    oldColor=screen.get_at((mx, my))#This variable is to get the color of where you click
    if newColor == oldColor:        #If you try to do fill it with the color you selected, it will do nothing
        return 0
    oldList = []
    oldList.append((mx, my))         #So that the place where you click will get put into the list
    while len(oldList) > 0:         #When there is no more coordinates in the list, it will stop
        x, y = oldList.pop()        
        if canvasRect.collidepoint(x, y) and screen.get_at((x, y)) == oldColor: #So that it stops if its outside of the canvas, 
                                                                                #and so that it will start if the color is same 
            screen.set_at((x, y), newColor)                                     
            oldList+=[(x+1, y), (x-1, y), (x, y+1), (x, y-1)]                   #Checks in all 4 directions
            
#--------------------------------Tool/Cursor Images-----------------------------
#These are images for all the draw tools or shapes. Mainly everything in the tool box section.
colors = image.load("Images/colors.jpg")
colors = transform.smoothscale(colors, (650, 100))
screen.blit(colors, (130, 620))

grayscale = image.load("Images/grayscale.jpg")
grayscale = transform.smoothscale(grayscale, (650, 40))
screen.blit(grayscale, (130, 730))

pencil = image.load("Images/pencil.png")
pencil = transform.scale(pencil, (40, 40))
screen.blit(pencil, (20, 60))

eraser = image.load("Images/eraser.png")
eraser = transform.scale(eraser, (40, 40))
screen.blit(eraser, (70, 60))

brush = image.load("Images/brush.png")
brush = transform.scale(brush, (40, 40))
screen.blit(brush, (20, 110))

marker = image.load("Images/marker.png")
marker = transform.scale(marker, (40, 40))
screen.blit(marker, (70, 110))

eyedropper = image.load("Images/eyedropper.jpg")
eyedropper = transform.scale(eyedropper, (40, 40))
screen.blit(eyedropper, (20, 160))

spraycan = image.load("Images/spray.jpg")
spraycan = transform.scale(spraycan, (40, 40))
screen.blit(spraycan, (70, 160))

rectangle = image.load("Images/rectangle.jpg")
rectangle = transform.scale(rectangle, (40, 40))
screen.blit(rectangle, (20, 210))

rectangleFill = image.load("Images/rectFill.png")
rectangleFill = transform.scale(rectangleFill, (40, 40))
screen.blit(rectangleFill, (70, 210))

ellipse = image.load("Images/ellipse.png")
ellipse = transform.scale(ellipse, (40, 40))
screen.blit(ellipse, (20, 260))

ellipseFill = image.load("Images/ellipseFILL.png")
ellipseFill = transform.scale(ellipseFill, (40, 40))
screen.blit(ellipseFill, (70, 260))

line = image.load("Images/line.png")
line = transform.scale(line, (40, 40))
screen.blit(line, (20, 310))
#
rhombus = image.load("Images/rhombus.png")
rhombus = transform.scale(rhombus, (40, 40))
screen.blit(rhombus, (70, 310))

pentagon = image.load("Images/pentagon.png")
pentagon = transform.scale(pentagon, (40, 40))
screen.blit(pentagon, (20, 360))

hexagon = image.load("Images/hexagon.png")
hexagon = transform.scale(hexagon, (40, 40))
screen.blit(hexagon, (70, 360))

horizontalArrow = image.load("Images/horizontalArrow.png")
horizontalArrow = transform.scale(horizontalArrow, (40, 40))
screen.blit(horizontalArrow, (20, 410))

verticalArrow = image.load("Images/verticalArrow.png")
verticalArrow = transform.scale(verticalArrow, (40, 40))
screen.blit(verticalArrow, (70, 410))

fourStar = image.load("Images/fourStar.png")
fourStar = transform.scale(fourStar, (40, 40))
screen.blit(fourStar, (20, 460))

fiveStar = image.load("Images/fiveStar.png")
fiveStar = transform.scale(fiveStar, (40, 40))
screen.blit(fiveStar, (70, 460))

sixStar = image.load("Images/sixStar.png")
sixStar = transform.scale(sixStar, (40, 40))
screen.blit(sixStar, (20, 510))

bolt = image.load("Images/bolt.png")
bolt = transform.scale(bolt, (40, 40))
screen.blit(bolt, (70, 510))

bucket = image.load("Images/bucket.png")
bucket = transform.scale(bucket, (40, 40))
screen.blit(bucket, (20, 560))

blur = image.load("Images/blur.png")
blur = transform.scale(blur, (40, 40))
screen.blit(blur, (70, 560))
#----------------------------- Filters -----------------------------------------
#These are screen filter button images.
sepia = image.load("Images/sepia.png")
sepia = transform.scale(sepia, (50, 100))
screen.blit(sepia, (790, 620))

invert = image.load("Images/invert.png")
invert = transform.scale(invert, (50, 100))
screen.blit(invert, (850, 620))

tint = image.load("Images/tint.png")
tint = transform.scale(tint, (50, 100))
screen.blit(tint, (910, 620))

xray = image.load("Images/xray.png")
xray = transform.scale(xray, (50, 100))
screen.blit(xray, (970, 620))

grayFilter = image.load("Images/grayFilter.png")
grayFilter = transform.scale(grayFilter, (50, 100))
screen.blit(grayFilter, (1030, 620))

#------------------------------ Other ------------------------------------------
#These are the images for the other buttons.
clear = image.load("Images/clear.png")
clear = transform.scale(clear, (70, 35))
screen.blit(clear, (790, 495))

fill = image.load("Images/fill.png")
fill = transform.scale(fill, (70, 35))
screen.blit(fill, (790, 545))

save = image.load("Images/save.png")
save = transform.scale(save, (70, 35))
screen.blit(save, (900, 495))

load = image.load("Images/load.png")
load = transform.scale(load, (70, 35))
screen.blit(load, (900, 545))

undo = image.load("Images/undo.png")
undo = transform.scale(undo, (70, 35))
screen.blit(undo, (1010, 495))

redo = image.load("Images/redo.png")
redo = transform.scale(redo, (70, 35))
screen.blit(redo, (1010, 545))

#----------------------------- Colors  -----------------------------------------
#These ones are for the color options.
random = image.load("Images/random.png")
random = transform.scale(random, (140, 40))
screen.blit(random, (790, 730))

rainbow = image.load("Images/rainbow.png")
rainbow = transform.scale(rainbow, (140, 40))
screen.blit(rainbow, (940, 730))

#----------------------------- Bitmaps -----------------------------------------
#First row
blankPizza = image.load("Images/blankPizza.png")
blankPizzaButton = transform.scale(blankPizza, (75, 75))
blankPizzaBlit = transform.smoothscale(blankPizza, (260, 260))
screen.blit(blankPizzaButton, (800, 60))#800+85=885

realPizza = image.load("Images/realCheesePizza.png")
realPizzaButton = transform.scale(realPizza, (75, 75))
realPizzaBlit = transform.smoothscale(realPizza, (260, 260))
screen.blit(realPizzaButton, (800, 150))

pepperoni = image.load("Images/pepperoni.png")
pepperoniButton = transform.scale(pepperoni, (35, 35))
pepperoniBlit = transform.scale(pepperoni, (40, 40))
screen.blit(pepperoniButton, (885, 60))#885+40=925

mushroom = image.load("Images/mushroom.png")
mushroomButton = transform.scale(mushroom, (35, 35))
mushroomBlit = transform.scale(mushroom, (30, 30))
screen.blit(mushroomButton, (885, 105))

blackOlive = image.load("Images/blackOlive.png")
blackOliveButton = transform.scale(blackOlive, (35, 35))
blackOliveBlit = transform.scale(blackOlive, (20, 20))
screen.blit(blackOliveButton, (925, 60))#925+40=965

greenPepper = image.load("Images/greenPepper.png")
greenPepperButton = transform.scale(greenPepper, (35, 35))
greenPepperBlit = transform.scale(greenPepper, (30, 30))
screen.blit(greenPepperButton, (925, 105))

bacon = image.load("Images/bacon.png")
baconButton = transform.scale(bacon, (35, 35))
baconBlit = transform.scale(bacon, (30, 30))
screen.blit(baconButton, (965, 60))

fish = image.load("Images/fish.png")
fishButton = transform.scale(fish, (35, 35))
fishBlit = transform.scale(fish, (30, 30))
screen.blit(fishButton, (965, 105))#965+40=1005

greenOlive = image.load("Images/greenOlive.png")
greenOliveButton = transform.scale(greenOlive, (35, 35))
greenOliveBlit = transform.scale(greenOlive, (20, 20))
screen.blit(greenOliveButton, (1005, 60))

pineapple = image.load("Images/pineapple.png")
pineappleButton = transform.scale(pineapple, (35, 35))
pineappleBlit = transform.scale(pineapple, (30, 30))
screen.blit(pineappleButton, (1005, 105))

shrimp = image.load("Images/shrimp.png")
shrimpButton = transform.scale(shrimp, (35, 35))
shrimpBlit = transform.scale(shrimp, (30, 30))
screen.blit(shrimpButton, (1045, 60))

tomato = image.load("Images/tomato.png")
tomatoButton = transform.scale(tomato, (35, 35))
tomatoBlit = transform.scale(tomato, (30, 30))
screen.blit(tomatoButton, (1045, 105))


#Second row
cheese = image.load("Images/cheese.png")
cheeseButton = transform.scale(cheese, (35, 35))
cheeseBlit = transform.scale(cheese, (30, 30))
screen.blit(cheeseButton, (885, 150))

cucumber = image.load("Images/cucumber.png")
cucumberButton = transform.scale(cucumber, (35, 35))
cucumberBlit = transform.scale(cucumber, (30, 30))
screen.blit(cucumberButton, (885, 195))

egg1 = image.load("Images/egg1.png")
egg1Button = transform.scale(egg1, (35, 35))
egg1Blit = transform.scale(egg1, (30, 30))
screen.blit(egg1Button, (925, 150))

egg2 = image.load("Images/egg2.png")
egg2Button = transform.scale(egg2, (35, 35))
egg2Blit = transform.scale(egg2, (30, 30))
screen.blit(egg2Button, (925, 195))

flatThing = image.load("Images/flatThing.png")
flatThingButton = transform.scale(flatThing, (35, 35))
flatThingBlit = transform.scale(flatThing, (30, 30))
screen.blit(flatThingButton, (965, 150))

greenChilli = image.load("Images/greenChilli.png")
greenChilliButton = transform.scale(greenChilli, (35, 35))
greenChilliBlit = transform.scale(greenChilli, (30, 30))
screen.blit(greenChilliButton, (965, 195))

meat1 = image.load("Images/meat1.png")
meat1Button = transform.scale(meat1, (35, 35))
meat1Blit = transform.scale(meat1, (30, 30))
screen.blit(meat1Button, (1005, 150))

meat2 = image.load("Images/meat2.png")
meat2Button = transform.scale(meat2, (35, 35))
meat2Blit = transform.scale(meat2, (30, 30))
screen.blit(meat2Button, (1005, 195))

redChilli = image.load("Images/redChilli.png")
redChilliButton = transform.scale(redChilli, (35, 35))
redChilliBlit = transform.scale(redChilli, (30, 30))
screen.blit(redChilliButton, (1045, 150))

sausage = image.load("Images/sausage.png")
sausageButton = transform.scale(sausage, (35, 25))
sausageBlit = transform.scale(sausage, (30, 20))
screen.blit(sausageButton, (1045, 200))
#--------------------------- Tool Help Pics ------------------------------------
#These are toolhelp pics, and they explain to the user how to use the program. I did not know how to put text on the screen,
#so I did it like this instead.
pencilHelp = image.load("ToolHelpPics/pencilHelp.png")
pencilHelp = transform.smoothscale(pencilHelp, (300, 230))

eraserHelp = image.load("ToolHelpPics/eraserHelp.png")
eraserHelp = transform.smoothscale(eraserHelp, (300, 230))

brushHelp = image.load("ToolHelpPics/brushHelp.png")
brushHelp = transform.smoothscale(brushHelp, (300, 230))

markerHelp = image.load("ToolHelpPics/markerHelp.png")
markerHelp = transform.smoothscale(markerHelp, (300, 230))

rectangleHelp = image.load("ToolHelpPics/rectangleHelp.png")
rectangleHelp = transform.smoothscale(rectangleHelp, (300, 230))

filledRectangleHelp = image.load("ToolHelpPics/filledRectangleHelp.png")
filledRectangleHelp = transform.smoothscale(filledRectangleHelp, (300, 230))


sprayHelp = image.load("ToolHelpPics/sprayHelp.png")
sprayHelp = transform.smoothscale(sprayHelp, (300, 230))

dropHelp = image.load("ToolHelpPics/dropHelp.png")
dropHelp = transform.smoothscale(dropHelp, (300, 230))

rhombusHelp = image.load("ToolHelpPics/rhombusHelp.png")
rhombusHelp = transform.smoothscale(rhombusHelp, (300, 230))

pentagonHelp = image.load("ToolHelpPics/pentagonHelp.png")
pentagonHelp = transform.smoothscale(pentagonHelp, (300, 230))

ellipseHelp = image.load("ToolHelpPics/ellipseHelp.png")
ellipseHelp = transform.smoothscale(ellipseHelp, (300, 230))

ellipseFillHelp = image.load("ToolHelpPics/ellipseFillHelp.png")
ellipseFillHelp = transform.smoothscale(ellipseFillHelp, (300, 230))


hexagonHelp = image.load("ToolHelpPics/hexagonHelp.png")
hexagonHelp = transform.smoothscale(hexagonHelp, (300, 230))

fourStarHelp = image.load("ToolHelpPics/fourStarHelp.png")
fourStarHelp = transform.smoothscale(fourStarHelp, (300, 230))

fiveStarHelp = image.load("ToolHelpPics/fiveStarHelp.png")
fiveStarHelp = transform.smoothscale(fiveStarHelp, (300, 230))

sixStarHelp = image.load("ToolHelpPics/sixStarHelp.png")
sixStarHelp = transform.smoothscale(sixStarHelp, (300, 230))

horizontalArrowHelp = image.load("ToolHelpPics/horizontalArrowHelp.png")
horizontalArrowHelp = transform.smoothscale(horizontalArrowHelp, (300, 230))

verticalArrowHelp = image.load("ToolHelpPics/verticalArrowHelp.png")
verticalArrowHelp = transform.smoothscale(verticalArrowHelp, (300, 230))


boltHelp = image.load("ToolHelpPics/boltHelp.png")
boltHelp = transform.smoothscale(boltHelp, (300, 230))

floodfillHelp = image.load("ToolHelpPics/floodfillHelp.png")
floodfillHelp = transform.smoothscale(floodfillHelp, (300, 230))

blurHelp = image.load("ToolHelpPics/blurHelp.png")
blurHelp = transform.smoothscale(blurHelp, (300, 230))

clearHelp = image.load("ToolHelpPics/clearHelp.png")
clearHelp = transform.smoothscale(clearHelp, (300, 230))

fillcanvasHelp = image.load("ToolHelpPics/fillcanvasHelp.png")
fillcanvasHelp = transform.smoothscale(fillcanvasHelp, (300, 230))

undoHelp = image.load("ToolHelpPics/undoHelp.png")
undoHelp = transform.smoothscale(undoHelp, (300, 230))


redoHelp = image.load("ToolHelpPics/redoHelp.png")
redoHelp = transform.smoothscale(redoHelp, (300, 230))

saveHelp = image.load("ToolHelpPics/saveHelp.png")
saveHelp = transform.smoothscale(saveHelp, (300, 230))

loadHelp = image.load("ToolHelpPics/loadHelp.png")
loadHelp = transform.smoothscale(loadHelp, (300, 230))

sepiaFilterHelp = image.load("ToolHelpPics/sepiaFilterHelp.png")
sepiaFilterHelp = transform.smoothscale(sepiaFilterHelp, (300, 230))

xrayFilterHelp = image.load("ToolHelpPics/xrayFilterHelp.png")
xrayFilterHelp = transform.smoothscale(xrayFilterHelp, (300, 230))

grayscaleFilterHelp = image.load("ToolHelpPics/grayscaleFilterHelp.png")
grayscaleFilterHelp = transform.smoothscale(grayscaleFilterHelp, (300, 230))


invertFilterHelp = image.load("ToolHelpPics/invertFilterHelp.png")
invertFilterHelp = transform.smoothscale(invertFilterHelp, (300, 230))

tintHelp = image.load("ToolHelpPics/tintHelp.png")
tintHelp = transform.smoothscale(tintHelp, (300, 230))

paletteHelp = image.load("ToolHelpPics/paletteHelp.png")
paletteHelp = transform.smoothscale(paletteHelp, (300, 230))

grayPaletteHelp = image.load("ToolHelpPics/grayPaletteHelp.png")
grayPaletteHelp = transform.smoothscale(grayPaletteHelp, (300, 230))

randomColorOptionHelp = image.load("ToolHelpPics/randomColorOptionHelp.png")
randomColorOptionHelp = transform.smoothscale(randomColorOptionHelp, (300, 230))

rainbowColorOptionHelp = image.load("ToolHelpPics/rainbowColorOptionHelp.png")
rainbowColorOptionHelp = transform.smoothscale(rainbowColorOptionHelp, (300, 230))


pizzaHelp = image.load("ToolHelpPics/pizzaHelp.png")
pizzaHelp = transform.smoothscale(pizzaHelp, (300, 230))

realPizzaHelp = image.load("ToolHelpPics/realPizzaHelp.png")
realPizzaHelp = transform.smoothscale(realPizzaHelp, (300, 230))

pepperoniHelp = image.load("ToolHelpPics/pepperoniHelp.png")
pepperoniHelp = transform.smoothscale(pepperoniHelp, (300, 230))

mushroomHelp = image.load("ToolHelpPics/mushroomHelp.png")
mushroomHelp = transform.smoothscale(mushroomHelp, (300, 230))

blackOliveHelp = image.load("ToolHelpPics/blackOliveHelp.png")
blackOliveHelp = transform.smoothscale(blackOliveHelp, (300, 230))

greenPepperHelp = image.load("ToolHelpPics/greenPepperHelp.png")
greenPepperHelp = transform.smoothscale(greenPepperHelp, (300, 230))


baconHelp = image.load("ToolHelpPics/baconHelp.png")
baconHelp = transform.smoothscale(baconHelp, (300, 230))

fishHelp = image.load("ToolHelpPics/fishHelp.png")
fishHelp = transform.smoothscale(fishHelp, (300, 230))

greenOliveHelp = image.load("ToolHelpPics/greenOliveHelp.png")
greenOliveHelp = transform.smoothscale(greenOliveHelp, (300, 230))

pineappleHelp = image.load("ToolHelpPics/pineappleHelp.png")
pineappleHelp = transform.smoothscale(pineappleHelp, (300, 230))

shrimpHelp = image.load("ToolHelpPics/shrimpHelp.png")
shrimpHelp = transform.smoothscale(shrimpHelp, (300, 230))

tomatoHelp = image.load("ToolHelpPics/tomatoHelp.png")
tomatoHelp = transform.smoothscale(tomatoHelp, (300, 230))


cheeseHelp = image.load("ToolHelpPics/cheeseHelp.png")
cheeseHelp = transform.smoothscale(cheeseHelp, (300, 230))

cucumberHelp = image.load("ToolHelpPics/cucumberHelp.png")
cucumberHelp = transform.smoothscale(cucumberHelp, (300, 230))

egg1Help = image.load("ToolHelpPics/egg1Help.png")
egg1Help = transform.smoothscale(egg1Help, (300, 230))

egg2Help = image.load("ToolHelpPics/egg2Help.png")
egg2Help = transform.smoothscale(egg2Help, (300, 230))

flatHelp = image.load("ToolHelpPics/flatHelp.png")
flatHelp = transform.smoothscale(flatHelp, (300, 230))

greenChilliHelp = image.load("ToolHelpPics/greenChilliHelp.png")
greenChilliHelp = transform.smoothscale(greenChilliHelp, (300, 230))


meat1Help = image.load("ToolHelpPics/meat1Help.png")
meat1Help = transform.smoothscale(meat1Help, (300, 230))

meat2Help = image.load("ToolHelpPics/meat2Help.png")
meat2Help = transform.smoothscale(meat2Help, (300, 230))

redChilliHelp = image.load("ToolHelpPics/redChilliHelp.png")
redChilliHelp = transform.smoothscale(redChilliHelp, (300, 230))

sausageHelp = image.load("ToolHelpPics/sausageHelp.png")
sausageHelp = transform.smoothscale(sausageHelp, (300, 230))

lineHelp = image.load("ToolHelpPics/lineHelp.png")
lineHelp = transform.smoothscale(lineHelp, (300, 230))

currentColorHelp = image.load("ToolHelpPics/currentColorHelp.png")
currentColorHelp = transform.smoothscale(currentColorHelp, (300, 230))


blankHelp = image.load("ToolHelpPics/blankHelp.png")#This is the blank help, So if u arent hovering over anything it shows this.
blankHelp = transform.smoothscale(blankHelp, (300, 230))

#-------------------------------- Rects ----------------------------------------
#This sections draws out all the rects first before it gets to the while running loop.
#Tool Rects
draw.rect(screen, green, pencilRect, 2)
draw.rect(screen, green, eraserRect, 2)
draw.rect(screen, green, brushRect, 2)

draw.rect(screen, green, bucketRect, 2)
draw.rect(screen, green, dropRect, 2)
draw.rect(screen, green, sprayRect, 2)

draw.rect(screen, green, rectRect, 2)
draw.rect(screen, green, filledRectRect, 2)
draw.rect(screen, green, ellipseRect, 2)
draw.rect(screen, green, filledEllipseRect, 2)
draw.rect(screen, green, lineRect, 2)

draw.rect(screen, green, rhombusRect, 2)
draw.rect(screen, green, pentagonRect, 2)
draw.rect(screen, green, hexagonRect, 2)

draw.rect(screen, green, horizontalArrowRect, 2)
draw.rect(screen, green, verticalArrowRect, 2)

draw.rect(screen, green, fourStarRect, 2)
draw.rect(screen, green, fiveStarRect, 2)
draw.rect(screen, green, sixStarRect, 2)

draw.rect(screen, green, boltRect, 2)

draw.rect(screen, green, clearRect, 2)
draw.rect(screen, green, floodfillRect, 2)
draw.rect(screen, green, blurRect, 2)
draw.rect(screen, green, markerRect, 2)

draw.rect(screen, green, saveRect, 2)
draw.rect(screen, green, loadRect, 2)

draw.rect(screen, green, undoRect, 2)
draw.rect(screen, green, redoRect, 2)

#Bitmap Rects
draw.rect(screen, green, blankPizzaRect, 2)
draw.rect(screen, green, realPizzaRect, 2)

draw.rect(screen, green, pepperoniRect, 2)
draw.rect(screen, green, mushroomRect, 2)

draw.rect(screen, green, blackOliveRect, 2)
draw.rect(screen, green, greenPepperRect, 2)

draw.rect(screen, green, baconRect, 2)
draw.rect(screen, green, fishRect, 2)

draw.rect(screen, green, greenOliveRect, 2)
draw.rect(screen, green, pineappleRect, 2)

draw.rect(screen, green, shrimpRect, 2)
draw.rect(screen, green, tomatoRect, 2)


draw.rect(screen, green, cheeseRect, 2)
draw.rect(screen, green, cucumberRect, 2)

draw.rect(screen, green, egg1Rect, 2)
draw.rect(screen, green, egg2Rect, 2)

draw.rect(screen, green, flatThingRect, 2)
draw.rect(screen, green, greenChilliRect, 2)

draw.rect(screen, green, meat1Rect, 2)
draw.rect(screen, green, meat2Rect, 2)

draw.rect(screen, green, redChilliRect, 2)
draw.rect(screen, green, sausageRect, 2)


#Color Rects    
draw.rect(screen, black, paletteRect, 3)
draw.rect(screen, black, grayscaleRect, 3)
draw.rect(screen, green, randomColorRect, 2)
draw.rect(screen, green, rainbowRect, 2)

#Filter Rects
draw.rect(screen, green, sepiaRect, 2)
draw.rect(screen, green, xrayRect, 2)
draw.rect(screen, green, invertRect, 2)
draw.rect(screen, green, grayRect, 2)
draw.rect(screen, green, tintRect, 2)

size=1      #Variable for size for drawing tools
ox=oy=300   #Offset variables for pencil tool

undolist=[screen.subsurface(canvasRect).copy()] #Starts the undolist
undopos = 0                                     #First undo position

mx, my=mouse.get_pos()

toolboxPIC = screen.subsurface(toolboxRect).copy()#Takes a picture of this before you start chaning things, called toolbox for all the tools

blitboxPIC = screen.subsurface(blitboxRect).copy()#Blit box is called this because this is where all the stamps are

colorboxPIC = screen.subsurface(colorboxRect).copy()#This thing is just the picture of everything else

toolcheck=""#Toolchecks for things that are different so that size can get reset when you change tools
tooltype="" #Different tooltypes such as drawing and filters and stamps

rainbow=131 #Starts the rainbow variable for rainbow color option

colorOption=""#Can use different color options
meep=1
sizePizza=260 #First pizza size so that you can change it later
shiftType=""  #Even though its called shifttype, its not for the shift. I made this for something else, but It didnt work so I did it this way instead.
              #THis is to draw unfilled with the left mouse button and to draw filled with right mousebutton.
while running:
    click = False
    drawn=False
    shift=False
    for e in event.get():
        if e.type==QUIT:
            running=False
        keys=key.get_pressed()

        if e.type == MOUSEBUTTONDOWN:
            
            if undoRect.collidepoint(mx, my) and len(undolist) - 1 > 0 and undopos>=0:
                undopos -= 1#Undopos goes down, screen.blit last thing into the screen.
                screen.blit(undolist[undopos], canvasRect)
                
            if redoRect.collidepoint(mx, my) and undopos + 1 < len(undolist) and undopos>=0:
                undopos += 1#Undopos goes up, and blits the frame before the frame that you just put in.
                screen.blit(undolist[undopos], canvasRect)
                
           #Gets position of the mouse when you first click
            if e.button == 1 or (e.button == 3 and shiftType == "Polygon"):#This part takes a picture of the screen and gets start coordinates for shapes and the like.
                                                                           #the shifttype=polygon is for drawing filled with the right mouse button. I couldnt change al of them after.
                canvasSurf=screen.subsurface(canvasRect)
                canvasPIC=canvasSurf.copy()
                x, y=mouse.get_pos()#Gets start coords for shapes.
               
            if e.button == 4:#When mousebutton scroll up, size can change
                if tool!="no tool" and tool!="blankPizza" and tool!="realPizza":
                    size += 1
                   
            if e.button == 4 and (tool=="blankPizza" or tool=="realPizza"):#Its the same thing, but this is only for the pizzas. You can do the same thing to go down two lines down
                sizePizza+=5#FOr pizza tool, it should increase faster so done like this.
               
            if e.button == 5 and size>0 and tool!="blankPizza" and tool!="realPizza":
                if tool!="no tool" and tool!="blankPizza" and tool!="realPizza":
                    size -= 1
            if e.button==5 and sizePizza>0 and (tool=="blankPizza" or tool=="realPizza"):
                sizePizza-=5

            size=max(1, size)#Just so size wont go under 0
            
            
        elif e.type == MOUSEBUTTONUP and canvasRect.collidepoint(mx, my) and undopos>=0 and e.button !=5 and e.button !=4:#It should not consider the scroll wheel when adding to list.
            #This is the undo tool. It undos what you previously have done.
            #Theres an undo list and a redo list, and what this does is that after you press and lift the mousebutton, it takes a picture
            #of the screen and adds it to a list. And then it adds 1 to the undolist position.
            #When undo is clicked, undopos decreases one and the last frame is put into the canvas
            #When redo is clicked, undopos increases one and the frame that someone last put is put into the screenn
            undolist += [screen.subsurface(canvasRect).copy()]
            undopos += 1        
    
    mx, my=mouse.get_pos()
    mb=mouse.get_pressed()

    draw.rect(screen, color, currentColorRect)
    draw.rect(screen, black, currentColorRect, 2)
    

    if toolcheck != tool:#If the tool is different from the toolcheck, then size will get reset to what it was before
        size=1
        
    toolcheck=tool
    
    brushHead = Surface((max(10, size)*2, max(10, size)*2), SRCALPHA)#This the surface is for the marker tool, the max is so that the size wont go under 10.
    blurHead = Surface((30, 30), SRCALPHA)                         #This is the surface for blur tool.
    
    blurColor=screen.get_at((mx,my))#blur tool takes the color of the mouse is at, and then draws the color. It creates a blur effect when used at low transparent. 
    blurr, blurg, blurb, al=blurColor#jus blur red blur green etc.
    
    draw.circle(blurHead, (blurr, blurg, blurb, 4), (15, 15), 15)
    
    draw.rect(screen, green, clearRect, 2)#These tools are tools that are like buttons, so you don't need to blit the toolboxes or blitbox on it
    draw.rect(screen, green, undoRect, 2)
    draw.rect(screen, green, redoRect, 2)
    draw.rect(screen, green, saveRect, 2)
    draw.rect(screen, green, loadRect, 2)
#----------------------------   Tool Help   -------------------------------------
#Whenever u hover over a button it shows description of what it is.
    if pencilRect.collidepoint(mx, my):
        screen.blit(pencilHelp, (790, 255))
        
    elif eraserRect.collidepoint(mx, my):
        screen.blit(eraserHelp, (790, 255))
        
    elif brushRect.collidepoint(mx, my):
        screen.blit(brushHelp, (790, 255))
        
    elif markerRect.collidepoint(mx, my):
        screen.blit(markerHelp, (790, 255))
        
    elif rectRect.collidepoint(mx, my):
        screen.blit(rectangleHelp, (790, 255))
        
    elif filledRectRect.collidepoint(mx, my):
        screen.blit(filledRectangleHelp, (790, 255))
        
        
    elif sprayRect.collidepoint(mx, my):
        screen.blit(sprayHelp, (790, 255))
        
    elif dropRect.collidepoint(mx, my):
        screen.blit(dropHelp, (790, 255))
        
    elif rhombusRect.collidepoint(mx, my):
        screen.blit(rhombusHelp, (790, 255))
        
    elif pentagonRect.collidepoint(mx, my):
        screen.blit(pentagonHelp, (790, 255))
        
    elif ellipseRect.collidepoint(mx, my):
        screen.blit(ellipseHelp, (790, 255))
        
    elif filledEllipseRect.collidepoint(mx, my):
        screen.blit(ellipseFillHelp, (790, 255))
        

    elif hexagonRect.collidepoint(mx, my):
        screen.blit(hexagonHelp, (790, 255))
        
    elif fourStarRect.collidepoint(mx, my):
        screen.blit(fourStarHelp, (790, 255))
        
    elif fiveStarRect.collidepoint(mx, my):
        screen.blit(fiveStarHelp, (790, 255))
        
    elif sixStarRect.collidepoint(mx, my):
        screen.blit(sixStarHelp, (790, 255))
        
    elif horizontalArrowRect.collidepoint(mx, my):
        screen.blit(horizontalArrowHelp, (790, 255))
        
    elif verticalArrowRect.collidepoint(mx, my):
        screen.blit(verticalArrowHelp, (790, 255))
        

    elif boltRect.collidepoint(mx, my):
        screen.blit(boltHelp, (790, 255))
        
    elif floodfillRect.collidepoint(mx, my):
        screen.blit(floodfillHelp, (790, 255))
        
    elif blurRect.collidepoint(mx, my):
        screen.blit(blurHelp, (790, 255))
        
    elif clearRect.collidepoint(mx, my):
        screen.blit(clearHelp, (790, 255))
        
    elif bucketRect.collidepoint(mx, my):
        screen.blit(fillcanvasHelp, (790, 255))
        
    elif undoRect.collidepoint(mx, my):
        screen.blit(undoHelp, (790, 255))
        

    elif redoRect.collidepoint(mx, my):
        screen.blit(redoHelp, (790, 255))
        
    elif saveRect.collidepoint(mx, my):
        screen.blit(saveHelp, (790, 255))
        
    elif loadRect.collidepoint(mx, my):
        screen.blit(loadHelp, (790, 255))
        
    elif sepiaRect.collidepoint(mx, my):
        screen.blit(sepiaFilterHelp, (790, 255))
        
    elif xrayRect.collidepoint(mx, my):
        screen.blit(xrayFilterHelp, (790, 255))
        
    elif grayRect.collidepoint(mx, my):
        screen.blit(grayscaleFilterHelp, (790, 255))


    elif invertRect.collidepoint(mx, my):
        screen.blit(invertFilterHelp, (790, 255))
        
    elif tintRect.collidepoint(mx, my):
        screen.blit(tintHelp, (790, 255))
        
    elif paletteRect.collidepoint(mx, my):
        screen.blit(paletteHelp, (790, 255))
        
    elif grayscaleRect.collidepoint(mx, my):
        screen.blit(grayPaletteHelp, (790, 255))
        
    elif randomColorRect.collidepoint(mx, my):
        screen.blit(randomColorOptionHelp, (790, 255))
        
    elif rainbowRect.collidepoint(mx, my):
        screen.blit(rainbowColorOptionHelp, (790, 255))


    elif blankPizzaRect.collidepoint(mx, my):
        screen.blit(pizzaHelp, (790, 255))
        
    elif realPizzaRect.collidepoint(mx, my):
        screen.blit(realPizzaHelp, (790, 255))
        
    elif pepperoniRect.collidepoint(mx, my):
        screen.blit(pepperoniHelp, (790, 255))
        
    elif mushroomRect.collidepoint(mx, my):
        screen.blit(mushroomHelp, (790, 255))
        
    elif blackOliveRect.collidepoint(mx, my):
        screen.blit(blackOliveHelp, (790, 255))
        
    elif greenPepperRect.collidepoint(mx, my):
        screen.blit(greenPepperHelp, (790, 255))


    elif baconRect.collidepoint(mx, my):
        screen.blit(baconHelp, (790, 255))
        
    elif fishRect.collidepoint(mx, my):
        screen.blit(fishHelp, (790, 255))
        
    elif greenOliveRect.collidepoint(mx, my):
        screen.blit(greenOliveHelp, (790, 255))
        
    elif pineappleRect.collidepoint(mx, my):
        screen.blit(pineappleHelp, (790, 255))
        
    elif shrimpRect.collidepoint(mx, my):
        screen.blit(shrimpHelp, (790, 255))
        
    elif tomatoRect.collidepoint(mx, my):
        screen.blit(tomatoHelp, (790, 255))
        
        
    elif cheeseRect.collidepoint(mx, my):
        screen.blit(cheeseHelp, (790, 255))
        
    elif cucumberRect.collidepoint(mx, my):
        screen.blit(cucumberHelp, (790, 255))
        
    elif egg1Rect.collidepoint(mx, my):
        screen.blit(egg1Help, (790, 255))
        
    elif egg2Rect.collidepoint(mx, my):
        screen.blit(egg2Help, (790, 255))
        
    elif flatThingRect.collidepoint(mx, my):
        screen.blit(flatHelp, (790, 255))
        
    elif greenChilliRect.collidepoint(mx, my):
        screen.blit(greenChilliHelp, (790, 255))


    elif meat1Rect.collidepoint(mx, my):
        screen.blit(meat1Help, (790, 255))
        
    elif meat2Rect.collidepoint(mx, my):
        screen.blit(meat2Help, (790, 255))
        
    elif redChilliRect.collidepoint(mx, my):
        screen.blit(redChilliHelp, (790, 255))
        
    elif sausageRect.collidepoint(mx, my):
        screen.blit(sausageHelp, (790, 255))
        
    elif lineRect.collidepoint(mx, my):
        screen.blit(lineHelp, (790, 255))
        
    elif currentColorRect.collidepoint(mx, my):
        screen.blit(currentColorHelp, (790, 255))

    else:
        screen.blit(blankHelp, (790, 255))
#---------------------------- Tool Selection-------------------------------------
#Every if statement checks if the mouse clicks on this rect.
#This will change the tools
#Everytime you change tools, it blits the toolbox and it blits other boxes so that it can show which tool is being selected.

    
        
    if pencilRect.collidepoint(mx, my) and mb[0]==1:
        tool="pencil"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, pencilRect, 2)
        tooltext="This is a pencil. You can draw things with a pencil."
        size=1

        screen.blit(pencilHelp, (790, 255))

        tooltype="Tool"
        
    elif eraserRect.collidepoint(mx, my) and mb[0]==1:
        tool="eraser"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, eraserRect, 2)
        tooltext="This is an eraser. You can erase the mistakes you have made, which is cool."
        size=10

        screen.blit(eraserHelp, (790, 255))

        tooltype="Tool"

    elif brushRect.collidepoint(mx, my) and mb[0]==1:
        tool="brush"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, brushRect, 2)
        tooltext="This is a paintbrush. This is kinda like a pencil but its kinda not. Its kinda like a paintbrush."
        size=10

        screen.blit(brushHelp, (790, 255))

        tooltype="Tool"
        
    elif bucketRect.collidepoint(mx, my) and mb[0]==1:
        tool="bucket"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, bucketRect, 2)
        tooltext="This is a paint bucket. With this thing you can fill the canvas with whatever selected color you want."

        tooltype="Tool"

    elif dropRect.collidepoint(mx, my) and mb[0]==1:
        tool="dropper"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, dropRect, 2)
        tooltext="This is an eye dropper. Most people use them to put liquids in their eyes, but in this program you can use this to sample any color on the screen and use it for the appropriate tools."

        tooltype="Tool"
        
    elif sprayRect.collidepoint(mx, my) and mb[0]==1:
        tool="spraycan"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, sprayRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=20

        tooltype="Tool"

    elif rectRect.collidepoint(mx, my) and mb[0]==1:
        tool="rectangle"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, rectRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=1

        screen.blit(rectangleHelp, (790, 255))

        tooltype="Tool"
        shiftType = "Polygon"

    elif filledRectRect.collidepoint(mx, my) and mb[0]==1:
        tool="rectangleFILL"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, filledRectRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"

        screen.blit(filledRectangleHelp, (790, 255))

        tooltype="Tool"

    elif ellipseRect.collidepoint(mx, my) and mb[0]==1:
        tool="ellipse"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, ellipseRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=2

        tooltype="Tool"
        shiftType = "Polygon"

    elif filledEllipseRect.collidepoint(mx, my) and mb[0]==1:
        tool="ellipseFILL"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, filledEllipseRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"

        tooltype="Tool"

    elif lineRect.collidepoint(mx, my) and mb[0]==1:
        tool="line"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, lineRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=1

        tooltype="Tool"

    elif rhombusRect.collidepoint(mx, my) and mb[0]==1:
        tool="rhombus"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, rhombusRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=1

        tooltype="Tool"
        shiftType="Polygon"

    elif pentagonRect.collidepoint(mx, my) and mb[0]==1:
        tool="pentagon"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, pentagonRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=1

        tooltype="Tool"
        shiftType="Polygon"

    elif hexagonRect.collidepoint(mx, my) and mb[0]==1:
        tool="hexagon"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, hexagonRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=1

        tooltype="Tool"
        shiftType="Polygon"

    elif horizontalArrowRect.collidepoint(mx, my) and mb[0]==1:
        tool="horizontalArrow"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, horizontalArrowRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=1

        tooltype="Tool"
        shiftType="Polygon"

    elif verticalArrowRect.collidepoint(mx, my) and mb[0]==1:
        tool="verticalArrow"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, verticalArrowRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=1

        tooltype="Tool"
        shiftType="Polygon"

    elif fourStarRect.collidepoint(mx, my) and mb[0]==1:
        tool="fourStar"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, fourStarRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=1

        tooltype="Tool"
        shiftType="Polygon"

    elif fiveStarRect.collidepoint(mx, my) and mb[0]==1:
        tool="fiveStar"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, fiveStarRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=1

        tooltype="Tool"
        shiftType="Polygon"

    elif sixStarRect.collidepoint(mx, my) and mb[0]==1:
        tool="sixStar"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, sixStarRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=1

        tooltype="Tool"
        shiftType="Polygon"

    elif boltRect.collidepoint(mx, my) and mb[0]==1:
        tool="bolt"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, boltRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"
        size=1

        tooltype="Tool"
        shiftType="Polygon"

    elif floodfillRect.collidepoint(mx, my) and mb[0]==1:
        tool="floodfill"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, floodfillRect, 2)
        tooltext="This is a spray paint can. It acts as a spray paint can and you can spray paint whatever you want"

        tooltype="Tool"

    elif markerRect.collidepoint(mx, my) and mb[0]==1:
        tool="marker"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, markerRect, 2)
        size=10

        tooltype="Tool"

    elif blurRect.collidepoint(mx, my) and mb[0]==1:
        tool="blur"
        screen.blit(toolboxPIC, (19, 59))
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, blurRect, 2)
        size=10

        tooltype="Tool"
#----------------------------- Bitmap Selection ---------------------------------
    elif blankPizzaRect.collidepoint(mx, my) and mb[0]==1:
        tool="blankPizza"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, blankPizzaRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        sizePizza=260

        tooltype="Bitmap"

    elif realPizzaRect.collidepoint(mx, my) and mb[0]==1:
        tool="realPizza"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, realPizzaRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        sizePizza=260

        tooltype="Bitmap"
        
    elif pepperoniRect.collidepoint(mx, my) and mb[0]==1:
        tool="pepperoni"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, pepperoniRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif mushroomRect.collidepoint(mx, my) and mb[0]==1:
        tool="mushroom"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, mushroomRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif blackOliveRect.collidepoint(mx, my) and mb[0]==1:
        tool="blackOlive"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, blackOliveRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif greenPepperRect.collidepoint(mx, my) and mb[0]==1:
        tool="greenPepper"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, greenPepperRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif baconRect.collidepoint(mx, my) and mb[0]==1:
        tool="bacon"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, baconRect, 2)
        screen.blit(toolboxPIC, (19, 59))
        
        tooltype="Bitmap"

    elif fishRect.collidepoint(mx, my) and mb[0]==1:
        tool="fish"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, fishRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif greenOliveRect.collidepoint(mx, my) and mb[0]==1:
        tool="greenOlive"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, greenOliveRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif pineappleRect.collidepoint(mx, my) and mb[0]==1:
        tool="pineapple"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, pineappleRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif shrimpRect.collidepoint(mx, my) and mb[0]==1:
        tool="shrimp"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, shrimpRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif tomatoRect.collidepoint(mx, my) and mb[0]==1:
        tool="tomato"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, tomatoRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif cheeseRect.collidepoint(mx, my) and mb[0]==1:
        tool="cheese"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, cheeseRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif cucumberRect.collidepoint(mx, my) and mb[0]==1:
        tool="cucumber"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, cucumberRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif egg1Rect.collidepoint(mx, my) and mb[0]==1:
        tool="egg1"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, egg1Rect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif egg2Rect.collidepoint(mx, my) and mb[0]==1:
        tool="egg2"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, egg2Rect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif flatThingRect.collidepoint(mx, my) and mb[0]==1:
        tool="flatThing"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, flatThingRect, 2)
        screen.blit(toolboxPIC, (19, 59))
        
        tooltype="Bitmap"

    elif greenChilliRect.collidepoint(mx, my) and mb[0]==1:
        tool="greenChilli"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, greenChilliRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif meat1Rect.collidepoint(mx, my) and mb[0]==1:
        tool="meat1"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, meat1Rect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif meat2Rect.collidepoint(mx, my) and mb[0]==1:
        tool="meat2"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, meat2Rect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif redChilliRect.collidepoint(mx, my) and mb[0]==1:
        tool="redChilli"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, redChilliRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"

    elif sausageRect.collidepoint(mx, my) and mb[0]==1:
        tool="sausage"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, sausageRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Bitmap"   
#----------------------------- Filter Selection ---------------------------------
    elif sepiaRect.collidepoint(mx, my) and mb[0]==1:
        tool="sepia"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, sepiaRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Filter"

    elif xrayRect.collidepoint(mx, my) and mb[0]==1:
        tool="xray"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, xrayRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Filter"

    elif invertRect.collidepoint(mx, my) and mb[0]==1:
        tool="invert"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, invertRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Filter"

    elif grayRect.collidepoint(mx, my) and mb[0]==1:
        tool="gray"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, grayRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Filter"

    elif tintRect.collidepoint(mx, my) and mb[0]==1:
        tool="tint"
        screen.blit(blitboxPIC, (799, 59))
        screen.blit(colorboxPIC, (0, 615))
        draw.rect(screen, red, tintRect, 2)
        screen.blit(toolboxPIC, (19, 59))

        tooltype="Filter"
        
#----------------------------- Using The Tool -----------------------------------

    if canvasRect.collidepoint(mx, my):
        screen.set_clip(canvasRect)

                
        sx, sy=mx, my
        
        if tool=="pencil" and mb[0]==1:

            draw.line(screen, color, (mx, my), (ox, oy), min(size, 5))
            drawn=True
            
        elif tool=="eraser" and mb[0]==1:
            #Basically, what this does is it draws a circle at every pixels the mouse moves across. It takes two pixels and calculates the distance of them, and
            #then draws circles between the distance.
            #This is the same for the brush tool, blur tool,and marker tool.
            bx=mx-ox
            by=my-oy
            dist=hypot(bx, by)
            dist=max(1, dist)
            sx=bx/dist
            sy=by/dist
    
            for i in range(int(dist)):
                dx=(ox+sx*i)
                dy=(oy+sy*i)
        
                draw.circle(screen, white, (int(dx), int(dy)), min(size, 20))
            drawn=True
            
        elif tool=="brush" and mb[0]==1:
            bx=mx-ox
            by=my-oy
            dist=hypot(bx, by)
            dist=max(1, dist)
            sx=bx/dist
            sy=by/dist
    
            for i in range(int(dist)):
                dx=(ox+sx*i)
                dy=(oy+sy*i)
        
                draw.circle(screen, color, (int(dx), int(dy)), min(size, 25))
            drawn=True
            
        elif tool=="bucket" and mb[0]==1:
            draw.rect(screen, color, canvasRect, 0)
            drawn=True
            
        elif tool=="spraycan" and mb[0]==1:
            
            for i in range(int(size**1.15)):#Increases speed and density. Puts more pixels at a time
                x=(randint(-max(size, 10), max(size, 10)))#Random pixels in a range
                y=(randint(-max(size, 10), max(size, 10)))
                
                if hypot(x, y)<max(size, 10):#Calculates the distance between the mouse and the random coordinates and checks if its inside the circle or not.
                    screen.set_at((mx+x, my+y), color)
                    
            drawn=True

        elif (tool=="rectangleFILL" and mb[0]==1) or (tool=="rectangle" and mb[2]==1):
            screen.blit(canvasPIC, (130, 60))#The blit thing is so that while you draw, it doesn't show the other times you draw. It basically lets you drag while drawing.
                                           #This the same for all the shape tools and line tool.
            
            difx, dify=mx-x, my-y#Basically, the difx and dify is the difference between mouse position and the position of where first pressed the mouse.
                                 #These two differences are the width and the height
                                 #This is pretty much the same for the rectangle, ellipse, and filled ellipse.
            draw.rect(screen, color, (x, y, difx, dify), 0)
            drawn=True

        
            
        elif tool=="rectangle" and mb[0]==1:           
            screen.blit(canvasPIC, (130, 60))
##          The unfilled rectangle is a bit more complicated because when you try to change the thickness, it doesn't show the corners.
##          This is because pygame takes coordinates and draws four lines, and it doesn't actually draw a rectangle.
##          For this, you just have to change the starting coordinates, the width, and height according to the size.
##          You just subtract or add the size divided by two to the coordinates, the width, and the height.
            

            extension=size//2#Called Extension because this how much you have to extend the line whilst drawing
            
##            if mx-x>=0:
##          The first if statement in the draw.line is so that when the size is odd, it will add the one.
##          The second is so that if you try to draw backwards, it will work. If that wasnt there it would mess it up.
            
            draw.line(screen, color, (x -extension if size%2!=0 else x-extension+1, y), (mx+extension, y), size) if mx-x>=0 else draw.line(screen, color, (mx -extension if size%2!=0 else mx-extension+1, my), (x+extension, my), size) 
            draw.line(screen, color, (x, y), (x, my), size)
            
            draw.line(screen, color, (x -extension if size%2!=0 else x-extension+1, my), (mx+extension, my), size) if mx-x>=0 else draw.line(screen, color, (mx -extension if size%2!=0 else mx-extension+1, y), (x+extension, y), size)
            draw.line(screen, color, (mx, y), (mx, my), size)

            
            drawn=True
            
        elif (tool=="ellipseFILL" and mb[0]==1) or (tool=="ellipse" and mb[2]==1):              
            screen.blit(canvasPIC, (130, 60))
##          rx means radius x, and ry means radius y. Its basically width and height for the ellipses.
##          The ternary if statement is so that if mouse pos and start pos is the same, the radiuses will be 1 instead of 0 in order to prevent errors
            
            rx, ry=mx-x if mx-x!=0 else 1, my-y if my-y!=0 else 1 
            
            normalizedRect=Rect(x, y, rx, ry)#Makes negative heights positive and automatically corrects the coordinates.
            normalizedRect.normalize()
            
            draw.ellipse(screen, color, normalizedRect)

            drawn=True

        elif tool=="ellipse" and mb[0]==1:
            #For the draw.ellipse in pygame, it draws a pretty crappy ellipse when its unfilled.
            #To prevent this, you draw a filled ellipse, and then a white transparent ellipse on top of it
            #on a SCRALPHA surface
            
            screen.blit(canvasPIC, (130, 60))

            size=max(2, size)             
            
            rx, ry=mx-x if mx-x!=0 else 1, my-y if my-y!=0 else 1                
            
            normalizedRect=Rect(0 if x<mx else (abs(rx) if abs(rx)>0 else 1), 0 if y<my else (abs(ry) if abs(ry)>0 else 1), rx, ry)
##                                 Start point will be 0         #Just so that             Same for the Y
##                                 if you are drawing towards    #it won't be 0
##                                 the bottom left corner
##                                 otherwise it would be rx                                 
            normalizedRect2=Rect(size if x<mx else (abs(rx) if abs(rx)>0 else 1)-size, 0+size if y<my else (abs(ry) if abs(ry)>0 else 1)-size, rx-size*2 if x<mx else rx+size*2, ry-size*2 if y<my else ry+size*2)
            normalizedRect.normalize()
            normalizedRect2.normalize()

            ellipseSurface=Surface((abs(rx) if abs(rx)>0 else 1, abs(ry) if abs(ry)>0 else 1), SRCALPHA)
            
            if min(abs(rx), abs(ry))>(size*2):#The empty ellipse has a thing where that if the radius is smaller than the thickness of the size, it will cause an error.
                                             #Because of that, you make an if statement that makes it so that it only draws if the ellipse size is half of the smallest radius.
                                             #The absolute value thing is so that it doesn't accidently take -300 instead of 3, even though the three would be smaller.

                draw.ellipse(ellipseSurface, color, normalizedRect)
                draw.ellipse(ellipseSurface, (255, 255, 255, 0), normalizedRect2)

                screen.blit(ellipseSurface, (x if x<mx else mx, y if y<my else my))
            else:
                draw.ellipse(ellipseSurface, color, normalizedRect)
                screen.blit(ellipseSurface, (x if x<mx else mx, y if y<my else my))
                
            drawn=True


            
        elif tool=="line" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            draw.line(screen, color, (x, y), (mx, my), min(size, 50))            

            drawn=True

        elif tool=="rhombus" and (mb[0]==1 or mb[2]==1):
            if mb[2]==1:
                size=0
            
            screen.blit(canvasPIC, (130, 60))
            
            pointList=[(x+(mx-x)//2, y),      #Divide the distance from x to mx by half, and then divide the height from y to my by half to get the 4 corners of a rhombus.
                       (x, y+(my-y)//2),      #The points for this shape and all the other ones were figured out by a lot of trial and error, but they ended up working
                       (x+(mx-x)//2, my), 
                       (mx, y+(my-y)//2)]
            
            draw.polygon(screen, color, pointList, size)

        elif tool=="pentagon" and (mb[0]==1 or mb[2]==1):
            if mb[2]==1:
                size=0
            screen.blit(canvasPIC, (130, 60))
            
            pointList=[(x+(mx-x)//2, y),     #All tools have their own set ratios.
                       (mx, y+int(2/5*(my - y))), 
                       (x+int(4/5*(mx - x)), my), 
                       (x+int(1/5*(mx - x)), my), 
                       (x, y+int(2/5*(my - y)))]
            
            draw.polygon(screen, color, pointList, size)

        elif tool=="hexagon" and (mb[0]==1 or mb[2]==1):
            if mb[2]==1:
                size=0
            screen.blit(canvasPIC, (130, 60))
            
            pointList=[(x+(mx-x)//2, y), 
                       (mx, y+int(1/4*(my - y))), 
                       (mx, y+int(3/4*(my - y))), 
                       (x+(mx-x)//2, my), 
                       (x, y+int(3/4*(my - y))), 
                       (x, y+int(1/4*(my - y)))]
            
            draw.polygon(screen, color, pointList, size)

        elif tool=="horizontalArrow" and (mb[0]==1 or mb[2]==1):
            if mb[2]==1:
                size=0
            screen.blit(canvasPIC, (130, 60))
            
            pointList=[(x+(mx-x)//2, y), (mx, y+(my - y)//2), (x+(mx-x)//2, my), 
                       (x+(mx-x)//2, y+int(3/4*(my - y))), (x, y+int(3/4*(my - y))), 
                       (x, y+int(1/4*(my - y))), (x+(mx-x)//2, y+int(1/4*(my - y)))]
            
            draw.polygon(screen, color, pointList, size)

        elif tool=="verticalArrow" and (mb[0]==1 or mb[2]==1):
            if mb[2]==1:
                size=0
            screen.blit(canvasPIC, (130, 60))
            
            pointList=[(x+(mx-x)//2, y), (mx, y+(my-y)//2), 
                       (x+int(3/4*(mx - x)), y+(my-y)//2), 
                       (x+int(3/4*(mx - x)), my), (x+int(1/4*(mx - x)), my), 
                       (x+int(1/4*(mx - x)), y+(my-y)//2), (x, y+(my-y)//2)]
            
            draw.polygon(screen, color, pointList, size)

        elif tool=="fourStar" and (mb[0]==1 or mb[2]==1):
            if mb[2]==1:
                size=0
            screen.blit(canvasPIC, (130, 60))
            
            pointList=[(x+(mx-x)//2, y), (x+int(2/5*(mx - x)), y+int(2/5*(my - y))), 
                       (x, y+(my-y)//2), (x+int(2/5*(mx - x)), y+int(3/5*(my - y))), 
                       (x+(mx-x)//2, my), (x+int(3/5*(mx - x)), y+int(3/5*(my - y))), 
                       (mx, y+(my-y)//2), (x+int(3/5*(mx - x)), y+int(2/5*(my - y))), ]
            
            draw.polygon(screen, color, pointList, size)

        elif tool=="fiveStar" and (mb[0]==1 or mb[2]==1):
            if mb[2]==1:
                size=0
            screen.blit(canvasPIC, (130, 60))
            
            pointList=[(x+(mx-x)//2, y), (x+int(3/5*(mx-x)), y+int(2/5*(my-y))), 
                       (mx, y+int(2/5*(my - y))), (x+int(7/10*(mx-x)), y+int(3/5*(my-y))), 
                       (x+int(4/5*(mx - x)), my), (x+(mx-x)//2, y+int(3/4*(my-y))), 
                       (x+int(1/5*(mx - x)), my), (x+int(3/10*(mx-x)), y+int(3/5*(my-y))), 
                       (x, y+int(2/5*(my - y))), (x+int(2/5*(mx-x)), y+int(2/5*(my-y)))]
            
            draw.polygon(screen, color, pointList, size)

        elif tool=="sixStar" and (mb[0]==1 or mb[2]==1):
            if mb[2]==1:
                size=0
            screen.blit(canvasPIC, (130, 60))
            
            pointList=[(x+(mx-x)//2, y), (x+int(2/3*(mx-x)), y+int(1/4*(my-y))), 
                       (mx, y+int(1/4*(my - y))), (x+int(5/6*(mx-x)), y+(my-y)//2), 
                       (mx, y+int(3/4*(my - y))), (x+int(2/3*(mx-x)), y+int(3/4*(my-y))), 
                       (x+(mx-x)//2, my), (x+int(1/3*(mx-x)), y+int(3/4*(my-y))), 
                       (x, y+int(3/4*(my - y))), (x+int(1/6*(mx-x)), y+(my-y)//2), 
                       (x, y+int(1/4*(my - y))), (x+int(1/3*(mx-x)), y+int(1/4*(my-y)))]
            
            draw.polygon(screen, color, pointList, size)

        elif tool=="bolt" and (mb[0]==1 or mb[2]==1):
            if mb[2]==1:
                size=0
            screen.blit(canvasPIC, (130, 60))

            a=(my-y)//5#These dont mean much, they were convenient to put it here so I did. Since the bolts points were rather irregular, it was easier to have set values here.
            a2=(mx-x)//5
            a3=(mx-x)//8
            a4=(my-y)//4
            a5=(my-y)//10
            a6=(mx-x)//10
            a7=(my-y)//14
            a8=(my-y)//20
            a9=(mx-x)//20

            a1x=x
            a1y=y+a#These are just the points and dont mean anything.
            a2x=x+a2*2
            a2y=y
            a3x=x+a6*6
            a3y=y+a4
            a4x=x+a3*4
            a4y=y+a5*3
            a5x=x+a6*8
            a5y=y+a5*6
            a6x=x+a6*7
            a6y=y+a8*13
            a7x=mx
            a7y=my
            a8x=x+a6*4
            a8y=y+a8*15
            a9x=x+a6*5
            a9y=y+a5*7
            a10x=x+a9*3
            a10y=y+a5*4
            a11x=x+a6*3
            a11y=y+a7*5

            pointList=[(a1x, a1y), (a2x, a2y), (a3x, a3y), (a4x, a4y), (a5x, a5y), (a6x, a6y), (a7x, a7y), (a8x, a8y), (a9x, a9y), (a10x, a10y), (a11x, a11y)]
            draw.polygon(screen, color, pointList, size)
            
        elif tool=="floodfill" and mb[0]==1:
            floodfill()
            drawn=True

        elif tool=="marker" and mb[0]==1:
            bx=mx-ox
            by=my-oy
            dist=hypot(bx, by)
            dist=max(1, dist)
            sx=bx/dist
            sy=by/dist

            alpha=10

            if 20>size:
                alpha=10#It makes it so tbat alpha is proportionate to to size.
            elif 40>size>20:
                alpha=7
            elif 60>size>39:
                alpha=5
            elif size>59:
                alpha=2
            
            lst=list(color)#Mkaes tuple into a ist
            lst[-1]=alpha  #Replaces last item in list
            color=tuple(lst)#Changes it back to tuple

            draw.circle(brushHead, color, (max(10, size), max(10, size)), max(10, size))
            
            for i in range(int(dist)):
                dx=(ox+sx*i)
                dy=(oy+sy*i)
                if dx!=ox or dy!=oy:#So that it doesnt draw when mouse isnt moving
                    screen.blit(brushHead, (dx-(max(10,size)), dy-(max(10,size))))       # this is where it uses the alpha

        elif tool=="blur" and mb[0]==1:
            #What was same for marker is same for this
            bx=mx-ox
            by=my-oy
            dist=hypot(bx, by)
            dist=max(1, dist)
            sx=bx/dist
            sy=by/dist
            
            for i in range(int(dist)):
                dx=(ox+sx*i)
                dy=(oy+sy*i)
                if dx!=ox or dy!=oy:
                    screen.blit(blurHead, (dx-15, dy-15))       # this is where it uses the alpha
                
            drawn=True
#---------------------------------Filters---------------------------------------
        elif tool=="sepia" and mb[0]==1:#These filters get the color value of every pixel on the canvas and then change it by how it is supposed.
            used=set()
            for x in range(130, 780):
                for y in range(60, 610):
                    if (x, y) not in used:
                        used.add((x, y))
                        r, g, b, alpha = screen.get_at((x, y))#Gets all rgba values of pixels
                        
                        r2 = min(255, int(r * .393 + g *.769 + b * .189))#Multiplies them by what its supposed to be
                        g2 = min(255, int(r * .349 + g *.686 + b * .168))
                        b2 = min(255, int(r * .272 + g *.534 + b * .131))
                        
                        screen.set_at((x, y), (r2, g2, b2))#And sets pixel at every spot
                        
        elif tool=="xray" and mb[0]==1:#xray filter gets the average of color in the pixel, and then you invert the average.
                                       #since all the r,g,b values are the same it will show a pixel on the grayscale. 
            used=set()
            for x in range(130, 780):
                for y in range(60, 610):
                    if (x, y) not in used:
                        used.add((x, y))
                        r, g, b, alpha = screen.get_at((x, y))
                        average = (r+g+b)//3#Gets avg of 3
                        
                        col=255-average#Inverts avg

                        screen.set_at((x, y), (col, col, col))#Sets pixel everywhere

        elif tool=="invert" and mb[0]==1:
            for x in range(130, 780):
                for y in range(60, 610):
                    if (x, y) not in used:
                        r, g, b, alpha = screen.get_at((x, y))
                        
                        col=(255-r, 255-g, 255-b)#It basically inverts the r,g and b values. So if original r is 20, then new r is 235.

                        screen.set_at((x, y), col)

        elif tool=="gray" and mb[0]==1:
            used=set()
            for x in range(130, 780):
                for y in range(60, 610):
                    if (x, y) not in used:
                        used.add((x, y))
                        r, g, b, alpha = screen.get_at((x, y))#Same as the xray one but it doesnt invert.
                        average = (r+g+b)//3

                        col=(average, average, average)

                        screen.set_at((x, y), col)

        elif tool=="tint" and mb[0]==1:
            used=set()
            for x in range(130, 780):
                for y in range(60, 610):
                    if (x, y) not in used:
                        used.add((x, y))
                        
                        r, g, b, alpha = screen.get_at((x, y))#Tint gets a color and then tints the image to the color u want.
                        r2, g2, b2, alpha = color
                        
                        r3 = min(255, int(r*r2/175))#U divide color selected by some certainn number (doesnt have to be 255) and then multiply that to each pixel to tint.
                        g3 = min(255, int(g*g2/175))
                        b3 = min(255, int(b*b2/175))

                        col=(r3, g3, b3)

                        screen.set_at((x, y), col)
#--------------------------------Picture Stuff----------------------------------

        elif tool=="blankPizza" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))

            blankPizzaBlit = transform.smoothscale(blankPizza, (max(sizePizza, 1), max(1, sizePizza)))#This is so that you can change sizes by scrolling within the loop
            
            screen.blit(blankPizzaBlit, (mx-(sizePizza//2), my-(sizePizza//2)))

        elif tool=="realPizza" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))

            realPizzaBlit = transform.smoothscale(realPizza, (max(sizePizza, 1), max(1, sizePizza)))
            
            screen.blit(realPizzaBlit, (mx-(sizePizza//2), my-(sizePizza//2)))
            
            
        elif tool=="pepperoni" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))

            pepperoniBlit = transform.smoothscale(pepperoni, (40+max(size, 1), 40+max(1, size)))
            
            screen.blit(pepperoniBlit, (mx-(40+size)//2, my-(40+size)//2))

        elif tool=="mushroom" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            mushroomBlit = transform.smoothscale(mushroom, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(mushroomBlit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="blackOlive" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))

            blackOliveBlit = transform.smoothscale(blackOlive, (20+max(size, 1), 20+max(1, size)))
            
            screen.blit(blackOliveBlit, (mx-(20+size)//2, my-(20+size)//2))

        elif tool=="greenPepper" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            greenPepperBlit = transform.smoothscale(greenPepper, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(greenPepperBlit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="bacon" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            baconBlit = transform.smoothscale(bacon, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(baconBlit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="fish" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            fishBlit = transform.smoothscale(fish, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(fishBlit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="greenOlive" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            greenOliveBlit = transform.smoothscale(greenOlive, (20+max(size, 1), 20+max(1, size)))
            
            screen.blit(greenOliveBlit, (mx-(20+size)//2, my-(20+size)//2))

        elif tool=="pineapple" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            pineappleBlit = transform.smoothscale(pineapple, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(pineappleBlit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="shrimp" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            shrimpBlit = transform.smoothscale(shrimp, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(shrimpBlit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="tomato" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            tomatoBlit = transform.smoothscale(tomato, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(tomatoBlit, (mx-(30+size)//2, my-(30+size)//2))
            
        elif tool=="cheese" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            cheeseBlit = transform.smoothscale(cheese, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(cheeseBlit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="cucumber" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            cucumberBlit = transform.smoothscale(cucumber, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(cucumberBlit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="egg1" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            egg1Blit = transform.smoothscale(egg1, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(egg1Blit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="egg2" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            egg2Blit = transform.smoothscale(egg2, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(egg2Blit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="flatThing" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            flatThingBlit = transform.smoothscale(flatThing, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(flatThingBlit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="greenChilli" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            greenChilliBlit = transform.smoothscale(greenChilli, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(greenChilliBlit, (mx-(30+size)//2, my-(30+size)//2))
            
        elif tool=="meat1" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            meat1Blit = transform.smoothscale(meat1, (20+max(size, 1), 20+max(1, size)))
            
            screen.blit(meat1Blit, (mx-(20+size)//2, my-(20+size)//2))

        elif tool=="meat2" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            meat2Blit = transform.smoothscale(meat2, (20+max(size, 1), 20+max(1, size)))
            
            screen.blit(meat2Blit, (mx-(20+size)//2, my-(20+size)//2))

        elif tool=="redChilli" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            redChilliBlit = transform.smoothscale(redChilli, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(redChilliBlit, (mx-(30+size)//2, my-(30+size)//2))

        elif tool=="sausage" and mb[0]==1:
            screen.blit(canvasPIC, (130, 60))
            
            sausageBlit = transform.smoothscale(sausage, (30+max(size, 1), 30+max(1, size)))
            
            screen.blit(sausageBlit, (mx-(30+size)//2, my-(30+size)//2))


     
        screen.set_clip(None)
#--------------------------------Other Stuff------------------------------------
#These other things are tools that cant work inside the collidecanvas because they dont work inside the canvas.
        
    if tool=="dropper" and mb[0]==1:
            color=screen.get_at((mx, my))#Gets color at mouse pos and uses as color
            color.normalize()
            colorOption=""
            
    elif clearRect.collidepoint(mx, my) and mb[0]==1:
        draw.rect(screen, red, clearRect, 2)
        draw.rect(screen, white, canvasRect, 0)
        undolist += [screen.subsurface(canvasRect).copy()]
        undopos+=1#Adds to undolist because u dont click on canvas when using clear.
        colorOption=""

    elif saveRect.collidepoint(mx, my) and mb[0]==1:
        draw.rect(screen, red, saveRect, 2)
        
        filename = filedialog.asksaveasfilename(defaultextension=".png")#Use this to save the image.
        if len(filename) > 0:#If file length is 0 then it will crash
            image.save(canvasPIC, filename)

    elif loadRect.collidepoint(mx, my) and mb[0]==1:
        draw.rect(screen, red, loadRect, 2)
        
        imageName = filedialog.askopenfilename()
            
        if len(imageName) > 0:
            imageLoad = image.load(imageName)
            
            imageWidth = imageLoad.get_width()
            imageHeight = imageLoad.get_height()
            
            if imageWidth > 650 or imageHeight > 550:
                imageLoad = transform.smoothscale(imageLoad, (650, 550))

            screen.blit(imageLoad, (130, 60))

            canvasPIC=canvasSurf.copy()
            undolist.append(canvasPIC)
            undopos+=1
        
    elif undoRect.collidepoint(mx, my) and mb[0]==1:
        draw.rect(screen, red, undoRect, 2)
        
    elif redoRect.collidepoint(mx, my) and mb[0]==1:
        draw.rect(screen, red, redoRect, 2)
#---------------------------- Selecting A Color --------------------------------
    
    if paletteRect.collidepoint(mx, my) and mb[0]==1:
        color=screen.get_at((mx, my))
        color.normalize()
        colorOption=""
        
    if grayscaleRect.collidepoint(mx, my) and mb[0]==1:
        color=screen.get_at((mx, my))
        color.normalize()
        colorOption==""
        
    if randomColorRect.collidepoint(mx, my) and mb[0]==1:
        colorOption="random"
        screen.blit(blitboxPIC, (799, 59))
        draw.rect(screen, red, randomColorRect, 2)
        
    if rainbowRect.collidepoint(mx, my) and mb[0]==1:
        colorOption="rainbow"
        screen.blit(blitboxPIC, (799, 59))
        draw.rect(screen, red, rainbowRect, 2)
        
#---------------------------- Special Colors -----------------------------------

    if colorOption=="random" and tooltype=="Tool":
        color=(randint(0, 255), randint(0, 255), randint(0, 255), 255)
        
    if colorOption=="rainbow" and tooltype=="Tool":
        if mb[0]==1:
            if mx!=ox or my!=oy:
                if rainbow>775:
                    rainbow=131
                color=screen.get_at((rainbow, 650))
                rainbow+=3

#-------------------------------------------------------------------------------        
    ox=mx
    oy=my
    
    display.flip()
    
quit()
