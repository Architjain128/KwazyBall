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
        temp = random.randrange(1,ppadle.length)
        self.x = ppadle.x + temp
        temp = temp // ppadle.scale
        self.speedx = self.speedx + temp - (ppadle.length//2)
        self.y = 27
        self.speedy = 1
        
    def launch_ball(self):
        pass
    
    def collision_check(self):
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
        return True
        
        
        # brick check
        
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