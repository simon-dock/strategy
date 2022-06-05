from re import U
import pygame
from pygame.locals import *

import init
import color
import unit
import board
import flag

import Draw
import Get
import Judge
import Display

#ウィンドウの初期化
pygame.init()
WIN = pygame.display.set_mode((init.WIN_WIDTH, init.WIN_HEIGHT))

unit_data = [0 for i in range(unit.NUMBER)]
unit.init(unit_data)


def main():
    
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if flag.LIST_UNIT == True:
                    selection_unit = Get.pos_select_list()
                    if selection_unit != -1:
                        flag.INFOR_UNIT = True
                        flag.LIST_UNIT = False

                if flag.INFOR_UNIT == True:
                    selection_deploy = Get.pos_select_infor_unit()
                    if selection_deploy == 1:
                        flag.DEPLOY_UNIT = True
                        flag.INFOR_UNIT = False
                    if selection_deploy == 2:
                        flag.LIST_UNIT = True
                        flag.INFOR_UNIT = False


                x, y = Get.pos_grid()
                if x == -1:continue
                

            if event.type == KEYDOWN:  # キーを押したとき
                Judge.key(event)

        Draw.board_surface(WIN)
        Display.pos_cursor(WIN)
        Display.infor_selection(WIN)

        
       
        if flag.LIST_UNIT == True:
            Display.list_unit(WIN, unit_data)
        elif flag.INFOR_UNIT == True:
            Display.infor_unit(WIN, unit_data, selection_unit)
        elif flag.DEPLOY_UNIT == True:
            Display.deploy_unit(WIN, unit_data, selection_unit)
        else:
            Display.infor_menu(WIN)

        


        pygame.time.delay(10)
        pygame.display.update()

if __name__ == '__main__':
    main()
