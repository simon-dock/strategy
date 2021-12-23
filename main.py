import pygame
from pygame.locals import *
import sys

#ウィンドウの初期化
pygame.init()
WIN_WIDTH = 2200
WIN_HEIGHT = 1200
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#色
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GRAY = [193, 162, 129]
BLUE = [51, 255, 255]
W_BLUE = [204,255,255]
ORANGE = [255,127,0]

def draw_board():

    WIN.fill(BLACK)

    for i in range(10):
        for j in range(18):
            x_ren = 120*(j+1)+10*j
            y_ren = 104*(i+1)+10*i
            pygame.draw.polygon(WIN, GRAY, [(x_ren,y_ren),(x_ren+30,y_ren-52),(x_ren+90,y_ren-52),(x_ren+120,y_ren),(x_ren+90,y_ren+52),(x_ren+30,y_ren+52)])

    start_pos = [[10,10],[10,1190],[2190,1190],[2190,10]]
    pygame.draw.lines(WIN, WHITE, True, start_pos, 5)

def main():
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_board()
        pygame.time.delay(30)
        pygame.display.update()

if __name__ == '__main__':
    main()