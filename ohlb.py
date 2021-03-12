import colorama
from config import RESET, SPEED
from powerup import *
import random
from config import *
from messages import gameover

def check_buddy(ok):
    if(ok>=0 and ok<=5):
        return True
    return False

class Ball:
    def __init__(self,ppadle):
        self.die = False
        self.spread = False
        self.spread_time = False
        self.shrink = False
        self.shrink_time = False
        self.thruball = False
        self.thruball_time = False
        self.sticky = False
        self.sticky_time = False
        self.fastball = False
        self.fastball_time = False
        self.multiball = False
        self.multiball_time = False
        self.lb = 10
        self.ub = 15 
        self.x = 0
        self.y = 0
        self.speedx = 0
        self.speedy = 0
        self.x2=0
        self.y2=0
        self.speedx2 = 0
        self.speedy2 = 0
        self.collison = False
        self.start_throw(ppadle)
        
    def get_fastball(self):
        return self.fastball
    
    def chickibum(self,y,ar):
        re = 0
        if(y==0):
            temp = 13
            for i in range(0,13):
                ar[0][i]=0
                if(ar[1][i]>0 and ar[1][i]<8):
                    temp = temp + ar[1][i]
                    ar[1][i]=0
            re = temp
        elif(y==5):
            temp = 13
            for i in range(0,13):
                ar[5][i]=0
                if(ar[4][i]>0 and ar[4][i]<8):
                    temp = temp + ar[4][i]
                    ar[4][i]=0
            re = temp
        else:
            temp = 13
            for i in range(0,13):
                ar[y][i]=0
                if(ar[y-1][i]>0 and ar[y-1][i]<8):
                    temp = temp + ar[y-1][i]
                    ar[y-1][i]=0
                if(ar[y+1][i]>0 and ar[y+1][i]<8):
                    temp = temp + ar[y+1][i]
                    ar[y+1][i]=0
            re = temp
        return re

    def start_throw(self,ppadle):
        # temp = random.randrange(1,ppadle.length)
        temp = 7
        self.x = ppadle.x + temp
        temp = temp // ppadle.scale
        # self.speedx = self.speedx + temp - (ppadle.length//2)
        self.y = 27
        self.speedy = 0
        self.speedx = 0
        
    def launch_ball(self,a,ppadle):
        if(a==1):
            self.speedy = -1
            self.speedx = random.choice([-1,0,1])
        if(a==2):
            self.speedy = -1
            self.speedx = 0 + (((ppadle.x - self.x)//3)-ppadle.scale+1)
    
    def collision_check(self,archit,archit_power,powers,sscore,llives,ppadle,cclock):
        # wall check
        # if(self.x == 5 and self.speedx < 0):
        #     self.speedx =  -1 * self.speedx 
        # if(self.x == 77 and self.speedx > 0):
        #     self.speedx =  -1 * self.speedx 
        # if(self.y == 8 and self.speedy < 0):
        #     self.speedy =  -1 * self.speedy 
        # if(self.y == 28 and self.speedy > 0):
        #     llives.sub_life()
        #     self.start_throw(ppadle)
            
        if(self.speedx < 0 and (self.x + self.speedx < 4)):
            self.speedx =  -1 * self.speedx 
            self.x = self.speedx - self.x + 8
        if(self.speedx > 0 and (self.x + self.speedx >= 77)):
            self.speedx =  -1 * self.speedx 
            self.x = self.speedx - self.x + 77 + 77
        if(self.y == 8 and self.speedy < 0):
            self.speedy =  -1 * self.speedy 
        if(self.y == 28 and self.speedy > 0):
            llives.sub_life()
            self.spread = False
            self.shrink = False
            self.thruball = False
            self.fastball = False
            self.sticky = False
            self.mutliball = False
            ppadle.sticky = True
            self.start_throw(ppadle)
            
            # self.speedy =  -1 * self.speedy      # Just to check
            # self.die = True
        # brick check
        
        
        if(self.speedy < 0):
            if(self.speedx > 0):
                t = self.x + self.speedx - 1
                if(t%5==3 ):
                    # check up and side
                    flup = False
                    flss = False
                    if((self.y <= self.ub and self.y >= self.lb) and ((t>=8 and t<73) and ( check_buddy(self.y-self.lb) and (archit[self.y-self.lb][(t-4)//5]!=0)))):
                        flss = True
                    if((self.y <=(1+self.ub) and self.y >=(1+self.lb)) and ((t>8 and t<=73) and ( check_buddy(self.y-1-self.lb) and (archit[self.y-(1+self.lb)][((t-4)//5)-1]!=0)))):
                        flup = True
            
                    if(flss==True and flup==True):
                        if(archit[self.y-self.lb][(t-4)//5] != 10):
                            if(archit[self.y-self.lb][(t-4)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-self.lb][(t-4)//5])
                                    archit[self.y-self.lb][(t-4)//5]=0
                                else:
                                    archit[self.y-self.lb][(t-4)//5]=archit[self.y-self.lb][(t-4)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-self.lb][(t-4)//5]==0 and archit_power[self.y-self.lb][(t-4)//5]!=0):
                                    powers.append(Power((t-4)//5,self.y-self.lb,archit_power[self.y-self.lb][(t-4)//5],cclock.return_val()))
                                
                        if(archit[self.y-(1+self.lb)][((t-4)//5)-1] != 10):
                            if(archit[self.y-(1+self.lb)][((t-4)//5)-1] == -1):
                                sscore.update_val( self.chickibum(self.y-(1+self.lb),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(1+self.lb)][((t-4)//5)-1] )
                                    archit[self.y-(1+self.lb)][((t-4)//5)-1] =0
                                else:
                                    archit[self.y-(1+self.lb)][((t-4)//5)-1] = archit[self.y-(1+self.lb)][((t-4)//5)-1]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(1+self.lb)][((t-4)//5)-1]==0 and archit_power[self.y-(1+self.lb)][((t-4)//5)-1]!=0):
                                    powers.append(Power(((t-4)//5)-1,self.y-(1+self.lb),archit_power[self.y-(1+self.lb)][((t-4)//5)-1],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                    elif(flss == True):
                        if(archit[self.y-self.lb][(t-4)//5]!=10):
                            if(archit[self.y-self.lb][(t-4)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-self.lb][((t-4)//5)] )
                                    archit[self.y-self.lb][((t-4)//5)] =0
                                else:
                                    archit[self.y-self.lb][(t-4)//5]=archit[self.y-self.lb][(t-4)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-self.lb][(t-4)//5]==0 and archit_power[self.y-self.lb][(t-4)//5]!=0):
                                    powers.append(Power((t-4)//5,self.y-self.lb,archit_power[self.y-self.lb][(t-4)//5],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx = -1 * self.speedx
                    
                    elif(flup == True):
                        if(archit[self.y-(1+self.lb)][((t-4)//5)-1] != 10):
                            if(archit[self.y-(1+self.lb)][((t-4)//5)-1] == -1):
                                sscore.update_val( self.chickibum(self.y-(1+self.lb),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(1+self.lb)][((t-4)//5)-1] )
                                    archit[self.y-(1+self.lb)][((t-4)//5)-1] =0
                                else:
                                    archit[self.y-(1+self.lb)][((t-4)//5)-1] = archit[self.y-(1+self.lb)][((t-4)//5)-1]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(1+self.lb)][((t-4)//5)-1]==0 and archit_power[self.y-(1+self.lb)][((t-4)//5)-1]!=0):
                                    powers.append(Power(((t-4)//5)-1,self.y-(1+self.lb),archit_power[self.y-(1+self.lb)][((t-4)//5)-1],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedy = -1 * self.speedy
                    
                    else : 
                        if( (((((t-4)//5)+1)<= 12) and ((((t-4)//5)+1) >= 0)) and  (check_buddy(self.y-(1+self.lb)) and  (archit[self.y-(1+self.lb)][((t-4)//5)]!=0)) ):
                            if(archit[self.y-(1+self.lb)][((t-4)//5)]!=10):
                                if(archit[self.y-(1+self.lb)][(t-4)//5] == -1):
                                    sscore.update_val( self.chickibum(self.y-(1+self.lb),archit))
                                else:
                                    if(self.thruball==True):
                                        sscore.update_val(archit[self.y-(1+self.lb)][((t-4)//5)] )
                                        archit[self.y-(1+self.lb)][((t-4)//5)] =0
                                    else:
                                        archit[self.y-(1+self.lb)][((t-4)//5)] = archit[self.y-(1+self.lb)][((t-4)//5)] -1
                                        sscore.update_val(1)
                                    if(archit[self.y-(1+self.lb)][(t-4)//5]==0 and archit_power[self.y-(1+self.lb)][(t-4)//5]!=0):
                                        powers.append(Power((t-4)//5,self.y-(1+self.lb),archit_power[self.y-(1+self.lb)][(t-4)//5],cclock.return_val()))
                            if(self.thruball == False):
                                self.speedx = -1 * self.speedx
                                self.speedy = -1 * self.speedy
                else:
                    if((self.y <=(1+self.ub) and self.y >= (1+self.lb)) and ((t>8 and t<73) and (archit[self.y-(1+self.lb)][(t-9)//5]!=0))):
                        if(archit[self.y-(1+self.lb)][(t-9)//5]!=10):
                            if(archit[self.y-(1+self.lb)][(t-4)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-(1+self.lb),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(1+self.lb)][((t-9)//5)] )
                                    archit[self.y-(1+self.lb)][((t-9)//5)] =0
                                else:
                                    archit[self.y-(1+self.lb)][(t-9)//5] = archit[self.y-(1+self.lb)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(1+self.lb)][(t-9)//5]==0 and archit_power[self.y-(1+self.lb)][(t-9)//5]!=0):
                                    powers.append(Power((t-9)//5,self.y-(1+self.lb),archit_power[self.y-(1+self.lb)][(t-9)//5],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedy = -1 * self.speedy

            elif(self.speedx < 0 ):
                t = self.x + self.speedx + 1 
                if(t%5==4 and t>9):
                    fldw = False
                    flss = False
                    if((self.y <= self.ub and self.y >= self.lb) and ((t>9 and t<=74) and ( check_buddy(self.y-self.lb) and (archit[self.y-self.lb][((t-14)//5)]!=0)))):
                        flss = True
                    if((self.y <=(1+self.ub) and self.y >= (1+self.lb)) and ((t>= 9 and t<=69) and ( check_buddy(self.y-(1+self.lb)) and (archit[self.y-(1+self.lb)][(t-9)//5]!=0)))):
                        fldw = True
                    
                    if(flss==True and fldw==True):
                        if(archit[self.y-self.lb][((t-14)//5)]!=10):
                            if(archit[self.y-self.lb][((t-14)//5)] == -1):
                                sscore.update_val( self.chickibum(self.y-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-self.lb][((t-14)//5)] )
                                    archit[self.y-self.lb][((t-14)//5)] =0
                                else:
                                    archit[self.y-self.lb][((t-14)//5)]=archit[self.y-self.lb][((t-14)//5)]-1
                                    sscore.update_val(1)
                                if(archit[self.y-self.lb][(t-4)//5]==0 and archit_power[self.y-self.lb][(t-4)//5]!=0):
                                    powers.append(Power((t-4)//5,self.y-self.lb,archit_power[self.y-self.lb][(t-4)//5],cclock.return_val()))
                        
                        if(archit[self.y-(1+self.lb)][(t-9)//5]!=10):
                            if(archit[self.y-(1+self.lb)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-(1+self.lb),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(1+self.lb)][((t-9)//5)-1] )
                                    archit[self.y-(1+self.lb)][((t-9)//5)-1] =0
                                else:
                                    archit[self.y-(1+self.lb)][(t-9)//5] = archit[self.y-(1+self.lb)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(1+self.lb)][(t-9)//5]==0 and archit_power[self.y-(1+self.lb)][(t-9)//5]!=0):
                                    powers.append(Power((t-9)//5,self.y-(1+self.lb),archit_power[self.y-(1+self.lb)][(t-9)//5],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                            
                    elif(flss == True):
                        if(archit[self.y-self.lb][((t-14)//5)]!=10):
                            if(archit[self.y-self.lb][((t-14)//5)] == -1):
                                sscore.update_val( self.chickibum(self.y-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-self.lb][((t-14)//5)] )
                                    archit[self.y-self.lb][((t-14)//5)] =0
                                else:
                                    archit[self.y-self.lb][((t-14)//5)]=archit[self.y-self.lb][((t-14)//5)]-1
                                    sscore.update_val(1)
                                if(archit[self.y-self.lb][((t-14)//5)]==0 and archit_power[self.y-self.lb][((t-14)//5)]!=0):
                                    powers.append(Power(((t-14)//5),self.y-self.lb,archit_power[self.y-self.lb][((t-14)//5)],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx = -1 * self.speedx
                    elif(fldw == True):
                        if(archit[self.y-(1+self.lb)][(t-9)//5] != 10):
                            if(archit[self.y-(1+self.lb)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-(1+self.lb),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(1+self.lb)][((t-9)//5)] )
                                    archit[self.y-(1+self.lb)][((t-9)//5)] =0
                                else:
                                    archit[self.y-(1+self.lb)][(t-9)//5] = archit[self.y-(1+self.lb)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(1+self.lb)][((t-9)//5)]==0 and archit_power[self.y-(1+self.lb)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y-(1+self.lb),archit_power[self.y-(1+self.lb)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedy = -1 * self.speedy
                    else:
                        if(( ((((t-4)//5)-1)>=0) and ((((t-4)//5)-1)<=12) ) and ( check_buddy(self.y-(1+self.lb)) and (archit[self.y-(1+self.lb)][((t-4)//5)-1]!=0)) ):
                            if(archit[self.y-(1+self.lb)][((t-4)//5)-1]!=10):
                                if(archit[self.y-(1+self.lb)][((t-4)//5)-1] == -1):
                                    sscore.update_val( self.chickibum(self.y-(1+self.lb),archit))
                                else:
                                    if(self.thruball==True):
                                        sscore.update_val(archit[self.y-(1+self.lb)][((t-4)//5)-1] )
                                        archit[self.y-(1+self.lb)][((t-4)//5)-1] =0
                                    else:
                                        archit[self.y-(1+self.lb)][((t-4)//5)-1] = archit[self.y-(1+self.lb)][((t-4)//5)-1] -1
                                        sscore.update_val(1)
                                    if(archit[self.y-(1+self.lb)][((t-4)//5)-1]==0 and archit_power[self.y-(1+self.lb)][((t-4)//5)-1]!=0):
                                        powers.append(Power(((t-4)//5)-1,self.y-(1+self.lb),archit_power[self.y-(1+self.lb)][((t-14)//5)-1],cclock.return_val()))
                            if(self.thruball == False):
                                self.speedx = -1 * self.speedx
                                self.speedy = -1 * self.speedy
                else:
                    if( (self.y>=(1+self.lb) and self.y<=(1+self.ub)) and ( (t>8 and t<73) and ( check_buddy(self.y-(1+self.lb)) and (archit[self.y-(1+self.lb)][(t-9)//5]!=0)))):
                        if(archit[self.y-(1+self.lb)][(t-9)//5]!=10):
                            if(archit[self.y-(1+self.lb)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-(1+self.lb),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(1+self.lb)][((t-9)//5)] )
                                    archit[self.y-(1+self.lb)][((t-9)//5)] =0
                                else:
                                    archit[self.y-(1+self.lb)][(t-9)//5] = archit[self.y-(1+self.lb)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(1+self.lb)][((t-9)//5)]==0 and archit_power[self.y-(1+self.lb)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y-(1+self.lb),archit_power[self.y-(1+self.lb)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedy = -1 * self.speedy
            else:
                t = self.x
                if((self.y>=(1+self.lb) and self.y<=(1+self.ub)) and ( check_buddy(self.y-(1+self.lb)) and  (archit[self.y-(1+self.lb)][(t-9)//5]!=0))):
                    if(archit[self.y-(1+self.lb)][(t-9)//5]!=10):
                        if(archit[self.y-(1+self.lb)][(t-9)//5] == -1):
                            sscore.update_val( self.chickibum(self.y-(1+self.lb),archit))
                        else:
                            if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(1+self.lb)][((t-9)//5)] )
                                    archit[self.y-(1+self.lb)][((t-9)//5)] =0
                            else:
                                archit[self.y-(1+self.lb)][(t-9)//5] = archit[self.y-(1+self.lb)][(t-9)//5]-1
                                sscore.update_val(1)
                            if(archit[self.y-(1+self.lb)][((t-9)//5)]==0 and archit_power[self.y-(1+self.lb)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y-(1+self.lb),archit_power[self.y-(1+self.lb)][((t-9)//5)],cclock.return_val()))
                    if(self.thruball == False):
                        self.speedy = -1 * self.speedy


        elif(self.speedy > 0):
            if(self.speedx > 0):
                t = self.x + self.speedx - 1
                if(t%5==3 ):
                    # check up and side
                    flup = False
                    flss = False
                    if((self.y <= self.ub and self.y >= self.lb) and ((t>=8 and t<73) and ( check_buddy(self.y-self.lb) and archit[self.y-self.lb][(t-4)//5]!=0))):
                        flss = True
                    if((self.y <=(self.ub-1) and self.y >= (self.lb-1)) and ((t>8 and t<=73) and ( check_buddy((self.y-(self.lb-1))) and archit[self.y-(self.lb-1)][((t-4)//5)-1]!=0))):
                        flup = True
                    print(flss, flup)
                    if(flss==True and flup==True):
                        if(archit[self.y-self.lb][(t-4)//5]!=10):
                            if(archit[self.y-self.lb][(t-4)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-self.lb][((t-4)//5)] )
                                    archit[self.y-self.lb][((t-4)//5)] =0
                                else:
                                    archit[self.y-self.lb][(t-4)//5]=archit[self.y-self.lb][(t-4)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-self.lb][((t-4)//5)]==0 and archit_power[self.y-self.lb][((t-4)//5)]!=0):
                                    powers.append(Power(((t-4)//5),self.y-self.lb,archit_power[self.y-self.lb][((t-4)//5)],cclock.return_val()))
                        if(archit[self.y-(self.lb-1)][((t-4)//5)-1]!=10):
                            if(archit[self.y-(self.lb-1)][((t-4)//5)-1] == -1):
                                sscore.update_val( self.chickibum(self.y-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(self.lb-1)][((t-4)//5)-1] )
                                    archit[self.y-(self.lb-1)][((t-4)//5)-1] =0
                                else:
                                    archit[self.y-(self.lb-1)][((t-4)//5)-1] = archit[self.y-(self.lb-1)][((t-4)//5)-1]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(self.lb-1)][((t-4)//5)-1]==0 and archit_power[self.y-(self.lb-1)][((t-4)//5)-1]!=0):
                                    powers.append(Power(((t-4)//5)-1,self.y-(self.lb-1),archit_power[self.y-(self.lb-1)][((t-4)//5)-1],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                    elif(flss == True):
                        if(archit[self.y-self.lb][(t-4)//5]!=10):
                            if(archit[self.y-self.lb][(t-4)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-self.lb][((t-4)//5)] )
                                    archit[self.y-self.lb][((t-4)//5)] =0
                                else:
                                    archit[self.y-self.lb][(t-4)//5]=archit[self.y-self.lb][(t-4)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-self.lb][((t-4)//5)]==0 and archit_power[self.y-self.lb][((t-4)//5)]!=0):
                                    powers.append(Power(((t-4)//5),self.y-self.lb,archit_power[self.y-self.lb][((t-4)//5)],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx = -1 * self.speedx
                    elif(flup == True):
                        if(archit[self.y-(self.lb-1)][((t-4)//5)-1]!=10):
                            if(archit[self.y-(self.lb-1)][((t-4)//5)-1] == -1):
                                sscore.update_val( self.chickibum(self.y-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(self.lb-1)][((t-4)//5)-1] )
                                    archit[self.y-(self.lb-1)][((t-4)//5)-1] =0
                                else:
                                    archit[self.y-(self.lb-1)][((t-4)//5)-1] = archit[self.y-(self.lb-1)][((t-4)//5)-1]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(self.lb-1)][((t-4)//5)-1]==0 and archit_power[self.y-(self.lb-1)][((t-4)//5)-1]!=0):
                                    powers.append(Power(((t-4)//5)-1,self.y-(self.lb-1),archit_power[self.y-(self.lb-1)][((t-4)//5)-1],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedy = -1 * self.speedy
                    else : 
                        if( (((((t-4)//5)+1)<= 12) and ((((t-4)//5)+1) >= 0)) and  (check_buddy(self.y-(self.lb-1)) and  archit[self.y-(self.lb-1)][((t-4)//5)]!=0) ):
                            if(archit[self.y-(self.lb-1)][((t-4)//5)]!=10):
                                if(archit[self.y-(self.lb-1)][((t-4)//5)] == -1):
                                    sscore.update_val( self.chickibum(self.y-(self.lb-1),archit))
                                else:
                                    if(self.thruball==True):
                                        sscore.update_val(archit[self.y-(self.lb-1)][((t-4)//5)] )
                                        archit[self.y-(self.lb-1)][((t-4)//5)] =0
                                    else:
                                        archit[self.y-(self.lb-1)][((t-4)//5)] = archit[self.y-(self.lb-1)][((t-4)//5)] -1
                                        sscore.update_val(1)
                                    if(archit[self.y-(self.lb-1)][((t-4)//5)]==0 and archit_power[self.y-(self.lb-1)][((t-4)//5)]!=0):
                                        powers.append(Power(((t-4)//5),self.y-(self.lb-1),archit_power[self.y-(self.lb-1)][((t-4)//5)],cclock.return_val()))
                            if(self.thruball==False):
                                self.speedx = -1 * self.speedx
                                self.speedy = -1 * self.speedy
                else:
                    if((self.y <= (self.ub-1) and self.y >=(self.lb-1)) and ((t>8 and t<73) and ( check_buddy(self.y-(self.lb-1)) and archit[self.y-(self.lb-1)][(t-9)//5]!=0))):
                        if(archit[self.y-(self.lb-1)][(t-9)//5]!=10):
                            if(archit[self.y-(self.lb-1)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(self.lb-1)][((t-9)//5)] )
                                    archit[self.y-(self.lb-1)][((t-9)//5)] =0
                                else:
                                    archit[self.y-(self.lb-1)][(t-9)//5] = archit[self.y-(self.lb-1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(self.lb-1)][((t-9)//5)]==0 and archit_power[self.y-(self.lb-1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y-(self.lb-1),archit_power[self.y-(self.lb-1)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball==False):
                            self.speedy = -1 * self.speedy
            
            elif(self.speedx < 0 ):
                t = self.x + self.speedx + 1
                if(t%5==4 and t>9):
                    fldw = False
                    flss = False
                    if((self.y <=self.ub and self.y >= self.lb) and ((t>9 and t<=74) and ( check_buddy(self.y-self.lb) and archit[self.y-self.lb][((t-14)//5)]!=0))):
                        flss = True
                    if((self.y <=(self.ub-1) and self.y >= (self.lb-1)) and ((t>= 9 and t<=69) and ( check_buddy(self.y-(self.lb-1)) and archit[self.y-(self.lb-1)][(t-9)//5]!=0))):
                        fldw = True
                    
                    if(flss==True and fldw==True):
                        if(archit[self.y-self.lb][((t-14)//5)]!=10):
                            if(archit[self.y-self.lb][((t-14)//5)] == -1):
                                sscore.update_val( self.chickibum(self.y-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-self.lb][((t-14)//5)] )
                                    archit[self.y-self.lb][((t-14)//5)] =0
                                else:
                                    archit[self.y-self.lb][((t-14)//5)]=archit[self.y-self.lb][((t-14)//5)]-1
                                    sscore.update_val(1)
                                if(archit[self.y-self.lb][((t-14)//5)]==0 and archit_power[self.y-self.lb][((t-14)//5)]!=0):
                                    powers.append(Power(((t-14)//5),self.y-self.lb,archit_power[self.y-self.lb][((t-14)//5)],cclock.return_val()))
                        if(archit[self.y-(self.lb-1)][(t-9)//5]!=10):
                            if(archit[self.y-(self.lb-1)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(self.lb-1)][((t-9)//5)] )
                                    archit[self.y-(self.lb-1)][((t-9)//5)] =0
                                else:
                                    archit[self.y-(self.lb-1)][(t-9)//5] = archit[self.y-(self.lb-1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(self.lb-1)][((t-9)//5)]==0 and archit_power[self.y-(self.lb-1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y-(self.lb-1),archit_power[self.y-(self.lb-1)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball==False):
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                    elif(flss == True):
                        if(archit[self.y-self.lb][((t-14)//5)]!=10):
                            if(archit[self.y-self.lb][((t-14)//5)] == -1):
                                sscore.update_val( self.chickibum(self.y-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-self.lb][((t-14)//5)] )
                                    archit[self.y-self.lb][((t-14)//5)] =0
                                else:
                                    archit[self.y-self.lb][((t-14)//5)]=archit[self.y-self.lb][((t-14)//5)]-1
                                    sscore.update_val(1)
                                if(archit[self.y-self.lb][((t-14)//5)]==0 and archit_power[self.y-self.lb][((t-14)//5)]!=0):
                                    powers.append(Power(((t-14)//5),self.y-self.lb,archit_power[self.y-self.lb][((t-14)//5)],cclock.return_val()))
                        if(self.thruball==False):
                            self.speedx = -1 * self.speedx
                    elif(fldw == True):
                        if(archit[self.y-(self.lb-1)][(t-9)//5]!=10):
                            if(archit[self.y-(self.lb-1)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(self.lb-1)][((t-9)//5)] )
                                    archit[self.y-(self.lb-1)][((t-9)//5)] =0
                                else:
                                    archit[self.y-(self.lb-1)][(t-9)//5] = archit[self.y-(self.lb-1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(self.lb-1)][((t-9)//5)]==0 and archit_power[self.y-(self.lb-1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y-(self.lb-1),archit_power[self.y-(self.lb-1)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball==False):
                            self.speedy = -1 * self.speedy
                    else:
                        if(( ((((t-4)//5)-1)>=0) and ((((t-4)//5)-1)<=12) ) and ( check_buddy(self.y-(self.lb-1)) and archit[self.y-(self.lb-1)][((t-4)//5)-1]!=0) ):
                            if(archit[self.y-(self.lb-1)][((t-4)//5)-1] !=10):
                                if(archit[self.y-(self.lb-1)][((t-4)//5)-1] == -1):
                                    sscore.update_val( self.chickibum(self.y-(self.lb-1),archit))
                                else:
                                    if(self.thruball==True):
                                        sscore.update_val(archit[self.y-(self.lb-1)][((t-4)//5)-1] )
                                        archit[self.y-(self.lb-1)][((t-4)//5)-1] =0
                                    else:
                                        archit[self.y-(self.lb-1)][((t-4)//5)-1] = archit[self.y-(self.lb-1)][((t-4)//5)-1] -1
                                        sscore.update_val(1)
                                    if(archit[self.y-(self.lb-1)][((t-4)//5)-1]==0 and archit_power[self.y-(self.lb-1)][((t-4)//5)-1]!=0):
                                        powers.append(Power(((t-4)//5)-1,self.y-(self.lb-1),archit_power[self.y-(self.lb-1)][((t-4)//5)-1],cclock.return_val()))
                            if(self.thruball==False):
                                self.speedx = -1 * self.speedx
                                self.speedy = -1 * self.speedy
                else:
                    if( (self.y>=(self.lb-1) and self.y<=(self.ub-1)) and ( (t>8 and t<73) and ( check_buddy(self.y-(self.lb-1)) and archit[self.y-(self.lb-1)][(t-9)//5]!=0))):
                        if(archit[self.y-(self.lb-1)][(t-9)//5]!=10):
                            if(archit[self.y-(self.lb-1)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y-(self.lb-1)][((t-9)//5)] )
                                    archit[self.y-(self.lb-1)][((t-9)//5)] =0
                                else:
                                    archit[self.y-(self.lb-1)][(t-9)//5] = archit[self.y-(self.lb-1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y-(self.lb-1)][((t-9)//5)]==0 and archit_power[self.y-(self.lb-1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y-(self.lb-1),archit_power[self.y-(self.lb-1)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball==False):
                            self.speedy = -1 * self.speedy
            else:
                t = self.x
                if((self.y>=(self.lb-1) and self.y<=(self.ub-1)) and ( check_buddy(self.y-(self.lb-1)) and  archit[self.y-(self.lb-1)][(t-9)//5]!=0)):
                    if(archit[self.y-(self.lb-1)][(t-9)//5]!=10):
                        if(archit[self.y-(self.lb-1)][(t-9)//5] == -1):
                            sscore.update_val( self.chickibum(self.y-(self.lb-1),archit))
                        else:
                            if(self.thruball==True):
                                sscore.update_val(archit[self.y-(self.lb-1)][((t-9)//5)] )
                                archit[self.y-(self.lb-1)][((t-9)//5)] =0
                            else:
                                archit[self.y-(self.lb-1)][(t-9)//5] = archit[self.y-(self.lb-1)][(t-9)//5]-1
                                sscore.update_val(1)
                            if(archit[self.y-(self.lb-1)][((t-9)//5)]==0 and archit_power[self.y-(1+self.lb)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y-(self.lb-1),archit_power[self.y-(self.lb-1)][((t-9)//5)],cclock.return_val()))
                    if(self.thruball==False):
                        self.speedy = -1 * self.speedy
        return True
    
    def collision_check2(self,archit,archit_power,powers,sscore,llives,ppadle,cclock):
        # wall check
        # if(self.x2 == 5 and self.speedx2 < 0):
        #     self.speedx2 =  -1 * self.speedx2 
        # if(self.x2 == 77 and self.speedx2 > 0):
        #     self.speedx2 =  -1 * self.speedx2 
        # if(self.y2 == 8 and self.speedy2 < 0):
        #     self.speedy2 =  -1 * self.speedy2 
        # if(self.y2 == 28 and self.speedy2 > 0):
        #     llives.sub_life()
        #     self.start_throw(ppadle)
            
        if(self.speedx2 < 0 and (self.x2 + self.speedx2 < 4)):
            self.speedx2 =  -1 * self.speedx2 
            self.x2 = self.speedx2 - self.x2 + 8
        if(self.speedx2 > 0 and (self.x2 + self.speedx2 >= 77)):
            self.speedx2 =  -1 * self.speedx2 
            self.x2 = self.speedx2 - self.x2 + 77 + 77
        if(self.y2 == 8 and self.speedy2 < 0):
            self.speedy2 =  -1 * self.speedy2 
        if(self.y2 == 28 and self.speedy2 > 0):
            llives.sub_life()
            self.spread = False
            self.shrink = False
            self.thruball = False
            self.fastball = False
            self.sticky = False
            self.mutliball = False
            self.start_throw(ppadle)
            
            # self.speedy2 =  -1 * self.speedy2      # Just to check
            # self.die = True
        # brick check
        
        
        if(self.speedy2 < 0):
            if(self.speedx2 > 0):
                t = self.x2 + self.speedx2 - 1
                if(t%5==3 ):
                    # check up and side
                    flup = False
                    flss = False
                    if((self.y2 <=self.ub and self.y2 >= self.lb) and ((t>=8 and t<73) and ( check_buddy(self.y2-self.lb) and (archit[self.y2-self.lb][(t-4)//5]!=0)))):
                        flss = True
                    if((self.y2 <=(1+self.ub) and self.y2 >= (1+self.lb)) and ((t>8 and t<=73) and ( check_buddy(self.y2-(self.lb+1)) and (archit[self.y2-(self.lb+1)][((t-4)//5)-1]!=0)))):
                        flup = True
            
                    if(flss==True and flup==True):
                        if(archit[self.y2-self.lb][(t-4)//5] != 10):
                            if(archit[self.y2-self.lb][(t-4)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-self.lb][(t-4)//5])
                                    archit[self.y2-self.lb][(t-4)//5]=0
                                else:
                                    archit[self.y2-self.lb][(t-4)//5]=archit[self.y2-self.lb][(t-4)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-self.lb][(t-4)//5]==0 and archit_power[self.y2-self.lb][(t-4)//5]!=0):
                                    powers.append(Power((t-4)//5,self.y2-self.lb,archit_power[self.y2-self.lb][(t-4)//5],cclock.return_val()))
                                
                        if(archit[self.y2-(self.lb+1)][((t-4)//5)-1] != 10):
                            if(archit[self.y2-(self.lb+1)][((t-4)//5)-1] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb+1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb+1)][((t-4)//5)-1] )
                                    archit[self.y2-(self.lb+1)][((t-4)//5)-1] =0
                                else:
                                    archit[self.y2-(self.lb+1)][((t-4)//5)-1] = archit[self.y2-(self.lb+1)][((t-4)//5)-1]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb+1)][((t-4)//5)-1]==0 and archit_power[self.y2-(self.lb+1)][((t-4)//5)-1]!=0):
                                    powers.append(Power(((t-4)//5)-1,self.y2-(self.lb+1),archit_power[self.y2-(self.lb+1)][((t-4)//5)-1],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx2 = -1 * self.speedx2
                            self.speedy2 = -1 * self.speedy2
                    elif(flss == True):
                        if(archit[self.y2-self.lb][(t-4)//5]!=10):
                            if(archit[self.y2-self.lb][(t-4)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-self.lb][((t-4)//5)] )
                                    archit[self.y2-self.lb][((t-4)//5)] =0
                                else:
                                    archit[self.y2-self.lb][(t-4)//5]=archit[self.y2-self.lb][(t-4)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-self.lb][(t-4)//5]==0 and archit_power[self.y2-self.lb][(t-4)//5]!=0):
                                    powers.append(Power((t-4)//5,self.y2-self.lb,archit_power[self.y2-self.lb][(t-4)//5],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx2 = -1 * self.speedx2
                    
                    elif(flup == True):
                        if(archit[self.y2-(self.lb+1)][((t-4)//5)-1] != 10):
                            if(archit[self.y2-(self.lb+1)][((t-4)//5)-1] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb+1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb+1)][((t-4)//5)-1] )
                                    archit[self.y2-(self.lb+1)][((t-4)//5)-1] =0
                                else:
                                    archit[self.y2-(self.lb+1)][((t-4)//5)-1] = archit[self.y2-(self.lb+1)][((t-4)//5)-1]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb+1)][((t-4)//5)-1]==0 and archit_power[self.y2-(self.lb+1)][((t-4)//5)-1]!=0):
                                    powers.append(Power(((t-4)//5)-1,self.y2-(self.lb+1),archit_power[self.y2-(self.lb+1)][((t-4)//5)-1],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedy2 = -1 * self.speedy2
                    
                    else : 
                        if( (((((t-4)//5)+1)<= 12) and ((((t-4)//5)+1) >= 0)) and  (check_buddy(self.y2-(self.lb+1)) and  (archit[self.y2-(self.lb+1)][((t-4)//5)]!=0)) ):
                            if(archit[self.y2-(self.lb+1)][((t-4)//5)]!=10):
                                if(archit[self.y2-(self.lb+1)][(t-4)//5] == -1):
                                    sscore.update_val( self.chickibum(self.y2-(self.lb+1),archit))
                                else:
                                    if(self.thruball==True):
                                        sscore.update_val(archit[self.y2-(self.lb+1)][((t-4)//5)] )
                                        archit[self.y2-(self.lb+1)][((t-4)//5)] =0
                                    else:
                                        archit[self.y2-(self.lb+1)][((t-4)//5)] = archit[self.y2-(self.lb+1)][((t-4)//5)] -1
                                        sscore.update_val(1)
                                    if(archit[self.y2-(self.lb+1)][(t-4)//5]==0 and archit_power[self.y2-(self.lb+1)][(t-4)//5]!=0):
                                        powers.append(Power((t-4)//5,self.y2-(self.lb+1),archit_power[self.y2-(self.lb+1)][(t-4)//5],cclock.return_val()))
                            if(self.thruball == False):
                                self.speedx2 = -1 * self.speedx2
                                self.speedy2 = -1 * self.speedy2
                else:
                    if((self.y2 <=(1+self.ub) and self.y2 >= (1+self.lb)) and ((t>8 and t<73) and (archit[self.y2-(self.lb+1)][(t-9)//5]!=0))):
                        if(archit[self.y2-(self.lb+1)][(t-9)//5]!=10):
                            if(archit[self.y2-(self.lb+1)][(t-4)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb+1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb+1)][((t-9)//5)] )
                                    archit[self.y2-(self.lb+1)][((t-9)//5)] =0
                                else:
                                    archit[self.y2-(self.lb+1)][(t-9)//5] = archit[self.y2-(self.lb+1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb+1)][(t-9)//5]==0 and archit_power[self.y2-(self.lb+1)][(t-9)//5]!=0):
                                    powers.append(Power((t-9)//5,self.y2-(self.lb+1),archit_power[self.y2-(self.lb+1)][(t-9)//5],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedy2 = -1 * self.speedy2

            elif(self.speedx2 < 0 ):
                t = self.x2 + self.speedx2 + 1 
                if(t%5==4 and t>9):
                    fldw = False
                    flss = False
                    if((self.y2 <=self.ub and self.y2 >= self.lb) and ((t>9 and t<=74) and ( check_buddy(self.y2-self.lb) and (archit[self.y2-self.lb][((t-14)//5)]!=0)))):
                        flss = True
                    if((self.y2 <=(1+self.ub) and self.y2 >= (1+self.lb)) and ((t>= 9 and t<=69) and ( check_buddy(self.y2-(self.lb+1)) and (archit[self.y2-(self.lb+1)][(t-9)//5]!=0)))):
                        fldw = True
                    
                    if(flss==True and fldw==True):
                        if(archit[self.y2-self.lb][((t-14)//5)]!=10):
                            if(archit[self.y2-self.lb][((t-14)//5)] == -1):
                                sscore.update_val( self.chickibum(self.y2-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-self.lb][((t-14)//5)] )
                                    archit[self.y2-self.lb][((t-14)//5)] =0
                                else:
                                    archit[self.y2-self.lb][((t-14)//5)]=archit[self.y2-self.lb][((t-14)//5)]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-self.lb][(t-4)//5]==0 and archit_power[self.y2-self.lb][(t-4)//5]!=0):
                                    powers.append(Power((t-4)//5,self.y2-self.lb,archit_power[self.y2-self.lb][(t-4)//5],cclock.return_val()))
                        
                        if(archit[self.y2-(self.lb+1)][(t-9)//5]!=10):
                            if(archit[self.y2-(self.lb+1)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb+1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb+1)][((t-9)//5)-1] )
                                    archit[self.y2-(self.lb+1)][((t-9)//5)-1] =0
                                else:
                                    archit[self.y2-(self.lb+1)][(t-9)//5] = archit[self.y2-(self.lb+1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb+1)][(t-9)//5]==0 and archit_power[self.y2-(self.lb+1)][(t-9)//5]!=0):
                                    powers.append(Power((t-9)//5,self.y2-(self.lb+1),archit_power[self.y2-(self.lb+1)][(t-9)//5],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx2 = -1 * self.speedx2
                            self.speedy2 = -1 * self.speedy2
                            
                    elif(flss == True):
                        if(archit[self.y2-self.lb][((t-14)//5)]!=10):
                            if(archit[self.y2-self.lb][((t-14)//5)] == -1):
                                sscore.update_val( self.chickibum(self.y2-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-self.lb][((t-14)//5)] )
                                    archit[self.y2-self.lb][((t-14)//5)] =0
                                else:
                                    archit[self.y2-self.lb][((t-14)//5)]=archit[self.y2-self.lb][((t-14)//5)]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-self.lb][((t-14)//5)]==0 and archit_power[self.y2-self.lb][((t-14)//5)]!=0):
                                    powers.append(Power(((t-14)//5),self.y2-self.lb,archit_power[self.y2-self.lb][((t-14)//5)],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx2 = -1 * self.speedx2
                    elif(fldw == True):
                        if(archit[self.y2-(self.lb+1)][(t-9)//5] != 10):
                            if(archit[self.y2-(self.lb+1)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb+1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb+1)][((t-9)//5)] )
                                    archit[self.y2-(self.lb+1)][((t-9)//5)] =0
                                else:
                                    archit[self.y2-(self.lb+1)][(t-9)//5] = archit[self.y2-(self.lb+1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb+1)][((t-9)//5)]==0 and archit_power[self.y2-(self.lb+1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y2-(self.lb+1),archit_power[self.y2-(self.lb+1)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedy2 = -1 * self.speedy2
                    else:
                        if(( ((((t-4)//5)-1)>=0) and ((((t-4)//5)-1)<=12) ) and ( check_buddy(self.y2-(self.lb+1)) and (archit[self.y2-(self.lb+1)][((t-4)//5)-1]!=0)) ):
                            if(archit[self.y2-(self.lb+1)][((t-4)//5)-1]!=10):
                                if(archit[self.y2-(self.lb+1)][((t-4)//5)-1] == -1):
                                    sscore.update_val( self.chickibum(self.y2-(self.lb+1),archit))
                                else:
                                    if(self.thruball==True):
                                        sscore.update_val(archit[self.y2-(self.lb+1)][((t-4)//5)-1] )
                                        archit[self.y2-(self.lb+1)][((t-4)//5)-1] =0
                                    else:
                                        archit[self.y2-(self.lb+1)][((t-4)//5)-1] = archit[self.y2-(self.lb+1)][((t-4)//5)-1] -1
                                        sscore.update_val(1)
                                    if(archit[self.y2-(self.lb+1)][((t-4)//5)-1]==0 and archit_power[self.y2-(self.lb+1)][((t-4)//5)-1]!=0):
                                        powers.append(Power(((t-4)//5)-1,self.y2-(self.lb+1),archit_power[self.y2-(self.lb+1)][((t-14)//5)-1],cclock.return_val()))
                            if(self.thruball == False):
                                self.speedx2 = -1 * self.speedx2
                                self.speedy2 = -1 * self.speedy2
                else:
                    if( (self.y2>=(1+self.lb) and self.y2<=(1+self.ub)) and ( (t>8 and t<73) and ( check_buddy(self.y2-(self.lb+1)) and (archit[self.y2-(self.lb+1)][(t-9)//5]!=0)))):
                        if(archit[self.y2-(self.lb+1)][(t-9)//5]!=10):
                            if(archit[self.y2-(self.lb+1)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb+1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb+1)][((t-9)//5)] )
                                    archit[self.y2-(self.lb+1)][((t-9)//5)] =0
                                else:
                                    archit[self.y2-(self.lb+1)][(t-9)//5] = archit[self.y2-(self.lb+1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb+1)][((t-9)//5)]==0 and archit_power[self.y2-(self.lb+1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y2-(self.lb+1),archit_power[self.y2-(self.lb+1)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedy2 = -1 * self.speedy2
            else:
                t = self.x2
                if((self.y2>=(1+self.lb) and self.y2<=(1+self.ub)) and ( check_buddy(self.y2-(self.lb+1)) and  (archit[self.y2-(self.lb+1)][(t-9)//5]!=0))):
                    if(archit[self.y2-(self.lb+1)][(t-9)//5]!=10):
                        if(archit[self.y2-(self.lb+1)][(t-9)//5] == -1):
                            sscore.update_val( self.chickibum(self.y2-(self.lb+1),archit))
                        else:
                            if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb+1)][((t-9)//5)] )
                                    archit[self.y2-(self.lb+1)][((t-9)//5)] =0
                            else:
                                archit[self.y2-(self.lb+1)][(t-9)//5] = archit[self.y2-(self.lb+1)][(t-9)//5]-1
                                sscore.update_val(1)
                            if(archit[self.y2-(self.lb+1)][((t-9)//5)]==0 and archit_power[self.y2-(self.lb+1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y2-(self.lb+1),archit_power[self.y2-(self.lb+1)][((t-9)//5)],cclock.return_val()))
                    if(self.thruball == False):
                        self.speedy2 = -1 * self.speedy2

        elif(self.speedy2 > 0):
            if(self.speedx2 > 0):
                t = self.x2 + self.speedx2 - 1
                if(t%5==3 ):
                    # check up and side
                    flup = False
                    flss = False
                    if((self.y2 <= self.ub and self.y2 >= self.lb) and ((t>=8 and t<73) and ( check_buddy(self.y2-self.lb) and archit[self.y2-self.lb][(t-4)//5]!=0))):
                        flss = True
                    if((self.y2 <=(self.ub-1) and self.y2 >= (self.lb-1)) and ((t>8 and t<=73) and ( check_buddy(self.y2-(self.lb-1)) and archit[self.y2-(self.lb-1)][((t-4)//5)-1]!=0))):
                        flup = True
                    print(flss, flup)
                    if(flss==True and flup==True):
                        if(archit[self.y2-self.lb][(t-4)//5]!=10):
                            if(archit[self.y2-self.lb][(t-4)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-self.lb][((t-4)//5)] )
                                    archit[self.y2-self.lb][((t-4)//5)] =0
                                else:
                                    archit[self.y2-self.lb][(t-4)//5]=archit[self.y2-self.lb][(t-4)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-self.lb][((t-4)//5)]==0 and archit_power[self.y2-self.lb][((t-4)//5)]!=0):
                                    powers.append(Power(((t-4)//5),self.y2-self.lb,archit_power[self.y2-self.lb][((t-4)//5)],cclock.return_val()))
                        if(archit[self.y2-(self.lb-1)][((t-4)//5)-1]!=10):
                            if(archit[self.y2-(self.lb-1)][((t-4)//5)-1] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb-1)][((t-4)//5)-1] )
                                    archit[self.y2-(self.lb-1)][((t-4)//5)-1] =0
                                else:
                                    archit[self.y2-(self.lb-1)][((t-4)//5)-1] = archit[self.y2-(self.lb-1)][((t-4)//5)-1]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb-1)][((t-4)//5)-1]==0 and archit_power[self.y2-(self.lb-1)][((t-4)//5)-1]!=0):
                                    powers.append(Power(((t-4)//5)-1,self.y2-(self.lb-1),archit_power[self.y2-(self.lb-1)][((t-4)//5)-1],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx2 = -1 * self.speedx2
                            self.speedy2 = -1 * self.speedy2
                    elif(flss == True):
                        if(archit[self.y2-self.lb][(t-4)//5]!=10):
                            if(archit[self.y2-self.lb][(t-4)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-self.lb][((t-4)//5)] )
                                    archit[self.y2-self.lb][((t-4)//5)] =0
                                else:
                                    archit[self.y2-self.lb][(t-4)//5]=archit[self.y2-self.lb][(t-4)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-self.lb][((t-4)//5)]==0 and archit_power[self.y2-self.lb][((t-4)//5)]!=0):
                                    powers.append(Power(((t-4)//5),self.y2-self.lb,archit_power[self.y2-self.lb][((t-4)//5)],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedx2 = -1 * self.speedx2
                    elif(flup == True):
                        if(archit[self.y2-(self.lb-1)][((t-4)//5)-1]!=10):
                            if(archit[self.y2-(self.lb-1)][((t-4)//5)-1] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb-1)][((t-4)//5)-1] )
                                    archit[self.y2-(self.lb-1)][((t-4)//5)-1] =0
                                else:
                                    archit[self.y2-(self.lb-1)][((t-4)//5)-1] = archit[self.y2-(self.lb-1)][((t-4)//5)-1]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb-1)][((t-4)//5)-1]==0 and archit_power[self.y2-(self.lb-1)][((t-4)//5)-1]!=0):
                                    powers.append(Power(((t-4)//5)-1,self.y2-(self.lb-1),archit_power[self.y2-(self.lb-1)][((t-4)//5)-1],cclock.return_val()))
                        if(self.thruball == False):
                            self.speedy2 = -1 * self.speedy2
                    else : 
                        if( (((((t-4)//5)+1)<= 12) and ((((t-4)//5)+1) >= 0)) and  (check_buddy(self.y2-(self.lb-1)) and  archit[self.y2-(self.lb-1)][((t-4)//5)]!=0) ):
                            if(archit[self.y2-(self.lb-1)][((t-4)//5)]!=10):
                                if(archit[self.y2-(self.lb-1)][((t-4)//5)] == -1):
                                    sscore.update_val( self.chickibum(self.y2-(self.lb-1),archit))
                                else:
                                    if(self.thruball==True):
                                        sscore.update_val(archit[self.y2-(self.lb-1)][((t-4)//5)] )
                                        archit[self.y2-(self.lb-1)][((t-4)//5)] =0
                                    else:
                                        archit[self.y2-(self.lb-1)][((t-4)//5)] = archit[self.y2-(self.lb-1)][((t-4)//5)] -1
                                        sscore.update_val(1)
                                    if(archit[self.y2-(self.lb-1)][((t-4)//5)]==0 and archit_power[self.y2-(self.lb-1)][((t-4)//5)]!=0):
                                        powers.append(Power(((t-4)//5),self.y2-(self.lb-1),archit_power[self.y2-(self.lb-1)][((t-4)//5)],cclock.return_val()))
                            if(self.thruball==False):
                                self.speedx2 = -1 * self.speedx2
                                self.speedy2 = -1 * self.speedy2
                else:
                    if((self.y2 <=(self.ub-1) and self.y2 >=(self.lb-1)) and ((t>8 and t<73) and ( check_buddy(self.y2-(self.lb-1)) and archit[self.y2-(self.lb-1)][(t-9)//5]!=0))):
                        if(archit[self.y2-(self.lb-1)][(t-9)//5]!=10):
                            if(archit[self.y2-(self.lb-1)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb-1)][((t-9)//5)] )
                                    archit[self.y2-(self.lb-1)][((t-9)//5)] =0
                                else:
                                    archit[self.y2-(self.lb-1)][(t-9)//5] = archit[self.y2-(self.lb-1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb-1)][((t-9)//5)]==0 and archit_power[self.y2-(self.lb-1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y2-(self.lb-1),archit_power[self.y2-(self.lb-1)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball==False):
                            self.speedy2 = -1 * self.speedy2
            
            elif(self.speedx2 < 0 ):
                t = self.x2 + self.speedx2 + 1
                if(t%5==4 and t>9):
                    fldw = False
                    flss = False
                    if((self.y2 <=self.ub and self.y2 >= self.lb) and ((t>9 and t<=74) and ( check_buddy(self.y2-self.lb) and archit[self.y2-self.lb][((t-14)//5)]!=0))):
                        flss = True
                    if((self.y2 <=(self.ub-1) and self.y2 >= (self.lb-1)) and ((t>= 9 and t<=69) and ( check_buddy(self.y2-(self.lb-1)) and archit[self.y2-(self.lb-1)][(t-9)//5]!=0))):
                        fldw = True
                    
                    if(flss==True and fldw==True):
                        if(archit[self.y2-self.lb][((t-14)//5)]!=10):
                            if(archit[self.y2-self.lb][((t-14)//5)] == -1):
                                sscore.update_val( self.chickibum(self.y2-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-self.lb][((t-14)//5)] )
                                    archit[self.y2-self.lb][((t-14)//5)] =0
                                else:
                                    archit[self.y2-self.lb][((t-14)//5)]=archit[self.y2-self.lb][((t-14)//5)]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-self.lb][((t-14)//5)]==0 and archit_power[self.y2-self.lb][((t-14)//5)]!=0):
                                    powers.append(Power(((t-14)//5),self.y2-self.lb,archit_power[self.y2-self.lb][((t-14)//5)],cclock.return_val()))
                        if(archit[self.y2-(self.lb-1)][(t-9)//5]!=10):
                            if(archit[self.y2-(self.lb-1)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb-1)][((t-9)//5)] )
                                    archit[self.y2-(self.lb-1)][((t-9)//5)] =0
                                else:
                                    archit[self.y2-(self.lb-1)][(t-9)//5] = archit[self.y2-(self.lb-1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb-1)][((t-9)//5)]==0 and archit_power[self.y2-(self.lb-1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y2-(self.lb-1),archit_power[self.y2-(self.lb-1)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball==False):
                            self.speedx2 = -1 * self.speedx2
                            self.speedy2 = -1 * self.speedy2
                    elif(flss == True):
                        if(archit[self.y2-self.lb][((t-14)//5)]!=10):
                            if(archit[self.y2-self.lb][((t-14)//5)] == -1):
                                sscore.update_val( self.chickibum(self.y2-self.lb,archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-self.lb][((t-14)//5)] )
                                    archit[self.y2-self.lb][((t-14)//5)] =0
                                else:
                                    archit[self.y2-self.lb][((t-14)//5)]=archit[self.y2-self.lb][((t-14)//5)]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-self.lb][((t-14)//5)]==0 and archit_power[self.y2-self.lb][((t-14)//5)]!=0):
                                    powers.append(Power(((t-14)//5),self.y2-self.lb,archit_power[self.y2-self.lb][((t-14)//5)],cclock.return_val()))
                        if(self.thruball==False):
                            self.speedx2 = -1 * self.speedx2
                    elif(fldw == True):
                        if(archit[self.y2-(self.lb-1)][(t-9)//5]!=10):
                            if(archit[self.y2-(self.lb-1)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb-1)][((t-9)//5)] )
                                    archit[self.y2-(self.lb-1)][((t-9)//5)] =0
                                else:
                                    archit[self.y2-(self.lb-1)][(t-9)//5] = archit[self.y2-(self.lb-1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb-1)][((t-9)//5)]==0 and archit_power[self.y2-(self.lb-1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y2-(self.lb-1),archit_power[self.y2-(self.lb-1)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball==False):
                            self.speedy2 = -1 * self.speedy2
                    else:
                        if(( ((((t-4)//5)-1)>=0) and ((((t-4)//5)-1)<=12) ) and ( check_buddy(self.y2-(self.lb-1)) and archit[self.y2-(self.lb-1)][((t-4)//5)-1]!=0) ):
                            if(archit[self.y2-(self.lb-1)][((t-4)//5)-1] !=10):
                                if(archit[self.y2-(self.lb-1)][((t-4)//5)-1] == -1):
                                    sscore.update_val( self.chickibum(self.y2-(self.lb-1),archit))
                                else:
                                    if(self.thruball==True):
                                        sscore.update_val(archit[self.y2-(self.lb-1)][((t-4)//5)-1] )
                                        archit[self.y2-(self.lb-1)][((t-4)//5)-1] =0
                                    else:
                                        archit[self.y2-(self.lb-1)][((t-4)//5)-1] = archit[self.y2-(self.lb-1)][((t-4)//5)-1] -1
                                        sscore.update_val(1)
                                    if(archit[self.y2-(self.lb-1)][((t-4)//5)-1]==0 and archit_power[self.y2-(self.lb-1)][((t-4)//5)-1]!=0):
                                        powers.append(Power(((t-4)//5)-1,self.y2-(self.lb-1),archit_power[self.y2-(self.lb-1)][((t-4)//5)-1],cclock.return_val()))
                            if(self.thruball==False):
                                self.speedx2 = -1 * self.speedx2
                                self.speedy2 = -1 * self.speedy2
                else:
                    if( (self.y2>=(self.lb-1) and self.y2<=(self.ub-1)) and ( (t>8 and t<73) and ( check_buddy(self.y2-(self.lb-1)) and archit[self.y2-(self.lb-1)][(t-9)//5]!=0))):
                        if(archit[self.y2-(self.lb-1)][(t-9)//5]!=10):
                            if(archit[self.y2-(self.lb-1)][(t-9)//5] == -1):
                                sscore.update_val( self.chickibum(self.y2-(self.lb-1),archit))
                            else:
                                if(self.thruball==True):
                                    sscore.update_val(archit[self.y2-(self.lb-1)][((t-9)//5)] )
                                    archit[self.y2-(self.lb-1)][((t-9)//5)] =0
                                else:
                                    archit[self.y2-(self.lb-1)][(t-9)//5] = archit[self.y2-(self.lb-1)][(t-9)//5]-1
                                    sscore.update_val(1)
                                if(archit[self.y2-(self.lb-1)][((t-9)//5)]==0 and archit_power[self.y2-(self.lb-1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y2-(self.lb-1),archit_power[self.y2-(self.lb-1)][((t-9)//5)],cclock.return_val()))
                        if(self.thruball==False):
                            self.speedy2 = -1 * self.speedy2
            else:
                t = self.x2
                if((self.y2>=(self.lb-1) and self.y2<=(self.ub-1)) and ( check_buddy(self.y2-(self.lb-1)) and  archit[self.y2-(self.lb-1)][(t-9)//5]!=0)):
                    if(archit[self.y2-(self.lb-1)][(t-9)//5]!=10):
                        if(archit[self.y2-(self.lb-1)][(t-9)//5] == -1):
                            sscore.update_val( self.chickibum(self.y2-(self.lb-1),archit))
                        else:
                            if(self.thruball==True):
                                sscore.update_val(archit[self.y2-(self.lb-1)][((t-9)//5)] )
                                archit[self.y2-(self.lb-1)][((t-9)//5)] =0
                            else:
                                archit[self.y2-(self.lb-1)][(t-9)//5] = archit[self.y2-(self.lb-1)][(t-9)//5]-1
                                sscore.update_val(1)
                            if(archit[self.y2-(self.lb-1)][((t-9)//5)]==0 and archit_power[self.y2-(self.lb+1)][((t-9)//5)]!=0):
                                    powers.append(Power(((t-9)//5),self.y2-(self.lb-1),archit_power[self.y2-(self.lb-1)][((t-9)//5)],cclock.return_val()))
                    if(self.thruball==False):
                        self.speedy2 = -1 * self.speedy2
        return True

    def collision_paddle(self,sscore,cclock,sscene,ppadle):
        # if ball stiky
        
        if(self.sticky==True):
            ppadle.sticky==True
            
        if(ppadle.sticky==True or self.sticky==True):
            msg2 =  "\n>> " + Fore.BLACK + Back.WHITE + " MESSAGE "  + RESET + " : Press \" \" space to launch"

            print(msg2)
            if((self.speedy > 0) and (self.y == 27) and ((self.x >= ppadle.x) and (self.x <= (ppadle.x + ppadle.length)))):
                self.speedy=0
                self.speedx=0
        else:
            if((self.speedy > 0) and (self.y == 27) and ((self.x >= ppadle.x) and (self.x <= (ppadle.x + ppadle.length)))):
                t1 = self.x - ppadle.x
                t1 = (t1*ppadle.scale) // ppadle.length
                t1 = t1 - 1
                self.speedx = self.speedx + t1
                if(self.speedx > 1 ):
                    self.speedx = 1
                elif(self.speedx < -1):
                    self.speedx = -1
                self.speedy = -1 * self.speedy
                if(sscene.skyfall==True):
                    sscene.falling_Sky(sscore.return_val(),cclock.return_val())
        return True
    
    def collision_paddle2(self,ppadle):
        # if ball stiky
        if(self.sticky==True):
            ppadle.sticky==True
            
        if(ppadle.sticky==True or self.sticky==True):
            msg2 = "\n>> " +  Fore.BLACK + Back.WHITE + " MESSAGE "  + RESET + " : Press \" \" space to launch"
            print(msg2)
            if((self.speedy2 > 0) and (self.y2 == 27) and ((self.x2 >= ppadle.x) and (self.x2 <= (ppadle.x + ppadle.length)))):
                self.speedy2=0
                self.speedx2=0
        else:
            if((self.speedy2 > 0) and (self.y2 == 27) and ((self.x2 >= ppadle.x) and (self.x2 <= (ppadle.x + ppadle.length)))):
                t1 = self.x2 - ppadle.x
                t1 = (t1*ppadle.scale) // ppadle.length
                t1 = t1 - 1
                self.speedx = self.speedx + t1
                if(self.speedx > 1 ):
                    self.speedx = 1
                elif(self.speedx < -1):
                    self.speedx = -1
                self.speedy2 = -1 * self.speedy2
                # print("OKOK")
        return True
    
    
    def reflect_vertical_wall(self):
        self.speedx = -1* self.speedx
        
    def reflect_top_wall(self):
        self.speedy = -1* self.speedy
        
    def reflect_corner_wall(self):
        self.speedx = -1* self.speedx
        self.speedy = -1* self.speedy
    
    def fall_off(self):
        # live gone restart
        pass
    
    def reflect_paddle(self,val):
        self.speedy = -1* self.speedy
        self.speedx = self.speedx + val
    
    def ball_move(self):
        self.x = self.x + self.speedx
        self.y = self.y + self.speedy
    
    def ball_move2(self):
        self.x2 = self.x2 + self.speedx2
        self.y2 = self.y2 + self.speedy2