
class Lives:
    def __init__(self,initialval):
        self.val = initialval
    def return_life(self):
        return self.val
    def sub_life(self):
        self.val = self.val - 1
        return self.val
    def add_life(self):
        self.val = self.val + 1
        return self.val

class Time:
    def __init__(self):
        self.cur = 0
    def return_time(self):
        return self.cur

class Score:
    def __init__(self):
        self.cur = 0
    def return_score(self):
        return self.cur