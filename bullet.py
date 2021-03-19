from powerup import *

class Bullet:
    def __init__(self,id1,id2,x,y):
        self.id1 = id1
        self.id2 = id2
        self.x = x
        self.y = y
        self.speedx = 0
        self.speedy = 1
        self.vis = True
        
class Bullets:
    def __init__(self):
        self.bullet_array = []
        self.tok = 0
        self.index = 0
        
        
    def add_bullet(self,a,b,c):
        if(self.tok % 2 == 1):
            bb1 = Bullet(self.index,0,a,c)
            bb2 = Bullet(self.index+1,0,b,c)
            self.index = self.index +2
            self.bullet_array.append(bb1)
            self.bullet_array.append(bb2)
        self.tok +=1
    
    def print_bullets(self,arrr):
        for b in self.bullet_array:
            if(b.vis == True):
                arrr[b.y][b.x] = '^'
    
    def move_bullet(self):
        for b in self.bullet_array:
            b.y = b.y -1
    
    def visible_bullet(self,b,lb):
        if(b.y<=(lb-2)):
            b.vis = False
    
    def collison_bullet(self,sscene,lb,ub,ran_archit,sscore,cclock):
        for b in self.bullet_array:
            self.visible_bullet(b,lb)
            if(b.vis == True):
                if((b.y<=(1+ub) and b.y>lb ) and ((b.x-9)//5 >=0 and (b.x-9)//5<= 12) ):
                    if(sscene.matrix[b.y-1-lb][(b.x-9)//5]!=0):
                        if(sscene.matrix[b.y-1-lb][(b.x-9)//5]!=10 and sscene.matrix[b.y-1-lb][(b.x-9)//5]!=-1):
                            if(sscene.matrix[b.y-1-lb][(b.x-9)//5]!=7):
                                if(sscene.power_matrix[b.y-1-lb][(b.x-9)//5]!=0):
                                    sscene.powers.append(Power(0,(b.x-9)//5,b.y-1-lb,sscene.power_matrix[b.y-1-lb][(b.x-9)//5],cclock.return_val()))
                                sscene.matrix[b.y-1-lb][(b.x-9)//5] = sscene.matrix[b.y-1-lb][(b.x-9)//5] - 1
                                sscore.update_val(1)
                            elif(sscene.matrix[b.y-1-lb][(b.x-9)//5]==7)):
                                sscene.matrix[b.y-1-lb][(b.x-9)//5] = ran_archit
                        b.vis = False