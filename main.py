import os
import sys
import time
from config import *
from messages import *
from levelsetup import *
from getch import *
from background import *

landing_page = landing_page()

# generate scene

# generate paddle

# set lives/level/score

# special power

getinp = Get()
PAUSE = False
LIFE = str(5)
LEVEL = str((20%10)+1)
SCORE = str(100000)
hh = 108-len(LEVEL)-len(LIFE)-len(SCORE)-70-8-8-11
scene = Scene()

if(1 == landing_page):
    while True:
        input = input_to(getinp)
        if(input=='q' or input=="Q"):
            quitmsg()
            break
        
        if(input=='p' or input=="P"):
            PAUSE = True
            pausedmsg(SCORE)
        
        if(input=='r' or input=="R"):
            PAUSE=False
        
        if(PAUSE==False):
            os.system('clear')
            scene.generate_level(1)
    
else:
    quitmsg();
    # gameover(str(150));