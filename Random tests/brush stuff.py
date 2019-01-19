#Brush stuff
bx=mx-ox#Mx is mouse pos and ox is your omx 
by=my-oy
dist=hypot(bx,by)
dist=max(1,dist)
sx=bx/dist
sy=by/dist
        
for i in range(int(dist)):
    dx=(ox+sx*i)#Draws a circle at every pixel
    dy=(oy+sy*i)
            
    draw.circle(screen,color,(int(dx),int(dy)),20)
