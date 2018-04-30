#planet jump
import math
import random

#add planet features like supergravity,blackhole etc
#add win/gameover,score display
#add menu 
#add ranks

path=os.getcwd()
# print path

class Planet:
    def __init__(self,x,y,r,name,type):
        self.x=x
        self.y=y
        self.r=r
        self.o=r*1.8
        self.img=loadImage(name)
        self.type=type
        
    def display(self):
        image(self.img,self.x-self.r-game.x, self.y-self.r, 2*self.r, 2*self.r)  

class Blackhole(Planet):
    def __init__(self,x,y,r,name,type):
        Planet.__init__(self,x,y,r,name,type)
        if self.type=='reverse':
            self.o=20
        
        
    def display(self):
        # tint(255,120)
        image(self.img,self.x-3*self.r-game.x, self.y-3*self.r, 6*self.r, 6*self.r)  
        noTint()
        
class Pulsating(Planet):
    def __init__(self,x,y,r,name,type):
        Planet.__init__(self,x,y,r,name,type)
        self.o=self.r*2.5
        
    def display(self):
        if self.o>=self.r*2.5:
            self.vo=-0.5
        elif self.o<=self.r*1.3:
            self.vo=0.5
        self.o+=self.vo
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
        
    # def collision(self):
    #     if game.distance(game.ship.x,game.ship.y,self.x,self.y+self.h)>game.ship.r:
    #         return True
        
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
    def __init__(self):
        self.w=1280
        self.h=837
        # self.l=1488
        self.x0=0 #the coordinate when it starts to leave the planet
        self.y0=0
        self.score=0
        self.fire=loadImage(path+'/images/bigfire.png')
        self.stage=0
        self.player=""

        
        
        
    def bgimg(self):
        self.bgimg=loadImage(path+"/images/galaxy.jpg")

    
    def creategame(self):
        #self.gameover=False
        self.showfire=False
        self.numFrame=0
        self.time=0
        self.x=0
        self.y=0
        self.result='lost'

            #create the planets
        self.planets=[]
        f = open(path+'/images/stage'+str(self.stage)+'.csv','r')
        for l in f:
            l = l.strip().split(",")
            if l[0]=="ShootingStar":
                self.star=ShootingStar(int(l[1]),l[2],int(l[3]),int(l[4]),int(l[5]),int(l[6]),)    
            # elif l[0]=="Meteorolite":
            #     self.meteorolite=Meteorolite(int(l[1]),l[2],int(l[3]),int(l[4]),int(l[5]))
            elif l[0]=="BgShootingStar":
                self.bgstar=BgShootingStar(int(l[1]),l[2],int(l[3]),int(l[4]),int(l[5]),int(l[6]))
            elif l[0]=="Planet":
                if l[5]=='simple' or l[5]=='superspin':
                    self.planets.append(Planet(int(l[1]),int(l[2]),int(l[3]),path+l[4],l[5]))
                elif l[5]=='blackhole'or l[5]=='reverse':
                    self.planets.append(Blackhole(int(l[1]),int(l[2]),int(l[3]),path+l[4],l[5]))
                elif l[5]=='pulsating':
                    self.planets.append(Pulsating(int(l[1]),int(l[2]),int(l[3]),path+l[4],l[5]))
        f.close()
        

        if self.stage>0 and self.stage<4:
            #create the spaceship
            self.ship=Ship(self.planets[0].x+self.planets[0].o,self.planets[0].y,self.planets[0])
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
                    self.freefly=0
                    self.cosinConnect=(self.ship.planet.x-p.x)/self.distance(self.ship.planet.x,self.ship.planet.y,p.x,p.y)
                #decide the flying direction       
                    if self.ship.planet.y>=p.y:
                        self.flydir="up"
                    else:
                        self.flydir="down"
                                    
                    self.ship.planet=p
                    
                    if p.type=='blackhole':
                        self.score+=50
                        if self.stage==3:
                            self.result='win'
                    else:
                        self.score+=10
                        
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
            
    def next(self):
        self.stage+=1
        if self.stage>0 and self.stage<4:
            self.creategame()

    def update(self):
        if self.revolve==True:
            if self.clockwise==False:
                self.angle+=0.05
                if self.ship.planet.type=='superspin':
                    self.angle+=0.05
                
            else:
                self.angle-=0.05
                if self.ship.planet.type=='superspin':
                    self.angle-=0.05
        else:
            self.freefly+=6
    
        #make the ship revolve around the selected planet
        if self.revolve==True:
            self.ship.x=self.ship.planet.x+self.ship.planet.o*cos(self.angle)
            self.ship.y=self.ship.planet.y-self.ship.planet.o*sin(self.angle)
            if self.ship.planet.type=='blackhole':
                if self.ship.planet.o>10:
                    self.ship.planet.o-=0.8
                else:
                    self.next()
            if self.ship.planet.type=='reverse':
                if self.ship.planet.o<80:
                    self.ship.planet.o+=0.8

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

        
        if self.stage>0 and self.stage<4:
            self.update()
            self.moveFrame()
            self.showItems()
            textSize(20)
            text('SCORE '+str(self.score),20,20)
            for p in self.planets:
                p.display()
                noFill()
                if p.type=='superspin':
                    stroke(255,0,0)
                else:
                    stroke(0,255,255)
                ellipse(p.x-self.x,p.y,p.o*2,p.o*2)
                        
            #while hit push, the fire effect that last half a second
            if self.showfire:
                image(self.fire,self.ship.x-self.ship.r-20-self.x,self.ship.y-self.ship.r+10,self.ship.r+70,self.ship.r+10)

            self.ship.display()
            
            if self.ship.x<=-100 or self.ship.x>3000 or self.ship.y<=-100 or self.ship.y>=self.h+200:
                self.stage=4
                self.x=0
                self.result='lost'
        
                
        elif self.stage==0:
            self.x=0
            self.moveFrame()
            textSize(50)
            if 590<mouseX<750 and 330<mouseY<375:
                fill(0,255,255)
            else:
                fill(255)
            text('   PLAY',self.w//2-80,self.h//2-50)
            if 450<mouseX<800 and 420<mouseY<480:
                fill(0,255,255)
            else:
                fill(255)
            text('RECORDS',self.w//2-80,self.h//2+50)
            
                        
        elif self.stage==4:
            self.x=0
            self.moveFrame()
            textSize(50)
            if self.result=='lost':
                text("The spaceship is forever lost in the universe.",self.w//2-500,self.h//2-150)
            else:
                text("You have reached your destination",self.w//2-500,self.h//2-150)
            text('Your score is '+str(self.score)+'.',self.w//2-500,self.h//2-50)
            text('please enter your name:'+self.player,self.w//2-500,self.h//2+50)
            #text(self.player,self.w//2-500,self.h//2+150)
        
                        
        elif self.stage==5:
            self.x=0
            self.moveFrame()
            textSize(40)
            fill(255)
            text('TOP10',self.w//2-80,100)
            textSize(30)
            f=open(path+'/images/records.csv','r')
            self.records={}
            self.scores=[]
            
            #put the record into the dic and list
            for line in f:
                l=line.split(',')
                self.records[l[0]]=int(l[1])
                self.scores.append(int(l[1]))
                
            # sort the records in descending order
            self.scores.sort()
            self.scores.reverse()
            
            #print the TOP10 records
            n=1
            for i in self.scores:
                for key in self.records:
                    if self.records[key]==i:
                        fill(255)
                        text(key+' '+str(self.records.pop((key),'unfound')),self.w//2-80,100+n*50)
                        n+=1
                        if n==11:
                            break
                if n==11:
                    break

                
            f.close()
            
            textSize(50)
            if 550<mouseX<715 and 645<mouseY<695:
                fill(0,255,255)
            else:
                fill(255)
            text('MENU',self.w//2-80,self.h-150)
     


        self.showItems()
        self.displayStar()
        
    def displayStar(self):  
          
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
   
    def pressKey(self):
        
        if self.stage>0 and self.stage<4:
            if self.ship.planet.type !='blackhole':
                if keyCode==32 and self.revolve==True:
                    self.showfire=True
                    self.angle+=0.05
        if game.stage==4:
            if keyCode == 8:
                self.player = self.player[:len(self.player)-1]
            elif keyCode == 10:
                f=open(path+'/images/records.csv','a')
                f.write(game.player+','+str(self.score)+'\n')
                f.close()
                self.stage=0
                self.score=0
                self.player=""
            elif type(key) != int:
                self.player += key
                




game=Game()

def setup():
    size(game.w,game.h)
    game.bgimg()
    game.creategame()

def draw():
    game.display()

    
def mouseClicked():
    # print(mouseX,mouseY)
    if game.stage==0:
        if 590<mouseX<750 and 330<mouseY<375:
            game.stage=1
            game.creategame()
        if 450<mouseX<800 and 420<mouseY<480:
            game.stage=5
    if game.stage==5:
        if 550<mouseX<715 and 645<mouseY<695:
            game.stage=0
        

    
def keyPressed():
    game.pressKey()
    
def keyReleased():
    if game.stage>0 and game.stage<4:
        if keyCode==32 and game.revolve==True:
            if game.ship.planet.type !='blackhole':
                game.revolve=False
                game.x0=game.ship.x
                game.y0=game.ship.y
                game.showfire=False
            
    
    
        

                       

        
