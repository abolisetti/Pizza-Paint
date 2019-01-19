def set_at((x,y), surfaceA, patternA):
	gx=x%patternA.shape[0]#width
	gy=y%patternA.shape[1]#height
	new_color=patternA[gx][gy]
	surfaceA[x][y]=new_color

def get_at((x,y), patternA):
	gx=x%patternA.shape[0]#width
	gy=y%patternA.shape[1]#height
	return patternA[gx][gy]

def push(rect,stack,(y,x,x2,dy)):# push for seed_fill
	if y+dy>=rect.bottom or y+dy<rect.top : return #don't fall of the
bottom or top of the surface.
	else : stack.append((y, x, x2, dy))
	
def seed_fillA(surface, x, y, pattern):# sk is for skip. It was a goto
   surface.lock()
   pattern.lock()
   (minx,miny,maxx,maxy)=(x,y,x,y)
   surfaceA=pygame.surfarray.pixels2d(surface)
   patternA=pygame.surfarray.pixels2d(pattern)
   if patternA==None : return
   stack=[]
   rect=Rect((0,0),surfaceA.shape)
   old_color = surfaceA[x][y]
   new_color = get_at((x, y), patternA)#make sure that surface color
is not the same as the pattern color
   if old_color == new_color : return #can't fill with same color
   if not rect.collidepoint(x, y) : return #can't fill off the surface
   push(rect,stack,(y, x, x, 1)) # needed in some cases
   push(rect,stack,(y+1, x, x, -1)) # seed segment (popped 1st)
   sk=0
   while len(stack)>0 :
	(y,x1,x2,dy)=stack.pop()
	y+=dy
	x=x1
	while x >= rect.left and surfaceA[x][y] == old_color : #bigger than
the left edge and point is old color
		#new_color=(randint(0,255),randint(0,255),randint(0,255))
		set_at((x,y), surfaceA, patternA)
		if minx>x : minx=x #find max and min x and y for Rect
		if miny>y : miny=y
		if maxx<x : maxx=x
		if maxy<y : maxy=y
		x-=1
	if( x >= x1 ) : sk=1
	if sk==0 : left = x+1
	if sk==0 and left < x1 : push(rect,stack,(y, left, x1-1, -dy)) # leak on left?
	if sk==0 : x = x1+1
	while True :
		if sk==0 :
			while x<rect.right and surfaceA[x][y] == old_color : #draw dot to
right if right needs color
				#new_color=(randint(0,255),randint(0,255),randint(0,255))
				set_at((x,y), surfaceA, patternA)
				if minx>x : minx=x
				if miny>y : miny=y
				if maxx<x : maxx=x
				if maxy<y : maxy=y
				#surface.set_at((x, y), new_color)
				x+=1
			push(rect,stack,(y, left, x-1,  dy))#look on the other side of
point, added to stack
			if x > x2+1 : push(rect,stack,(y,x2+1, x-1,  -dy)) # leak on right?
		x+=1; sk=0
		while  x <= x2 and surfaceA[x][y] != old_color : #draw right if ??
			x+=1
		left = x
		if x>x2 : break
   surface.unlock()
   pattern.unlock()
   return Rect(minx,miny,maxx-minx+1,maxy-miny+1)
