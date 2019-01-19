from pygame import *
from random import *
from tkinter import *
from math import *

init()
size=width,height=800,850
screen=display.set_mode(size)
wholescreen=Rect(0,0,800,850)
root=Tk()
root.withdraw()
grn=0,255,0
red=255,0,0
blk=0,0,0
wht=255,255,255
screen.fill(blk)
myClock=time.Clock()

tool='pencil'
tool2='eraser'
c=blk
size=10
trans=4

canvasBox=Rect(130,40,650,520)
pencilBox=Rect(20,40,40,40)
eraserBox=Rect(70,40,40,40)
paintBox=Rect(20,190,40,40)
sprayBox=Rect(20,240,40,40)
airbrushBox=Rect(70,240,40,40)
blurBox=Rect(70,190,40,40)
bucketBox=Rect(20,140,40,40)
shapeBox1=Rect(20,90,40,40)
shapeBox2=Rect(20,290,40,40)
stampBox1=Rect(70,140,40,40)

#blit stuff here

openBox=Rect(20,760,80,50)
saveBox=Rect(110,760,80,50)
paletteBox=Rect(485,570,295,250)
colourPalette=image.load("Images/colors.jpg")
screen.blit(colourPalette,(485,570))
draw.rect(screen,wht,canvasBox)

mmode="up"
ox=0
oy=0
r2,g2,b2,a2=0,0,0,trans

running=True

