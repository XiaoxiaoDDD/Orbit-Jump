#planet jump

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
        
        image(self.img,self.x-self.r, self.y-self.r, 2*self.r, 2*self.r)
    
    
class Ship:
    def __init__(self,x,y,planet):
        self.x=x
        self.y=y
        self.planet=planet
        self.theta=0
        self.img=loadImage(path+"/images/spaceship.png")
        self.r=30
    
        
    def display(self):
        image(self.img,self.x-self.r,self.y-self.r,self.r*2,self.r*2)
        
        
class Game:
    def __init__(self,numPlanet):
        self.numPlanet=numPlanet
        self.x=400
        self.w=1280
        self.h=837
        self.l=1488
        
    def bgimg(self):
        self.bgimg=loadImage(path+"/images/galaxy.jpg")
    
    def displaybg(self):
        image(self.bgimg,0,0,self.w-self.x%self.w,self.h,self.x%self.w,0,self.w,self.h)
        image(self.bgimg,self.w-self.x%self.w,0,self.x%self.w,self.h,0,0,self.x%self.w,self.h)
    
    def creategame(self):
        #create the planets
        self.planets=[]
        self.planets.append(Planet(100,70,70,path+"/images/0.png"))
        
        #create the spaceship
        self.ship=Ship(50,50,0)
        #revolving
        self.angle=0
        
    def revolve(self):
        self.ship.x=self.planets[self.ship.planet].x+self.planets[self.ship.planet].o*cos(self.angle)
        self.ship.y=self.planets[self.ship.planet].y+self.planets[self.ship.planet].o*sin(self.angle)
        
        
     
    def display(self):
        self.displaybg()
        for i in self.planets:
            i.display()
        self.revolve()
        self.ship.display()
        
game=Game(7)

def setup():
    size(game.w,game.h)
    game.bgimg()
    game.creategame()

def draw():
    game.display()
    game.angle+=0.1
    
def mousePressed():
    pass
def mouseReleased():
    pass
    
def keyPressed():
    pass

        
