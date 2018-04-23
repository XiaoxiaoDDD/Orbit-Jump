#planet jump
import math

path=os.getcwd()
# print path

class Planet:
    def __init__(self,x,y,r,name):
        self.x=x
        self.y=y
        self.r=r
        self.o=r*1.8
        self.name=name
        self.img=loadImage(self.name)
        
    def display(self):
        
        image(self.img,self.x-self.r-game.x, self.y-self.r, 2*self.r, 2*self.r)
    
    
class Ship:
    def __init__(self,x,y,planet):
        self.x=x
        self.y=y
        self.planet=planet
        self.theta=0
        self.img=loadImage(path+"/images/spaceship.png")
        self.r=30
    
        
    def display(self):
        image(self.img,self.x-self.r-game.x,self.y-self.r,self.r*2,self.r*2)
        
        
class Game:
    def __init__(self,numPlanet):
        self.numPlanet=numPlanet
        self.x=400
        self.w=1280
        self.h=837
        self.l=1488
        self.x0=0 #the coordinate when it starts to leave the planet
        self.y0=0
        
        
    def bgimg(self):
        self.bgimg=loadImage(path+"/images/galaxy.jpg")
    
    def moveFrame(self):
        image(self.bgimg,0,0,self.w-self.x%self.w,self.h,self.x%self.w,0,self.w,self.h)
        image(self.bgimg,self.w-self.x%self.w,0,self.x%self.w,self.h,0,0,self.x%self.w,self.h)

    
    def creategame(self):
        #create the planets
        self.planets=[]
        self.planets.append(Planet(200,200,70,path+"/images/0.png"))
        
        #create the spaceship
        self.ship=Ship(0,0,0)
        self.revolve=True
        #revolving
        self.angle=0
        self.freefly=0 #the time the spaceship travels between planets
        
    def update(self):
        if self.revolve==True:
            self.ship.x=self.planets[self.ship.planet].x+self.planets[self.ship.planet].o*cos(self.angle)
            self.ship.y=self.planets[self.ship.planet].y-self.planets[self.ship.planet].o*sin(self.angle)
        else:
            self.ship.x=self.x0-self.freefly*cos(math.pi/2-self.angle)
            self.ship.y=self.y0-self.freefly*sin(math.pi/2-self.angle)
            
        if self.ship.x>self.w/2:
            self.x=int(self.ship.x-self.w/2)
        else:
            self.x=0
     
    def display(self):
        self.update()
            
        self.moveFrame()
        for i in self.planets:
            i.display()
        self.ship.display()
        
game=Game(7)

def setup():
    size(game.w,game.h)
    game.bgimg()
    game.creategame()

def draw():
    game.display()
    if game.revolve==True:
        game.angle+=0.1
    else:
        game.freefly+=10
    
def mousePressed():
    pass
def mouseReleased():
    pass
    
def keyPressed():
    if keyCode==32:
        game.revolve=False
        game.x0=game.ship.x
        game.y0=game.ship.y
    


        

        