while running:
    
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            nx,ny=mx,my
            canBuff=screen.copy()
            if e.button==4:
                if size<30:
                    size+=1
            elif e.button==5:
                if size>5:
                    size-=1
        if e.type==KEYDOWN:
            if e.key==K_UP:
                if trans<10:
                    trans+=1
            if e.key==K_DOWN:
                if trans>1:
                    trans-=1
            
            
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    brushHead=Surface((size*2,size*2),SRCALPHA)
    r,g,b,a=screen.get_at((mx,my))   
    draw.circle(brushHead,(r,g,b,8),(size,size),size)
    brushHead2=Surface((size*2,size*2),SRCALPHA)
    draw.circle(brushHead2,(r2,g2,b2,trans),(size,size),size)
    dist=int(sqrt((mx-ox)**2+(my-oy)**2))
    
            
    draw.rect(screen,wht,pencilBox,2)
    draw.rect(screen,wht,eraserBox,2)
    draw.rect(screen,wht,paintBox,2)
    draw.rect(screen,wht,shapeBox1,2)
    draw.rect(screen,wht,shapeBox2,2)
    draw.rect(screen,wht,stampBox1,2)
    draw.rect(screen,wht,bucketBox,2)
    draw.rect(screen,wht,blurBox,2)
    draw.rect(screen,wht,sprayBox,2)
    draw.rect(screen,wht,airbrushBox,2)
    draw.rect(screen,wht,openBox,2)
    draw.rect(screen,wht,saveBox,2)


    if pencilBox.collidepoint(mx,my) and mb[0]==1:
        tool='pencil'
        draw.rect(screen,grn,pencilBox,2)
    if eraserBox.collidepoint(mx,my) and mb[0]==1:
        tool='eraser'
        draw.rect(screen,grn,eraserBox,2)
    if paintBox.collidepoint(mx,my) and mb[0]==1:
        tool='paint'
        draw.rect(screen,grn,paintBox,2)
    if bucketBox.collidepoint(mx,my) and mb[0]==1:
        tool='fill'
        draw.rect(screen,grn,bucketBox,2)
    if shapeBox1.collidepoint(mx,my) and mb[0]==1:
        tool='rect'
        draw.rect(screen,grn,shapeBox1,2)
    if shapeBox2.collidepoint(mx,my) and mb[0]==1:
        tool='circle'
        draw.rect(screen,grn,shapeBox2,2)
    if blurBox.collidepoint(mx,my) and mb[0]==1:
        tool='blur'
        draw.rect(screen,grn,blurBox,2)
    if sprayBox.collidepoint(mx,my) and mb[0]==1:
        tool='spray'
        draw.rect(screen,grn,sprayBox,2)
    if airbrushBox.collidepoint(mx,my) and mb[0]==1:
        tool='airbrush'
        draw.rect(screen,grn,airbrushBox,2)
    if openBox.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,grn,openBox,2)
        fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.bmp;*.jpg;*.jpeg")])
        #print(fname)
    if saveBox.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,grn,saveBox,2)
        fname=filedialog.asksaveasfilename(defaultextension=".png")
        #print(fname)
    if stampBox1.collidepoint(mx,my) and mb[0]==1:
        tool='placeholder'

                        
    if paletteBox.collidepoint(mx,my) and mb[0]==1:
        c=screen.get_at((mx,my))
        r2,g2,b2,a2=screen.get_at((mx,my))

                           
    if canvasBox.collidepoint(mx,my):
        screen.set_clip(canvasBox)
        if tool=='pencil' and mb[0]==1:
            draw.line(screen,c,(ox,oy),(mx,my),2)
        if tool=='eraser' and mb[0]==1:
            ax=mx-ox
            ay=my-oy
            dist=sqrt(ax**2+ay**2)
            dist=max(1,dist)
            dotX=ax/dist
            dotY=ay/dist
            for i in range(int(dist)):
                dx=(ox+dotX*i)
                dy=(oy+dotY*i)
                draw.circle(screen,wht,(int(dx),int(dy)),size+int(size/5))
        if tool2=='eraser' and mb[2]==1:
            ax=mx-ox
            ay=my-oy
            dist=sqrt(ax**2+ay**2)
            dist=max(1,dist)
            dotX=ax/dist
            dotY=ay/dist
            for i in range(int(dist)):
                dx=(ox+dotX*i)
                dy=(oy+dotY*i)
                draw.circle(screen,wht,(int(dx),int(dy)),size+int(size/5))
        if tool=='paint' and mb[0]==1:
            ax=mx-ox
            ay=my-oy
            dist=sqrt(ax**2+ay**2)
            dist=max(1,dist)
            dotX=ax/dist
            dotY=ay/dist
            for i in range(int(dist)):
                dx=(ox+dotX*i)
                dy=(oy+dotY*i)
                draw.circle(screen,c,(int(dx),int(dy)),size)
        if tool=='spray' and mb[0]==1:
            for i in range(size*3):
                sx=mx-randint(-size,size)
                sy=my-randint(-size,size)
                dist=int(sqrt((mx-sx)**2+(my-sy)**2))  
                if dist<size:
                    draw.line(screen,c,(sx,sy),(sx,sy),1)
        if tool=='fill' and mb[0]==1:
            rc=screen.get_at((mx,my))
            spots=[(mx,my)]
            while len(spots)>0:
                newSpots=[]
                for fx,fy in spots:
                    if 0<fx<width and 0<fy<height and screen.get_at((fx,fy))==rc:
                        screen.set_at((fx,fy),c)
                        newSpots+=[(fx+1,fy),(fx-1,fy),(fx,fy-1),(fx,fy+1)]
                spots=newSpots
        if tool=='airbrush' and mb[0]==1:
            ax=mx-ox
            ay=my-oy
            dist=sqrt(ax**2+ay**2)
            dist=max(1,dist)
            dotX=ax/dist
            dotY=ay/dist
            if mx!=ox or my!=oy:
                for i in range(int(dist)):
                    dx=(ox+dotX*i)
                    dy=(oy+dotY*i)
                    screen.blit(brushHead2,(int(dx)-size,int(dy)-size))
        if tool=='blur' and mb[0]==1:
            ax=mx-ox
            ay=my-oy
            dist=sqrt(ax**2+ay**2)
            dist=max(1,dist)
            dotX=ax/dist
            dotY=ay/dist
            for i in range(int(dist)):
                dx=(ox+dotX*i)
                dy=(oy+dotY*i)
                screen.blit(brushHead,(int(dx)-size,int(dy)-size))
        if tool=='rect' and mb[0]==1:
            screen.blit(canBuff,(0,0))
            draw.rect(screen,c,(nx,ny,mx-nx,my-ny),2)
        if tool=='circle' and mb[0]==1:
            screen.blit(canBuff,(0,0))
            cx,cy=mx-nx,my-ny
            if cx==0:
                cx=1
            if cy==0:
                cy=1
            nNorm=Rect(nx,ny,cx,cy)
            nNorm.normalize()
            if min(abs(cx),abs(cy))>size*2:
                draw.ellipse(screen,c,nNorm,size)
            else:
                draw.ellipse(screen,c,nNorm,0)
            
        

                       
            
            
    

        ox=mx
        oy=my
             
        

        screen.set_clip(None)


    display.flip()
    
quit()
