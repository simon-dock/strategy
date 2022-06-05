import pygame
import init
import color
import board
import Display


def square(WIN, colors, x, y):
    pygame.draw.rect(WIN, colors, (x, y, 100, 100))

def empty_square(WIN, colors, size, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    pos = [[x_1, y_1], [x_2, y_2], [x_3, y_3], [x_4, y_4]]
    pygame.draw.lines(WIN, color.select(colors), True, pos, size)

def line(WIN, colors, size, x_1, y_1, x_2, y_2):
    pos = [[x_1, y_1], [x_2, y_2]]
    pygame.draw.lines(WIN, color.select(colors), True, pos, size)

def partition_line(WIN):

    Display.string(WIN, "Selected Infor", 50, "WHITE", 1250, 20)
    Display.string(WIN, "Player Menu", 50, "WHITE", 1700, 20)

    FORMAT = pygame.font.SysFont(None,50)
    text = FORMAT.render("----------------------------------------", True, color.select("WHITE"))
    WIN.blit(text, (1230,70))
    text = FORMAT.render("----------------------------------------", True, color.select("WHITE"))
    WIN.blit(text, (1680,70))
    empty_square(WIN, "WHITE", 7, 0, 0, 0, init.WIN_HEIGHT, init.WIN_WIDTH, init.WIN_HEIGHT, init.WIN_WIDTH, 0)

    line(WIN, "WHITE", 5, init.X_MID, 0, init.X_MID, init.WIN_HEIGHT)
    line(WIN, "WHITE", 5, init.X_MID2, 0, init.X_MID2, init.WIN_HEIGHT)
    line(WIN, "WHITE", 5, 0, init.Y_MID, init.X_MID, init.Y_MID)
    


def board_surface(WIN):

    WIN.fill(color.select("BLACK"))

    for i in range(init.Y_BOARD):
        for j in range(init.X_BOARD):
            x_raw = 100*j+10*j+init.X_ORIGIN
            y_raw = 100*i+10*i+init.Y_ORIGIN
            color_now = board.terrain[i][j]
            square(WIN, color.select(color_now), x_raw, y_raw)

    partition_line(WIN)