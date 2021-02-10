class Paddle:

    def __init__(self):
        self.length = 10
        self.sticky = False
        self.cordinate = 26
        self.x = 54
        self.arr = [" "]*4 + ["|"] + [" "]*109 + ["|"]
        print(self.arr)
        for i in range(54,54+self.length):
            self.arr[i]="_"

    def addpaddle(self,t):
        self.arr = [" "]*115
        self.arr[4]="|"
        self.arr[114]="|"
        for i in range(t,t+self.length):
            self.arr[i]="_"

    def upgrade(self):
        self.length = self.length + 2
        return 

    def degrade(self):
        self.length = self.length - 2
        return

    def move_right(self):
        right_coordinate = self.x + self.length
        if(right_coordinate < 114):
            self.x = self.x + 1
        self.addpaddle(self.x)

    def move_left(self):
        left_coordinate = self.x
        if(left_coordinate > 5):
            self.x = self.x - 1
        self.addpaddle(self.x)

    def print_paddle(self):
        for i in range(0,len(self.arr)):
            print(self.arr[i],end="")
        print("?\n",end="")