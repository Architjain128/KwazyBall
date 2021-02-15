from config import SPEED
import random

def check_buddy(ok):
    if(ok>=0 and ok<=5):
        return True
    return False

class Ball:
    def __init__(self,ppadle):
        self.die = False
        self.sticky = False
        self.fastball = False
        self.thruball = False
        self.multiball = False
        self.x = 0
        self.y = 0
        self.speedx = -1
        self.speedy = -1
        self.collison = False
        self.start_throw(ppadle)
    
    
    
    def start_throw(self,ppadle):
        # temp = random.randrange(1,ppadle.length)
        temp = 7
        self.x = ppadle.x + temp
        temp = temp // ppadle.scale
        # self.speedx = self.speedx + temp - (ppadle.length//2)
        self.y = 27
        self.speedy = 1
        
    def launch_ball(self):
        pass
    
    def collision_check(self,archit,sscore,llives):
        # wall check
        print(self.speedx)
        if(self.x == 5 and self.speedx < 0):
            self.speedx =  -1 * self.speedx 
        if(self.x == 77 and self.speedx > 0):
            self.speedx =  -1 * self.speedx 
        if(self.y == 8 and self.speedy < 0):
            self.speedy =  -1 * self.speedy 
        if(self.y == 28 and self.speedy > 0):
            self.speedy =  -1 * self.speedy      # Just to check
            # self.die = True
        # brick check
        
        
        if(self.speedy < 0):
            if(self.speedx > 0):
                t = self.x
                if(t%5==3 ):
                    # check up and side
                    flup = False
                    flss = False
                    if((self.y <=15 and self.y >= 10) and ((t>=8 and t<73) and ( check_buddy(self.y-10) and archit[self.y-10][(t-4)//5]!=0))):
                        flss = True
                    if((self.y <=16 and self.y >= 11) and ((t>8 and t<=73) and ( check_buddy(self.y-11) and archit[self.y-11][((t-4)//5)-1]!=0))):
                        flup = True
                    print(flss, flup)
                    if(flss==True and flup==True):
                        archit[self.y-10][(t-4)//5]=archit[self.y-10][(t-4)//5]-1
                        archit[self.y-11][((t-4)//5)-1] = archit[self.y-11][((t-4)//5)-1]-1
                        sscore.update_val(2)
                        self.speedx = -1 * self.speedx
                        self.speedy = -1 * self.speedy
                    elif(flss == True):
                        archit[self.y-10][(t-4)//5]=archit[self.y-10][(t-4)//5]-1
                        sscore.update_val(1)
                        self.speedx = -1 * self.speedx
                    elif(flup == True):
                        archit[self.y-11][((t-4)//5)-1] = archit[self.y-11][((t-9)//5)-1]-1
                        sscore.update_val(1)
                        self.speedy = -1 * self.speedy
                    else : 
                        if( (((((t-4)//5)+1)<= 12) and ((((t-4)//5)+1) >= 0)) and  (check_buddy(self.y-11) and  archit[self.y-11][((t-4)//5)]!=0) ):
                            archit[self.y-11][((t-4)//5)] = archit[self.y-11][((t-4)//5)] -1
                            sscore.update_val(1)
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                else:
                    if((self.y <=16 and self.y >= 11) and ((t>8 and t<73) and archit[self.y-11][(t-9)//5]!=0)):
                        archit[self.y-11][(t-9)//5] = archit[self.y-11][(t-9)//5]-1
                        sscore.update_val(1)
                        self.speedy = -1 * self.speedy
                        
            elif(self.speedx < 0 ):
                t = self.x
                if(t%5==4 and t>9):
                    fldw = False
                    flss = False
                    if((self.y <=15 and self.y >= 10) and ((t>9 and t<=74) and ( check_buddy(self.y-10) and archit[self.y-10][((t-14)//5)]!=0))):
                        flss = True
                    if((self.y <=16 and self.y >= 11) and ((t>= 9 and t<=69) and ( check_buddy(self.y-11) and archit[self.y-11][(t-9)//5]!=0))):
                        fldw = True
                    
                    if(flss==True and fldw==True):
                        archit[self.y-10][((t-14)//5)]=archit[self.y-10][((t-14)//5)]-1
                        archit[self.y-11][(t-9)//5] = archit[self.y-11][(t-9)//5]-1
                        sscore.update_val(2)
                        self.speedx = -1 * self.speedx
                        self.speedy = -1 * self.speedy
                    elif(flss == True):
                        archit[self.y-10][((t-14)//5)]=archit[self.y-10][((t-14)//5)]-1
                        sscore.update_val(1)
                        self.speedx = -1 * self.speedx
                    elif(fldw == True):
                        archit[self.y-11][(t-9)//5] = archit[self.y-11][(t-9)//5]-1
                        sscore.update_val(1)
                        self.speedy = -1 * self.speedy
                    else:
                        if(( ((((t-4)//5)-1)>=0) and ((((t-4)//5)-1)<=12) ) and ( check_buddy(self.y-11) and archit[self.y-11][((t-4)//5)-1]!=0) ):
                            archit[self.y-11][((t-4)//5)-1] = archit[self.y-11][((t-4)//5)-1] -1
                            sscore.update_val(1)
                            self.speedx = -1 * self.speedx
                            self.speedy = -1 * self.speedy
                else:
                    if( (self.y>=11 and self.y<=16) and ( (t>8 and t<73) and ( check_buddy(self.y-11) and archit[self.y-11][(t-9)//5]!=0))):
                        archit[self.y-11][(t-9)//5] = archit[self.y-11][(t-9)//5]-1
                        sscore.update_val(1)
                        self.speedy = -1 * self.speedy
            else:
                if((self.y>=11 and self.y<=16) and ( check_buddy(self.y-11) and  archit[self.y-11][(t-9)//5]!=0)):
                    archit[self.y-11][(t-9)//5] = archit[self.y-11][(t-9)//5]-1
                    sscore.update_val(1)
                    self.speedy = -1 * self.speedy


        if(self.speedy > 0):
            pass
        
        
        # pos = self.x + self.speedx
        # if(self.speedy > 0):      # Going down
        #     if((pos>=9 and pos<=73)and (self.y<=14 and self.y>=9)):
        #         g = pos-9
        #         t = g
        #         while(t%5!=0):
        #             t=t+1
        #         t = t//5
        #         if(archit[self.y-9][t]!=0):
        #             archit[self.y-9][t] = archit[self.y-9][t] -1
        #             self.speedy = -1 * self.speedy
        #         else :
        #             if((g%5 == 0 and self.speedx < 0) and (t!=0 and archit[self.y-9][t-1]!=0)):
        #                 self.speedx = -1 * self.speedx
        #                 archit[self.y-9][t-1]=archit[self.y-9][t-1]-1
        #             elif((g%5 == 4 and self.speedx > 0) and (t!=12 and archit[self.y-9][t+1]!=0)):
        #                 self.speedx = -1 * self.speedx
        #                 archit[self.y-9][t+1]=archit[self.y-9][t+1]-1
        # elif(self.speedy < 0):      # Going up
        #     if((pos>=9 and pos<=73)and (self.y<=16 and self.y>=11)):
        #         g = pos - 4
        #         t = pos - 9
        #         while(t%5!=0): 
        #             t=t+1
        #         t = t//5
        #         if(archit[self.y-11][t]!=0):
        #             archit[self.y-11][t] = archit[self.y-11][t] -1
        #             self.speedy = -1 * self.speedy
        #         else :
        #             if((g%5 == 0 and self.speedx < 0) and (t!=0 and archit[self.y-11][t-1]!=0)):
        #                 self.speedx = -1 * self.speedx
        #                 archit[self.y-11][t-1]=archit[self.y-11][t-1]-1
        #             elif((g%5 == 4 and self.speedx > 0) and (t!=12 and archit[self.y-11][t+1]!=0)):
        #                 self.speedx = -1 * self.speedx
        #                 archit[self.y-11][t+1]=archit[self.y-11][t+1]-1
            
            
        # if(self.y >= 10 and self.y <=15):
        #     if(self.speedx < 0 and archit[self.y-10][(self.x//6)-1]!=0):
        #         self.speedx = -1 * self.speedx
        #         archit[self.y-10][(self.x//6)-1] = archit[self.y-10][(self.x//6)-1] -1
        #     if(self.speedx > 0 and archit[self.y-10][(self.x //6)+1]!=0):
        #         self.speedx = -1 * self.speedx
        #         archit[self.y-10][(self.x//6)+1] = archit[self.y-10][(self.x//6)+1] -1
        
        
        # if(self.speedy < 0):
        #     if((self.y >= 11) and (self.y<=16)):
        #         if((self.x - 5)%6==0):
        #             if(self.x == 5):
        #                 if(self.speedx > 0 and archit[self.y-11][0]!=0):
        #                     self.speedx = -1 * self.speedx
        #                     self.speedy = -1 * self.speedy
        #                     archit[self.y-11][0]=archit[self.y-11][0]-1
        #                 if(self.speedx < 0 and archit[self.y-11][0]!=0):
        #                     self.speedx = -1 * self.speedx
        #                     self.speedy = -1 * self.speedy
        #                     archit[self.y-11][0]=archit[self.y-11][0]-1
                            
        #             elif(self.x == 77 and archit[self.y-11][11]!=0):
        #                 if(self.speedx > 0 and archit[self.y-11][11]!=0):
        #                     self.speedx = -1 * self.speedx
        #                     self.speedy = -1 * self.speedy
        #                     archit[self.y-11][11]=archit[self.y-11][11]-1
        #                 if(self.speedx < 0 and archit[self.y-11][11]!=0):
        #                     self.speedx = -1 * self.speedx
        #                     self.speedy = -1 * self.speedy
        #                     archit[self.y-11][11]=archit[self.y-11][11]-1
        #             else:
        #                 if(archit[self.y-11][(self.x//6)] !=0 and archit[self.y-11][(self.x//6)-1]!=0):
        #                     self.speedy = -1 * self.speedy
        #                     archit[self.y-11][(self.x//6)]=archit[self.y-11][(self.x//6)]-1
        #                     archit[self.y-11][(self.x//6)-1]=archit[self.y-11][(self.x//6)-1]-1
        #                 elif(archit[self.y-11][(self.x//6)-1]!=0):
        #                     archit[self.y-11][(self.x//6)-1]=archit[self.y-11][(self.x//6)-1]-1
        #                     self.speedy = -1 * self.speedy
        #                     if(self.speedx < 0):
        #                         self.speedx = -1 * self.speedx
        #                 elif(archit[self.y-11][(self.x//6)]!=0):
        #                     archit[self.y-11][(self.x//6)]=archit[self.y-11][(self.x//6)]-1
        #                     self.speedy = -1 * self.speedy
        #                     if(self.speedx > 0):
        #                         self.speedx = -1 * self.speedx
        #         else:
        #             t = self.x
        #             for i in range(0,8):
        #                 if(t%6==0):
        #                     break
        #                 t=t-1
        #             t = t//6
        #             t = t-1
        #             if(archit[self.y-11][t]!=0):
        #                 # print(self.x)
        #                 archit[self.y-11][t]=archit[self.y-11][t]-1
        #                 self.speedy = -1 * self.speedy

        # elif(self.speedy > 0):
        #     if((self.y >= 9) and (self.y<=14)):
        #         if((self.x - 5)%6==0):
        #             if(self.x == 5):
        #                 if(self.speedx > 0 and archit[self.y-9][0]!=0):
        #                     self.speedx = -1 * self.speedx
        #                     self.speedy = -1 * self.speedy
        #                     archit[self.y-9][0]=archit[self.y-9][0]-1
        #                 elif(self.speedx < 0 and archit[self.y-9][0]!=0):
        #                     self.speedx = -1 * self.speedx
        #                     self.speedy = -1 * self.speedy
        #                     archit[self.y-9][0]=archit[self.y-9][0]-1
        #             elif(self.x == 77 and archit[self.y-9][9]!=0):
        #                 if(self.speedx > 0):
        #                     self.speedx = -1 * self.speedx
        #                     self.speedy = -1 * self.speedy
        #                     archit[self.y-9][9]=archit[self.y-9][9]-1
        #                 elif(self.speedx < 0):
        #                     self.speedx = -1 * self.speedx
        #                     self.speedy = -1 * self.speedy
        #                     archit[self.y-9][9]=archit[self.y-9][9]-1
        #             else:
        #                 if(archit[self.y-9][(self.x//6)] !=0 and archit[self.y-9][(self.x//6)-1]!=0):
        #                     self.speedy = -1 * self.speedy
        #                     archit[self.y-9][(self.x//6)]=archit[self.y-9][(self.x//6)+1]-1
        #                     archit[self.y-9][(self.x//6)-1]=archit[self.y-9][(self.x//6)-1]-1
        #                 elif(archit[self.y-9][(self.x//6)-1]!=0):
        #                     archit[self.y-9][(self.x//6)-1]=archit[self.y-9][(self.x//6)-1]-1
        #                     self.speedy = -1 * self.speedy
        #                     if(self.speedx < 0):
        #                         self.speedx = -1 * self.speedx
        #                 elif(archit[self.y-9][(self.x//6)]!=0):
        #                     archit[self.y-9][(self.x//6)]=archit[self.y-9][(self.x//6)]-1
        #                     self.speedy = -1 * self.speedy
        #                     if(self.speedx > 0):
        #                         self.speedx = -1 * self.speedx
        #         else:
        #             t = self.x
        #             for i in range(0,8):
        #                 if(t%6==0):
        #                     break
        #                 t=t-1
        #             t = t//6
        #             t = t-1
        #             if(archit[self.y-9][t]!=0):
        #                 self.speedy = -1 * self.speedy
        #                 archit[self.y-9][t]=archit[self.y-9][t]-1
        return True

    def collision_paddle(self,ppadle):
        if((self.speedy > 0) and (self.y == 27) and ((self.x >= ppadle.x) and (self.x <= (ppadle.x + ppadle.length)))):
            t1 = self.x - ppadle.x
            t1 = t1 // ppadle.scale
            t1 = t1 - (ppadle.length//2)
            # self.speedx = self.speedx + t1
            self.speedy = -1 * self.speedy
            # print("OKOK")
        return True
    
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
    
    def ball_move(self):
        self.x = self.x + self.speedx
        self.y = self.y + self.speedy