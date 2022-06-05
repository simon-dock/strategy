import pygame
import init
import color
import board

def square(WIN, colors, x, y):
    pygame.draw.rect(WIN, colors, (x, y, 100, 100))

def partition_line(WIN):
    start_pos = [[0,0],[0,init.WIN_HEIGHT],[init.WIN_WIDTH,init.WIN_HEIGHT],[init.WIN_WIDTH,0]]
    pygame.draw.lines(WIN, color.select("WHITE"), True, start_pos, 7)
    start_pos = [[init.X_MID,0],[init.X_MID,init.WIN_HEIGHT]]
    pygame.draw.lines(WIN, color.select("WHITE"), True, start_pos, 5)
    start_pos = [[init.X_MID2,0],[init.X_MID2,init.WIN_HEIGHT]]
    pygame.draw.lines(WIN, color.select("WHITE"), True, start_pos, 5)
    start_pos = [[0,init.Y_MID],[init.X_MID,init.Y_MID]]
    pygame.draw.lines(WIN, color.select("WHITE"), True, start_pos, 5)


def board_surface(WIN):

    WIN.fill(color.select("BLACK"))

    for i in range(init.Y_BOARD):
        for j in range(init.X_BOARD):
            x_ren = 100*j+10*j+init.X_ORIGIN
            y_ren = 100*i+10*i+init.Y_ORIGIN
            color_now = board.terrain[i][j]
            square(WIN, color.select(color_now), x_ren, y_ren)

    partition_line(WIN)