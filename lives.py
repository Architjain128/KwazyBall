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

class Time(ScoreBoard):
    def return_val(self):
        return math.floor(self.val)

class Score(ScoreBoard):
    def update_val(self):
        self.val = self.val + 10
        
class Level(ScoreBoard):
    def update_val(self):
        self.val = self.val + 1
        return self.val