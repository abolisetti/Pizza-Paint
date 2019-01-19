from pygame import *
    
screen = display.set_mode((800,600))

start = 0,0
size = 10
running =True
a=1
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False        
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    ox,oy=1,1

    if mb[0]==1:
        if a==1:
            ox=mx
            oy=my
        screen.fill((0,0,0))
        draw.rect(screen,(255,0,0),(ox,oy,mx-ox,my-oy),1)
        
    a+=1
    display.flip()

quit()
