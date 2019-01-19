from pygame import *
   
screen = display.set_mode((1200,675))
 
canvasRect = Rect(100,50,900,575)
running =True
screen.fill((255,255,255))
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 3:
                image.save(screen.subsurface(canvasRect),"jan8.png")
   
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
 
    draw.rect(screen,(0,0,0), canvasRect,2)
    if mb[0]==1:
        draw.circle(screen, (0,0,0), (mx,my), 3)
 
    display.flip()
 
quit()
 
 
#open and save
 
from pygame import *
from tkinter import *  
 
root = Tk()
root.withdraw() #hiding the tk window
 
 
 
screen = display.set_mode((800,600))
openRect = Rect(20,80,40,40)
saveRect = Rect(65,80,40,40)
 
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
 
 
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
 
    draw.rect(screen,(0,255,0),openRect,2)
    draw.rect(screen,(0,255,0),saveRect,2)
 
    if mb[0]==1 and openRect.collidepoint(mx,my):
        fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.bmp;*.jpg;*.jpeg")])
        print(fname)
 
    if mb[0]==1 and saveRect.collidepoint(mx,my):
        fname=filedialog.asksaveasfilename(defaultextension=".png")
        print(fname)        
 
   
 
 
    display.flip()
 
 
quit()
 
 
#using the keyboard1
 
from pygame import *
   
screen = display.set_mode((800,600))
 
size = 10
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type==MOUSEBUTTONDOWN:
            mouse.set_visible(False)
        if e.type==MOUSEBUTTONUP:
            mouse.set_visible(True)
           
           
           
        if e.type==KEYDOWN:
            if e.key==K_UP: #up arrow key
                size+=1
            if e.key==K_DOWN:#down arrow key
                size-=1
       
 
           
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
 
    if mb[0]==1:
        draw.circle(screen,(0,255,0),(mx,my),size)
 
 
   
 
    display.flip()
 
quit()
 
#using the scroller
 
from pygame import *
   
screen = display.set_mode((800,600))
 
size = 10
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type==MOUSEBUTTONDOWN:
            #print(e)
            if e.button==4:
                print("scrolling up")
                if size<30: #maximum size 30
                    size+=1
            elif e.button==5:
                print("scrolling down")
                if size>1:  #minimum size 1
                    size-=1
            elif e.button==1:
                print("left click")
                start=e.pos #ordered pair (x,y)
 
           
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
 
 
    if mb[0]==1:
        screen.fill((0,0,0))
        print(size)
        draw.line(screen,(0,255,0),start,(mx,my),size)
   
 
    display.flip()
 
quit()
 
'''
alphaBrush.py
-----------------------
Colour in Python is actually RGBA. The A is the alpha. It controls
how transparent/opaque the colour is (0 = transparent, 255 = opaque.)
These values are only used when you blit a surface onto the screen. So,
if I want to draw a partially transparent circle I draw this circle to
a blank Surface then I blit this Surface to the screen.
'''
 
from pygame import *
 
screen = display.set_mode((800,600)) #creates a surface
 
 
running =True
mx,my = 0,0
 
 
brushHead=Surface((20,20),SRCALPHA) #creates a surface 20x20 pixels
draw.circle(brushHead,(255,0,0,127),(10,10),10)
 
eraserHead=Surface((40,40),SRCALPHA) #creates a surface 40x40 pixels
draw.circle(eraserHead,(255,255,255,127),(20,20),20)
 
 
screen.fill((255,255,255))#white
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
 
    mb = mouse.get_pressed()
    omx,omy = mx,my
    mx,my = mouse.get_pos()
 
    #only draw the circle when we move the mouse
    #while using left click
 
    if mx!=omx or my!=omy: #moving the mouse
        if mb[0]==1:#left click
            screen.blit(brushHead,(mx-10,my-10))
        if mb[2]==1:#right click
            screen.blit(eraserHead,(mx-20,my-20))
 
 
    display.flip()
 
quit()
 
 
#drawingText.py
from pygame import *
from random import *
 
init()
size = width, height = 800, 600
screen = display.set_mode(size)
green = 0, 255, 0  
red = 255, 0, 0
black=0,0,0
 
running = True
 
font.init()
comicFont=font.SysFont("Comic Sans MS",20)
names=['Toronto','Computer Science','Vincent Massey',
       'Paint Project','Windsor','Christmas Break',
       'Happy New Year','Basketball','Weekend']
 
 
while running:
    clicked=False #my own flag variable
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type==MOUSEBUTTONDOWN:
            clicked=True
                   
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
 
    if clicked: # same as if clicked==True
        word=choice(names) #random name from the list
        dWord=comicFont.render(word,True,red)
        screen.blit(dWord,(mx-dWord.get_width()/2,my-dWord.get_height()/2))
 
    display.flip()
    font.quit()
 
quit()
 
 
 
# basicPaint.py
from pygame import *
from random import *
from math import *
 
init()
size = width, height = 800, 600
screen = display.set_mode(size)
green = 0, 255, 0  
red = 255, 0, 0
black=0,0,0
white=255,255,255
col=red
 
tool="no tool"
 
pencilRect=Rect(20,60,40,40)
eraserRect=Rect(70,60,40,40)
canvasRect=Rect(130,60,650,520)#130+650=780  60+520=580
 
draw.rect(screen,white,canvasRect,0)#only once
running = True
 
ox=oy=300
 
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
 
    mx,my=mouse.get_pos()
 
    mb=mouse.get_pressed()
 
    draw.rect(screen,green,pencilRect,2)
    draw.rect(screen,green,eraserRect,2)
   
 
################################################
    #selecting the tool
    if pencilRect.collidepoint(mx,my) and mb[0]==1:
        tool="pencil"
        draw.rect(screen,red,pencilRect,2)
       
    if eraserRect.collidepoint(mx,my) and mb[0]==1:
        tool="eraser"
        draw.rect(screen,red,eraserRect,2)
   #<more if statements for ALL tools>
##################################################
   #use the tool
    if canvasRect.collidepoint(mx,my) and mb[0]==1:
       
        if tool=="pencil":
            draw.line(screen,col,(ox,oy),(mx,my))
        if tool=="eraser":
            draw.circle(screen,white,(mx,my),10)
 
 
 
       
    ox=mx
    oy=my
 
    display.flip()
 
quit()
