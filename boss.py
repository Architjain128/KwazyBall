from powerup import Power

class Boom:
    def __init__(self,idx,x,y):
        self.x = x
        self.idx = idx
        self.y = y
        self.vis = True

class Ufo:
    def __init__(self):
        self.x = 40
        self.y = 8
        self.tok = 0
        self.index = 0
        self.boom_array = []
        self.health = 30
        
    def move_ufo(self,x):
        self.x=x
    
    def add_boom(self):
        a = self.x
        c = self.y
        if(self.tok %4 ==1):
            bb = Boom(self.index,a,c)
            self.index +=1
            self.boom_array.append(bb)
        self.tok+=1
    
    def print_boom(self,arrr):
        for b in self.boom_array:
            if(b.vis == True):
                arrr[b.y][b.x] = '*'
                
    def print_ufo(self,arrr):
        arrr[self.y][self.x] = '#'
        arrr[self.y][self.x-1] = '('
        arrr[self.y][self.x+1] = ')'
        
    def move_boom(self):
        for b in self.boom_array:
            b.y = b.y +1
    
    def visible_boom(self):
        for b in self.boom_array:
            if(b.y>27):
                b.vis = False
            
    # collect boom
    def destroy_boom(self,ppadle,llives,sscene):
        for b in self.boom_array:
            if(b.y == 27):
                if(b.x >= ppadle.x and b.x <= ppadle.x + ppadle.length):
                    sscene.powers=[]
                    llives.sub_life()
                    
                    # life loss
                    
    def ufo_hit(self,bball,bbullets):
        for b in bbullets.bullet_array:
            if(b.y == 9):
                if(b.x >= (self.x-1) and b.x <= (self.x+1) ):
                    self.health -=1

        if(bball.y == 9):
            tt = bball.x
            if(bball.speedx > 0 ):
                tt+=1
            elif(bball.speedx < 0):
                tt-=1
            else:
                tt = tt
            if(tt >= (self.x-1) and tt >= (self.x+1) ):
                    self.health -=1
                    
    def win_check(self):
        if(self.health==0):
            return True
        return False