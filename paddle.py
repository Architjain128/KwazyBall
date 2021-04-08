class Paddle:

    def __init__(self):
        self.scale = 3
        self.length = 5*self.scale
        self.sticky = True
        self.cordinate = 26
        self.x = 34
        self.arr = [" "]*4 + ["|"] + [" "]*61 + ["|"]
        for i in range(34,34+self.length):
            self.arr[i]="_"

    def addpaddle(self,t):
        self.arr = [" "]*79
        self.arr[4]="|"
        self.arr[66]="|"
        for i in range(t,t+self.length):
            self.arr[i]="_"

    def set_sticky(self,t):
        self.sticky = t
    
    def upgrade(self):
        self.length = self.length + 2*self.scale
        return 

    def degrade(self):
        self.length = self.length - 2*self.scale
        return

    def move_right(self,bball):
        right_coordinate = self.x + self.length
        if(right_coordinate < 78):
            cc = min(self.x + self.scale,78-self.length)
            dd = cc - self.x
            self.x = cc
            if((self.sticky==True or bball.sticky == True ) and bball.y==27):
                bball.x = bball.x + dd
                bball.speedy = 0
                bball.speedx = 0
        self.addpaddle(self.x)

    def move_left(self,bball):
        left_coordinate = self.x
        if(left_coordinate > 5):
            cc = max(self.x - self.scale,5)
            dd = cc -self.x
            self.x = cc
            if((self.sticky==True or bball.sticky == True ) and bball.y==27):
                bball.x = bball.x + dd
                bball.speedx = 0
                bball.speedy = 0
        self.addpaddle(self.x)

    def print_paddle(self):
        for i in range(0,len(self.arr)):
            print(self.arr[i],end="")
        print("\n",end="")