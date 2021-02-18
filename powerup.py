
class Power:
    
    def __init__(self,x,y,num,tinka):
        self.x = x
        self.y = y+10
        self.speedy = 2
        self.num = num
        self.start = int(tinka)
        self.starteff = 0
        self.active = True
    
    def print_data(self):
        print(self.x,self.y,self.speedy,self.num,self.start,self.starteff,self.active)
    
    # def print_label(self):
    #     print()
    
    def restore(self,ppadle,bball):
        self.active=False
        if(self.num==1):
            print("revert spresd")
            ppadle.degrade()
        if(self.num==2):
            ppadle.upgrade()
        if(self.num==3):
            bball.sticky=False
        if(self.num==3):
            bball.thruball=False
    
    def power_move(self,bball,ppadle,cclock):
        
        self.y = self.y + self.speedy
        tt = self.x*5 + 11
        print(self.num)
        if(self.y == 25):
            if(tt >= ppadle.x and tt <= ppadle.x + ppadle.length):
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                self.starteff = cclock.return_val()
                self.collect(bball,ppadle,cclock)
            
        # if(self.y >= 26):
        #     self.active = False
    
    def collect(self,bball,ppadle,cclock):
        num = self.num
        if(num == 1):
            print("paddle spread activated")
            ppadle.upgrade()
        
        if(num == 2):
            print("paddle shrink activated")
            ppadle.degrade()
        
        if(num == 3):
            print("sticky ball activated")
            bball.sticky=True
        
        if(num == 4):
            print("thruball activated")
            bball.thruball = True
        
        if(num == 5):
            bball.fastball = True
            bball.fastball_time = True
        
        if(num == 6):
            bball.multiball = True
            bball.multiball_time = True