import pygame

NUMBER = 5

def init(data):
    data[0] = Saber()
    data[1] = Archer()
    data[2] = Shielder()
    data[3] = Cavalry()
    data[4] = Magician()

#ユニットのクラス
class Unit():

    side = 0

    def __init__(self,n,p,h,a,r,t,c,img):
        self.name = n
        self.power = p
        self.health = h
        self.action = a
        self.range = r
        self.time = t
        self.cost = c
        self.image = img

    def set(self, x):
        self.side = x



class Saber(Unit):

    def __init__(self):
        name = "Saber"
        power = 2
        health = 2
        action = 2
        range = 1
        time = 1
        cost = 100
        image = pygame.image.load(f"./image/001.png")
        super().__init__(name, power, health, action, range, time, cost, image)

class Archer(Unit):

    def __init__(self):
        name = "Archer"
        power = 1
        health = 2
        action = 2
        range = 3
        time = 1
        cost = 200
        image = pygame.image.load(f"./image/002.png")
        super().__init__(name, power, health, action, range, time, cost, image)

class Shielder(Unit):

    def __init__(self):
        name = "Shielder"
        power = 2
        health = 4
        action = 1
        range = 1
        time = 2
        cost = 300
        image = pygame.image.load(f"./image/001.png")
        super().__init__(name, power, health, action, range, time, cost, image)

class Cavalry(Unit):

    def __init__(self):
        name = "Cavalry"
        power = 3
        health = 3
        action = 3
        range = 1
        time = 3
        cost = 600
        image = pygame.image.load(f"./image/001.png")
        super().__init__(name, power, health, action, range, time, cost, image)


class Magician(Unit):

    def __init__(self):
        name = "Magician"
        power = 4
        health = 1
        action = 1
        range = 2
        time = 2
        cost = 400
        image = pygame.image.load(f"./image/001.png")
        super().__init__(name, power, health, action, range, time, cost, image)
