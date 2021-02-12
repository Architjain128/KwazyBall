from config import SPEED

class Ball:
    def __init__(self):
        self.sticky = False
        self.fastball = False
        self.thruball = False
        self.multiball = False
        self.x = 0
        self.y = 0
        self.speedx = 0
        self.speedy = 0
    
    def start_throw(self):
        # random pos on paddle
        pass
    
    def collision_check(self,scene):
        pass
    
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
        