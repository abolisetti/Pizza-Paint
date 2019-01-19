# basicPaint.py
from pygame import *
from random import *
from math import *

screen = display.set_mode((1000,800))

running = True

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
color=black

tool="no tool"

#--------------------------------Images------------------------------------------
colors = image.load("Images/colors.png")
colors = transform.smoothscale(colors,(300,175))
screen.blit(colors,(130,600))

pencil = image.load("Images/pencil.png")
pencil = transform.scale(pencil,(40,40))
screen.blit(pencil,(20,60))

eraser = image.load("Images/eraser.png")
eraser = transform.scale(eraser,(40,40))
screen.blit(eraser,(70,60))

brush = image.load("Images/brush.png")
brush = transform.scale(brush,(40,40))
screen.blit(brush,(20,110))

#--------------------------------Tools------------------------------------------- 
pencilRect=Rect(20,60,40,40)

eraserRect=Rect(70,60,40,40)

brushRect=Rect(20,110,40,40)

canvasRect=Rect(130,60,650,520)

paletteRect=Rect(130,600,300,175)

draw.rect(screen,white,canvasRect,0)

running = True

ox=oy=300

while running:
    for e in event.get():
        if e.type==QUIT:
            running=False

    mx,my=mouse.get_pos()

    mb=mouse.get_pressed()

    draw.rect(screen,green,pencilRect,2)
    draw.rect(screen,green,eraserRect,2)
    draw.rect(screen,green,brushRect,2)
    draw.rect(screen,black,paletteRect,1)
    

#---------------------------- Tool Selection-------------------------------------

    if pencilRect.collidepoint(mx,my) and mb[0]==1:
        tool="pencil"
        draw.rect(screen,red,pencilRect,2)
        
    if eraserRect.collidepoint(mx,my) and mb[0]==1:
        tool="eraser"
        draw.rect(screen,red,eraserRect,2)

    if brushRect.collidepoint(mx,my) and mb[0]==1:
        tool="brush"
        draw.rect(screen,red,brushRect,2)
        
   #<more if statements for ALL tools>

        
#----------------------------- Using The Tool -----------------------------------

    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        screen.set_clip(canvasRect)
        
        if tool=="pencil":
            draw.line(screen,color,(ox,oy),(mx,my),1)
        if tool=="eraser":
            draw.circle(screen,white,(mx,my),15)
        if tool=="brush":
            draw.circle(screen,color,(mx,my),15)
            
        screen.set_clip(None)


#---------------------------- Selecting A Color --------------------------------
    if paletteRect.collidepoint(mx,my) and mb[0]==1:
        color=screen.get_at((mx,my))
#--------------------------------------------------------------------------------        

    ox=mx
    oy=my

    display.flip()

quit()
