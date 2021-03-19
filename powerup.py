from config import *

class Power:
    
    def __init__(self,sp,x,y,num,tinka):
        self.x = x
        self.y = y+10
        self.speedy = 2
        self.speedx = sp
        self.num = num
        self.start = int(tinka)
        self.starteff = 0
        self.active = True
        self.indexx = 0
        self.set = 0
        self.confi =0 
        self.moving = [-1,0,1,3,5,8,12]
    
    def print_data(self):
        print(self.x,self.y,self.speedy,self.num,self.start,self.starteff,self.active)
    
    # def print_label(self):
    #     print()
    
    def restore(self,sscene,ppadle,bball):
        msg3 = "\n>> " +  Fore.BLACK + Back.WHITE + " MESSAGE : [POWERUP DEACTIVATED] "  + RESET 
        idiotbox = False
        self.active=False
        if(self.num==1):
            msg3 = msg3 + " : Paddle spread deactivated"
            idiotbox = True
            ppadle.degrade()
            bball.spread = False
        if(self.num==2):
            msg3 = msg3 + " : Paddle shrink deactivated"
            idiotbox = True
            ppadle.upgrade()
            bball.shrink = False
        if(self.num==3):
            msg3 = msg3 + " : Sticky ball deactivated"
            idiotbox = True
            bball.sticky=False
        if(self.num==4):
            msg3 = msg3 + " : Thruball deactivated"
            idiotbox = True
            bball.thruball=False
        if(self.num==5):
            msg3 = msg3 + " : Fast ball deactivated"
            idiotbox = True
            bball.fastball=False
            sscene.speed = sscene.speed*2
        if(self.num==6):
            msg3 = msg3 + " : Mutiball deactivated"
            idiotbox = True
            bball.multiballflag = False
            bball.multiball = False
        if(idiotbox == True):
            print(msg3)
        return False

    def power_move(self,sscene,bball,ppadle,cclock):
        if(self.set ==0):
            self.set = self.y
        self.y = self.set + self.moving[self.indexx]
        self.indexx +=1
        if(self.x==5 or self.x == 77 ):
            self.speedx = -1*self.speedx
        if(self.confi!=0):
            self.x = self.x + self.speedx
        if(self.confi == 0):
            tt = self.x*5 + 11
            self.x = tt
            self.confi +=1
        
        
        if(self.y == 25 and self.num !=  6):
            if(tt >= ppadle.x and tt <= ppadle.x + ppadle.length):
                self.starteff = cclock.return_val()
                self.collect(sscene,bball,ppadle,cclock)
        elif(self.y == 27 and self.num == 6):
            if(tt >= ppadle.x and tt <= ppadle.x + ppadle.length):
                self.starteff = cclock.return_val()
                self.collect(sscene,bball,ppadle,cclock)
    
    def collect(self,sscene,bball,ppadle,cclock):
        idiotbox = False
        msg3 = "\n>> " +  Fore.BLACK + Back.WHITE + " MESSAGE : [POWERUP ACTIVATED] "  + RESET 
        num = self.num
        
        if(num == 1):
            idiotbox = True
            msg3 = msg3 + " : Paddle spread activated"
            ppadle.upgrade()
            bball.spread = True
        
        if(num == 2):
            idiotbox = True
            msg3 = msg3 + " : Paddle shrink activated"
            ppadle.degrade()
            bball.shrink = True
        if(num == 3):
            idiotbox = True
            msg3 = msg3 + " : Sticky ball activated"
            bball.sticky=True
        
        if(num == 4):
            idiotbox = True
            msg3 = msg3 + " : Thruball activated"
            bball.thruball = True
        
        if(num == 5):
            idiotbox = True
            msg3 = msg3 + " : Fast ball activated"
            bball.fastball = True
            sscene.speed = sscene.speed/2
        
        if(num == 6):
            idiotbox = True
            msg3 = msg3 + " : Mutiball activated"
            bball.multiball = True
            bball.x2=bball.x
            bball.y2=bball.y
            bball.speedx2 = -1*bball.speedx 
            bball.speedy2 = -1*bball.speedy 
        if(idiotbox == True):
            print(msg3)
        return False