from config import *
import numpy as np

class Scene:
    
    def __init__(self, length, width):
        self.width = width
        self.length = length
        self.score = 0
        self.lives = 5
        self.level = 1
        self.time = 0
        self.matrix = []
        # self.walltop = 0
        # self.wallbottom = 0
        # self.wallleft = 0
        # self.wallright = 0
    
    def generate_level(self,level):
        
    # update time
    # update level
    # update life
    # update score