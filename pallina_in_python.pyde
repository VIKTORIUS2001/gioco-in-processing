r=0
g=0
b=0
r2=0
g2=0
b2=0
xrac1=330
yrac1=600-25
xrad=50
yrad=50
xrad2=0
yrad2=0
xpos=0;
ypos=0;
xVers=1
yVers=-1
def setup():
    global xpos,ypos
    xpos=200
    ypos=200
    size(800,600)
    background(62)
    fill(0,255,0)
    rect(60,4,100,140)
    fill(255,255,255)
    rect(160,4,100,140)
    fill(255,0,0)
    rect(260,4,100,140)
    fill(255,215,255)
    triangle(210,10,170,80,250,80)
    fill(205,0,0)
    rect(20,4,40,300)
    
    
def tocca(xpos,ypos,xrac1,yrac1,yVers):
    if(ypos>=yrac1-25 and (xpos+25>xrac1 and xpos-25<xrac1+100) ):
        return(True)
    else:
        return(False)
        
def draw():
    global xpos,ypos,xVers,yVers,r,g,b,r2,b2,g2,xrad,yrad,xrad2,yrad2,xrac1,yra1
    xpos=xpos+xVers*4
    ypos=ypos+yVers*4
    background(62)
    r=r2
    g=g2
    b=b2
    fill(r,g,b)
    ellipse(xpos,ypos,xrad,yrad)
    if(xpos>width-15 or xpos<0+15):
        xVers*=-1
        r2=random(0,255)
        g2=random(0,255)
        b2=random(0,255)
        
    if(ypos>height-15 or ypos<0+15):
        yVers*=-1
        r2=random(0,255)
        g2=random(0,255)
        b2=random(0,255)
        
    if tocca(xpos,ypos,xrac1,yrac1,yVers):
        yVers*=-1
        
    fill(255,255,255)    
    rect(xrac1,yrac1,100,25)

def keyPressed():
    global xrac1
    if(keyCode==LEFT):
        xrac1-=15
    if(keyCode==RIGHT):
        xrac1+=15

    

    
