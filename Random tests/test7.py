import pygame
import math
import random
import sys
sys.setrecursionlimit(999999999)
from pygame.locals import *
SIZE = 640, 480
pygame.init()
screen = pygame.display.set_mode(SIZE)
FPSCLOCK = pygame.time.Clock()
done = False   
def ff(screen,cord,target,replacement):
    x,y=cord
    if x<0 or y<0 or x>640 or y>480:
        return
    if screen.get_at(cord) != target:
        return

    screen.set_at(cord,replacement)

    ff(screen,(x+1,y),target,replacement);
    ff(screen,(x-1,y),target,replacement);
    ff(screen,(x,y+1),target,replacement);
    ff(screen,(x,y-1),target,replacement);
    return;
screen.fill(Color("white"))
while not done:

    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
        elif e.type == MOUSEBUTTONDOWN:
            mouse_pos =  pygame.mouse.get_pos()
            ff(screen,mouse_pos,Color("white"),Color("red"))



    for x in range(1,240,10):
        pygame.draw.circle(screen,Color("pink"),(320,240),x,1)    

    pygame.display.flip()   

    FPSCLOCK.tick(30)
