#地形情報
from select import select


terrain = [["0" for j in range(11)]for i in range(7)]

for i in range(7):
    for j in range(11):
        terrain[i][j] = "GREEN"


terrain[3][0] = "BLUE"#本拠地
terrain[1][1] = "W_BLUE"#ユニット製造所
terrain[3][2] = "W_BLUE"
terrain[5][1] = "W_BLUE"

terrain[3][10] = "RED"
terrain[1][9] = "W_RED"
terrain[3][8] = "W_RED"
terrain[5][9] = "W_RED"

class Ground_Both():

    def __init__(self,n,w,c):
        self.name = n
        self.whose = w
        self.color = c

class Plain(Ground_Both):

    def __init__(self):
        name = "Plain"
        whose = 0
        color = "BEIGE"
        super().__init__(name,whose,color) 


class Ground_Either():

    def __init__(self,n,w,c1,c2):
        self.name = n
        self.whose = w
        self.color1 = c1
        self.color2 = c2

    def set(self,w):
        self.whose = w

class Home(Ground_Either):

    def __init__(self):
        name = "Home"
        whose = 0
        color1 = "BLUE"
        color2 = "RED"
        super().__init__(name,whose,color1,color2) 

class Base(Ground_Either):

    def __init__(self):
        name = "Base"
        whose = 0
        color1 = "W_BLUE"
        color2 = "W_RED"
        super().__init__(name,whose,color1,color2) 
