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
from ball import *

landing_page = landing_page()

getinp = Get()
scene = Scene(SPEED)
paddle = Paddle()
clock = Time(0)
score = Score(0)
level = Level(1)
lives = Lives(1) 
ball = Ball(paddle)
PAUSE = Pause(False)
scene.set_init_array(1)
ball.start_throw(paddle)
FLAG = Level_change_flag(False)

if(0 != landing_page):
    while True:
        
        input = input_to(getinp,scene.speed)
        
        if(input=='q' or input=="Q"):
            quitmsg()
            break
        
        if(input=='p' or input=="P" and PAUSE.return_val() == False):
            PAUSE.toggle_pause()
            pausedmsg(score.return_val(),clock.return_val())
        
        if(input=='r' or input=="R" and PAUSE.return_val() == True):
            PAUSE.toggle_pause()
            
        if(input=='a' or input=="A"):
            if(ball.get_fastball()==False):
                paddle.move_left(ball)
            else:
                if(clock.return_value()%(scene.get_speed())==0):
                    paddle.move_left(ball)
        
        if(input=='d' or input=="D"):
            if(ball.get_fastball()==False):
                    paddle.move_right(ball)
            else:
                if(clock.return_value()%(scene.get_speed())==0):
                    paddle.move_right(ball)
            
        if((input =='z' or (score.return_val()>=1130)) and level.return_val()==1):
            FLAG.set_val(True)
            
        if((input =='z' or score.return_val()>=2380 )and (level.return_val()==2)):
            gameover(score.return_val(),clock.return_val())
            break
            
        if(lives.return_val()==0):
            gameover(score.return_val(),clock.return_val())
            break
        
        if(input==' '):
            paddle.set_sticky(False)
            ball.launch_ball(landing_page,paddle)
        
        if(PAUSE.return_val()==False):
            clock.update_val(scene.speed,scene)
            if(FLAG.return_val()==True):
                level.update_val(scene)
                scene.set_init_array(level.return_val())
                ball.start_throw(paddle)
                FLAG.set_val(False)
            scene.generate_screen(clock,level,lives,score,paddle,ball)
    
else:
    quitmsg();
