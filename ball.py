from config import SPEED
import random

class Ball:
    def __init__(self,ppadle):
        self.die = False
        self.sticky = False
        self.fastball = False
        self.thruball = False
        self.multiball = False
        self.x = 0
        self.y = 0
        self.speedx = 1
        self.speedy = -1
        self.collison = False
        self.start_throw(ppadle)
    
    def start_throw(self,ppadle):
        # temp = random.randrange(1,ppadle.length)
        temp = 7
        self.x = ppadle.x + temp
        temp = temp // ppadle.scale
        self.speedx = self.speedx + temp - (ppadle.length//2)
        self.y = 27
        self.speedy = 1
        
    def launch_ball(self):
        pass
    
    def collision_check(self,archit):
        # wall check
        if(self.x == 5 and self.speedx < 0):
            self.speedx =  -1 * self.speedx 
        if(self.x == 77 and self.speedx > 0):
            self.speedx =  -1 * self.speedx 
        if(self.y == 8 and self.speedy < 0):
            self.speedy =  -1 * self.speedy 
        if(self.y == 28 and self.speedy > 0):
            self.speedy =  -1 * self.speedy      # Just to check
            # self.die = True
        # brick check
        # side collison
        
        
        
        if(self.y >= 10 and self.y <=15):
            if(self.speedx < 0 and archit[(self.x//6)-1][self.y-10]!=0):
                self.speedx = -1 * self.speedx
                archit[(self.x//6)-1][self.y-10] = archit[(self.x//6)-1][self.y-10] -1
            if(self.speedx > 0 and archit[(self.x //6)+1][self.y-10]!=0):
                self.speedx = -1 * self.speedx
                archit[(self.x//6)-1][self.y-10] = archit[(self.x//6)-1][self.y-10] -1
        
        if(self.speedy < 0):
            if((self.y >= 11) and (self.y<=16)):
                if((self.x - 5)%6==0):
                    if(self.x == 5):
                        if(self.speedx > 0 and archit[self.y-11][0]!=0):
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                            archit[self.y-11][0]=archit[self.y-11][0]-1
                        if(self.speedx < 0):
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                            archit[self.y-11][0]=archit[self.y-11][0]-1
                            
                    elif(self.x == 77 and archit[self.y-11][11]!=0):
                        if(self.speedx > 0):
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                            archit[self.y-11][11]=archit[self.y-11][11]-1
                        if(self.speedx < 0):
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                            archit[self.y-11][11]=archit[self.y-11][11]-1
                    else:
                        if(archit[self.y-11][(self.x//6)+1] !=0 and archit[self.y-11][(self.x//6)-1]!=0):
                            self.speedy = -1 * self.speedy
                            archit[self.y-11][(self.x//6)+1]=archit[self.y-11][(self.x//6)+1]-1
                            archit[self.y-11][(self.x//6)-1]=archit[self.y-11][(self.x//6)-1]-1
                        elif(archit[self.y-11][(self.x//6)-1]!=0):
                            archit[self.y-11][(self.x//6)-1]=archit[self.y-11][(self.x//6)-1]-1
                            self.speedy = -1 * self.speedy
                            if(self.speedx < 0):
                                self.speedx = -1 * self.speedx
                        elif(archit[self.y-11][(self.x//6)+1]!=0):
                            archit[self.y-11][(self.x//6)+1]=archit[self.y-11][(self.x//6)+1]-1
                            self.speedy = -1 * self.speedy
                            if(self.speedx > 0):
                                self.speedx = -1 * self.speedx
                else:
                    t = self.x
                    for i in range(0,8):
                        if(t%6==0):
                            break
                        t=t-1
                    t = t//6
                    t = t-1
                    if(archit[self.y-11][t]!=0):
                        self.speedy = -1 * self.speedy
                        archit[self.y-11][t]=archit[self.y-11][t]-1

        elif(self.speedy > 0):
            if(self.y+1 >= 10 and self.y+1 <=15):
                if((self.x - 5)%6==0):
                    if(self.x == 5):
                        if(self.speedx > 0 and archit[self.y-11][0]!=0):
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                            archit[self.y-11][0]=archit[self.y-11][0]-1
                        if(self.speedx < 0):
                            pass
                    elif(self.x == 77 and archit[self.y-11][11]!=0):
                        if(self.speedx > 0):
                            pass
                        if(self.speedx < 0):
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                            archit[self.y-11][11]=archit[self.y-11][11]-1
                    else:
                        if(archit[self.y-11][(self.x//6)+1] !=0 and archit[self.y-11][(self.x//6)-1]!=0):
                            self.speedy = -1 * self.speedy
                            archit[self.y-11][(self.x//6)+1]=archit[self.y-11][(self.x//6)+1]-1
                            archit[self.y-11][(self.x//6)-1]=archit[self.y-11][(self.x//6)-1]-1
                        elif(archit[self.y-11][(self.x//6)-1]!=0):
                            archit[self.y-11][(self.x//6)-1]=archit[self.y-11][(self.x//6)-1]-1
                            self.speedy = -1 * self.speedy
                            if(self.speedx < 0):
                                self.speedx = -1 * self.speedx
                        elif(archit[self.y-11][(self.x//6)+1]!=0):
                            archit[self.y-11][(self.x//6)+1]=archit[self.y-11][(self.x//6)+1]-1
                            self.speedy = -1 * self.speedy
                            if(self.speedx > 0):
                                self.speedx = -1 * self.speedx
                else:
                    t = self.x
                    for i in range(0,8):
                        if(t%6==0):
                            break
                        t=t-1
                    t = t//6
                    t = t-1
                    if(archit[self.y-11][t]!=0):
                        self.speedy = -1 * self.speedy
                        archit[self.y-11][t]=archit[self.y-11][t]-1
        return True

    def collision_paddle(self,ppadle):
        if((self.y == 27) and ((self.x >= ppadle.x) and (self.x <= (ppadle.x + ppadle.length)))):
            t1 = self.x - ppadle.x
            t1 = t1 // ppadle.scale
            t1 = t1 - (ppadle.length//2)
            # self.speedx = self.speedx + t1
            self.speedy = -1 * self.speedy
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