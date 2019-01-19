#Floodfill
def floodfill():
    mx,my=mouse.get_pos()
    newColor=color
    oldColor=screen.get_at((mx,my))
    if newColor == oldColor:
        return 0
    oldSet = set()
    oldSet.add((mx,my))
    while len(oldSet) > 0:
        x,y = oldSet.pop()
        if canvasRect.collidepoint(x,y) and screen.get_at((x,y)) == oldColor:
            screen.set_at((x,y),newColor)
            oldSet.add((x+1,y))
            oldSet.add((x-1,y))
            oldSet.add((x,y+1))
            oldSet.add((x,y-1))
