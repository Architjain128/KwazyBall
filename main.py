import os
import sys
import time
from config import *
from messages import *
from levelsetup import *
from getch import *
from background import *
from paddle import *
from scoreoard import *


landing_page = landing_page()

getinp = Get()
scene = Scene()
paddle = Paddle()
clock = Time(0)
score = Score(0)
level = Level(1)
lives = Lives(5)
# ball
# bricks
# special power

PAUSE = False
scene.set_init_array(1)
paddle.addpaddle(55)

# lives.add_in_scene(scene)
# score.add_in_scene(scene)
# clock.add_in_scene(scene)
# level.add_in_scene(scene)
level_change_flag = False
if(1 == landing_page):
    while True:
        
        input = input_to(getinp,SPEED)
        
        if(input=='q' or input=="Q"):
            quitmsg()
            break
        
        if(input=='p' or input=="P"):
            PAUSE = True
            pausedmsg(score.return_val(),clock.return_val())
        
        if(input=='r' or input=="R"):
            PAUSE=False
            
        if(input=='a' or input=="A"):
            paddle.move_left()
        
        if(input=='d' or input=="D"):
            paddle.move_right()
            
        if(input=='z' or input=="Z"):
            level_change_flag = True
            
        if(PAUSE==False):
            # clock.update_val(SPEED,scene)
            os.system('clear')
            if(level_change_flag==True):
                level.update_val()
                scene.set_init_array(level.val)
                level_change_flag = False
                
            scene.generate_screen()
            

            

else:
    quitmsg();
    # gameover(str(150));