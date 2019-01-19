from pygame import *

screen = display.set_mode((1000,800))
colors = image.load("Images/colors.png")
colors = transform.smoothscale(colors,(300,175))
screen.blit(colors,(130,600))
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
   
    display.flip()

quit()
