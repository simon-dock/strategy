import pygame
import init
import unit

#座標が盤面上（7☓11)のどの領域にあるのか取得する
def pos_grid():

    x_raw, y_raw = pos_cursor()

    for i in range(init.Y_BOARD):
        for j in range(init.X_BOARD):
            x = 110*j+init.X_ORIGIN-5
            y = 110*i+init.Y_ORIGIN-5
            if x_raw >= x and x+110 >= x_raw and y_raw >= y and y+110 >= y_raw:
                return j, i

    return -1,-1 

#ユニットを選択する画面のとき、どの領域にあるのか取得する
def pos_select_list():

    x_raw, y_raw = pos_cursor()

    x = init.X_MID2 + 15

    for i in range(unit.NUMBER):
        y = 75*i+175
        if x_raw >= x and x+350 >= x_raw and y_raw >= y and y+75 >= y_raw:
            return i

    return -1

def pos_select_infor_unit():

    x_raw, y_raw = pos_cursor()

    x = 1720
    y = 600

    if x_raw >= x and x+180 >= x_raw and y_raw >= y and y+75 >= y_raw:
        return 1
    
    x = 1920

    if x_raw >= x and x+180 >= x_raw and y_raw >= y and y+75 >= y_raw:
        return 2

    return -1

#マウスカーソルがある位置を取得する
def pos_cursor():

    x_raw, y_raw = pygame.mouse.get_pos()
    x = x_raw
    y = y_raw

    return x, y