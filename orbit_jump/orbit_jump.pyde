#planet jump
import math
import random

#need to adjust the initial location when getting into a new orbit
#decide the direction of rotation
#add propeller effect on the trail
#add multiply orbits to gchoose from

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

class Items:
    def __init__(self,interval,imageName,speed,w,h,angle):
        self.x=random.randint(0,game.w)
        self.y=0
        self.w=w
        self.h=h
        self.interval=interval
        self.img=loadImage(path+imageName)
        self.speed=speed
        self.angle=angle
        
    def collision(self):
        if game.distance(game.ship.x,game.ship.y,self.x,self.y+self.h)>game.ship.r:
            return True
        
    def display(self):
        if self.x>=0:
            image(self.img,self.x-game.x,self.y,self.w,self.h)
        self.x-=self.speed
        self.y+=self.speed/self.angle
        
class ShootingStar(Items):
    def __init__(self,interval,imageName,speed,w,h,angle):
        Items.__init__(self,interval,imageName,speed,w,h,angle)
        
                
class BgShootingStar(Items):
    def __init__(self,interval,imageName,speed,w,h,angle):
        Items.__init__(self,interval,imageName,speed,w,h,angle)

        
        
class Game:
    def __init__(self,numPlanet):
        self.numPlanet=numPlanet
        self.x=0
        self.y=0
        self.w=1280
        self.h=837
        self.l=1488
        self.x0=0 #the coordinate when it starts to leave the planet
        self.y0=0
        self.score=0
        self.fire=loadImage(path+'/images/bigfire.png')
        
        
        
    def bgimg(self):
        self.bgimg=loadImage(path+"/images/galaxy.jpg")

    
    def creategame(self):
        self.gameover=False
        self.showfire=False
        self.numFrame=0
        self.time=0
        
        #create the planets
        self.planets=[]
        f = open(path+'/images/stage1.csv','r')
        for l in f:
            l = l.strip().split(",")
            if l[0]=="ShootingStar":
                self.star=ShootingStar(int(l[1]),l[2],int(l[3]),int(l[4]),int(l[5]),int(l[6]))    
            # elif l[0]=="Meteorolite":
            #     self.meteorolite=Meteorolite(int(l[1]),l[2],int(l[3]),int(l[4]),int(l[5]))
            elif l[0]=="BgShootingStar":
                self.bgstar=BgShootingStar(int(l[1]),l[2],int(l[3]),int(l[4]),int(l[5]),int(l[6]))
            elif l[0]=="Planet":
                self.planets.append(Planet(int(l[1]),int(l[2]),int(l[3]),path+l[4]))
        f.close()
        
        print self.planets

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
        for p in self.planets:
            if p!=self.ship.planet and self.distance(self.ship.x,self.ship.y,p.x,p.y)<=(p.o+self.ship.r):
                self.score+=50
                self.revolve=True
                self.freefly=0
                self.cosinConnect=(self.ship.planet.x-p.x)/self.distance(self.ship.planet.x,self.ship.planet.y,p.x,p.y)
             #decide the flying direction       
                if self.ship.planet.y>=p.y:
                    self.flydir="up"
                else:
                    self.flydir="down"
                                
                self.ship.planet=p
                self.string=self.distance(self.ship.x,self.ship.y,p.x+p.o,p.y) #intermediate step
                self.cosangle=((p.o**2+p.o**2-self.string**2)/2)/(2*p.o**2)
                self.angle=math.acos(self.cosangle)            
                if self.ship.y>p.y:
                    self.angle=2*math.pi-self.angle
               
                self.decide_direction()
                break

                
    def decide_direction(self):   #get the rotation deirection
        if self.flydir=="down":
            self.connectangle=math.acos(self.cosinConnect)
            if self.angle>self.connectangle:
                self.clockwise=False
            else:
                self.clockwise=True
             
        else:
            self.connectangle=2*math.pi-math.acos(self.cosinConnect)
            if self.angle>self.connectangle:
                self.clockwise=True
            else:
                self.clockwise=False
                
    def moveFrame(self):

        image(self.bgimg,0,0,self.w-self.x%self.w,self.h,self.x%self.w,0,self.w,self.h)
        image(self.bgimg,self.w-self.x%self.w,0,self.x%self.w,self.h,0,0,self.x%self.w,self.h)
        
    def showItems(self):
        if self.time%self.star.interval==0:
            self.showStar=True
        if self.time%self.bgstar.interval==0:
            self.showbgStar=True
        

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
        self.numFrame+=1
        if self.numFrame%60==0:
            self.time+=1
        self.update()
        self.moveFrame()
        self.showItems()
        for p in self.planets:
            p.display()
            noFill()
            stroke(0,255,255)
            ellipse(p.x-self.x,p.y,p.o*2,p.o*2)
            
        if self.showStar==True:
            if self.star.x+self.star.w>0:
                self.star.display()
            else:
                self.showStar=False
                self.star.x=random.randint(0,self.w)
                self.star.y=0
                
        if self.showbgStar==True:
            if self.bgstar.x+self.bgstar.w>0:
                self.bgstar.display()
            else:
                self.bgshowStar=False
                self.bgstar.x=random.randint(0,self.w)
                self.bgstar.y=random.randint(0,self.h//2)

            
        #while hit push, the fire effect that last half a second
        if self.showfire:
            image(self.fire,self.ship.x-self.ship.r-20-self.x,self.ship.y-self.ship.r+10,self.ship.r+70,self.ship.r+10)

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
        game.showfire=True

def keyReleased():
    if keyCode==32:
        game.revolve=False
        game.x0=game.ship.x
        game.y0=game.ship.y
        game.showfire=False
    


        

        
