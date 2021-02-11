import math


class ScoreBoard : 
    def __init__(self,initialval):
        self.val = initialval
    def return_val(self):
        return self.val

class Lives(ScoreBoard):
    def sub_life(self):
        self.val = self.val - 1
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
        self.add_in_scene(scene)
    def return_val(self):
        return math.floor(self.val)
    def add_in_scene(self,scene):
        temp = str(self.val)
        for i in range(0,len(temp)):
            scene.matrix[4][54+i]=temp[i]

class Score(ScoreBoard):
    def update_val(self):
        self.val = self.val + 10
        self.add_in_scene(scene)
        
    def add_in_scene(self,scene):
        temp = str(self.val)
        for i in range(0,len(temp)):
            scene.matrix[6][84+i]=temp[i]
        
class Level(ScoreBoard):
    def update_val(self):
        self.val = self.val + 1
        # self.add_in_scene(scene)

    def add_in_scene(self,scene):
        temp = str(self.val)
        for i in range(0,len(temp)):
            scene.matrix[6][55+i]=temp[i]