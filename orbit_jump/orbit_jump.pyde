#planet jump
import math

#need to adjust the initial location when getting into a new orbit
#decide the direction of rotation
#add propeller effect on the trail
#add multiply orbits to choose from

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
    def __init__(self,x,y,centralPlanet):
        self.x=x
        self.y=y
        self.planet=centralPlanet
        # self.theta=0
        self.img=loadImage(path+"/images/spaceship.png")
        self.r=30
        
    
        
    def display(self):
        image(self.img,self.x-self.r-game.x,self.y-self.r,self.r*2,self.r*2)
        
        
class Game:
    def __init__(self,numPlanet):
        self.numPlanet=numPlanet
        self.x=0
        self.w=1280
        self.h=837
        self.l=1488
        self.x0=0 #the coordinate when it starts to leave the planet
        self.y0=0
        
        
    def bgimg(self):
        self.bgimg=loadImage(path+"/images/galaxy.jpg")

    
    def creategame(self):
        #create the planets
        self.planets=[]
        self.planets.append(Planet(150,150,70,path+"/images/0.png"))
        self.planets.append(Planet(400,800,40,path+"/images/1.png"))
        self.planets.append(Planet(700,500,60,path+"/images/2.png"))
        self.planets.append(Planet(900,200,50,path+"/images/3.png"))
        self.planets.append(Planet(1200,600,90,path+"/images/4.png"))
        #create the spaceship
        self.ship=Ship(0,0,self.planets[0])
        self.revolve=True
        #revolving
        self.angle=0
        self.clockwise=False
        self.freefly=0 #the time the spaceship travels between planets
        
    def distance(self,x1,y1,x2,y2):
        return ((x1-x2)**2+(y1-y2)**2)**0.5

    
    def neworbit(self):
        if self.revolve==False:
            for p in self.planets:
                if p!=self.ship.planet and self.distance(self.ship.x,self.ship.y,p.x,p.y)<=(p.o+self.ship.r):
                    self.revolve=True
                    self.cosinConnect=(self.ship.planet.x-p.x)/self.distance(self.ship.planet.x,self.ship.planet.y,p.x,p.y)
                    #print self.cosinConnect
                    self.ship.planet=p
                    self.freefly=0
                    self.string=self.distance(self.ship.x,self.ship.y,p.x+p.o,p.y)
                    self.cosangle=((p.o**2+p.o**2-self.string**2)/2)/(2*p.o**2)
                    # self.cosangle=1-(self.string**2/(2*p.o**2))
                    print self.cosangle
                    self.angle=math.acos(self.cosangle) #this is the angle to the horizontal line
                    
                    #decide the direction of revolvement
                    if self.cosangle>self.cosinConnect:
                        self.clockwise=True
                    else:
                        self.clockwise=False
                    break
            
    def moveFrame(self):

        image(self.bgimg,0,0,self.w-self.x%self.w,self.h,self.x%self.w,0,self.w,self.h)
        image(self.bgimg,self.w-self.x%self.w,0,self.x%self.w,self.h,0,0,self.x%self.w,self.h)
        
    def update(self):
        #make the ship revolve around the selected planet
        if self.revolve==True:
            self.ship.x=self.ship.planet.x+self.ship.planet.o*cos(self.angle)
            self.ship.y=self.ship.planet.y-self.ship.planet.o*sin(self.angle)
        else:
            #travel between planets
            if self.clockwise==False:
                self.ship.x=self.x0-self.freefly*sin(math.pi-self.angle)
                self.ship.y=self.y0+self.freefly*cos(math.pi-self.angle)
            else:
                self.ship.x=self.x0+self.freefly*sin(math.pi-self.angle)
                self.ship.y=self.y0-self.freefly*cos(math.pi-self.angle)
            
        
        if self.revolve==False:
            if self.ship.x>self.w/2:
                self.x=int(self.ship.x-self.w/2)
      
            
        self.neworbit()
            

     
    def display(self):
        self.update()
        self.moveFrame()
        for p in self.planets:
            p.display()
            noFill()
            stroke(0,255,255)
            ellipse(p.x-self.x,p.y,p.o*2,p.o*2)
        
        self.ship.display()
        
game=Game(7)

def setup():
    size(game.w,game.h)
    game.bgimg()
    game.creategame()

def draw():
    game.display()
    if game.revolve==True:
        if game.clockwise==False:
            game.angle+=0.05
        else:
            game.angle-=0.05
    else:
        game.freefly+=6
    
def mousePressed():
    pass
def mouseReleased():
    pass
    
def keyPressed():
    if keyCode==32:
        game.revolve=False
        game.x0=game.ship.x
        game.y0=game.ship.y
    


        

        
