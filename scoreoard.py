import math
from sound import play_blast, play_brick, play_loss, play_other

class ScoreBoard : 
    def __init__(self,initialval):
        self.val = initialval
    def return_val(self):
        return self.val

class Lives(ScoreBoard):
    def sub_life(self):
        self.val = self.val - 1
        play_loss()
        return self.val
    def add_life(self):
        self.val = self.val + 1
        return self.val
    def add_in_scene(self,scene):
        temp = str(self.val)
        for i in range(0,len(temp)):
            scene.matrix[6][16+i]=temp[i]

class Time(ScoreBoard):
    def update_val(self,delta,scene):
        self.val = self.val + delta
    def return_val(self):
        return math.floor(self.val)
    def return_value(self):
        return self.val
    def add_in_scene(self,scene):
        temp = str(self.val)
        for i in range(0,len(temp)):
            scene.matrix[4][54+i]=temp[i]

class Score(ScoreBoard):
    def update_val(self,ss):
        self.val = self.val + ss*10
        play_brick()
        
    def set_val(self,ss):
        self.val  = ss
    
    def add_in_scene(self,scene):
        temp = str(self.val)
        for i in range(0,len(temp)):
            scene.matrix[6][84+i]=temp[i]

class Pause(ScoreBoard):
    def toggle_pause(self):
        if(self.val == True):
            self.val = False
        else : 
            self.val = True

class Level(ScoreBoard):
    def update_val(self,scene):
        self.val = self.val + 1

    def add_in_scene(self,scene):
        temp = str(self.val)
        for i in range(0,len(temp)):
            scene.matrix[6][55+i]=temp[i]
            
class Level_change_flag(ScoreBoard):
    def set_val(self,t):
        self.val = t