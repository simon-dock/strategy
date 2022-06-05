import pygame
import flag

#どのボタンが押されたか判断する
def key(event):
    flag.HOME = False
    flag.LIST_UNIT = False
    flag.INFOR_UNIT = False
    flag.DEPLOY_UNIT = False
    if pygame.key.name(event.key) == "m":
        flag.LIST_UNIT = True
    if pygame.key.name(event.key) == "h":
        flag.HOME = True