from pygame import *
import sys
# Initialize the game engine
init()

# define colors
black = [0, 0, 0]
white = [255,255,255]
color = (255,255,255,255)
red = [255,0,0]

# set screen
size=[640,480]
screen=display.set_mode(size)
display.set_caption("Flood Fill")

# set recursion limit
sys.setrecursionlimit(1500000000)

def check_quit(event):
    if event.type == QUIT: # If user clicked close
        return True # Flag that we are done so we exit this loop
    return False

# recursive color fill
def floodfill(name,x,y):
	get=name.get_at((x,y))
	if get==color:
		name.set_at((x,y),red)
		display.update()
		floodfill(name,x+1,y)
		floodfill(name,x-1,y)
		floodfill(name,x,y+1)
		floodfill(name,x,y-1)
	return

# set screen
size=[640,480]
screen=display.set_mode(size)
display.set_caption("Flood Fill")

screen.fill(white)
display.update()

# take a point inside the polygon
x1 =295 
y1 =440

# body of the program
done = False
while done==False:
    for event in event.get(): # User did something
        done=check_quit(event)
	draw.polygon(screen,black,((200,350),(300,100),(400,350),(300,450)),2)
	display.update()

	floodfill(screen,x1,y1)
	display.update()
# exit from pygame
quit()
