from select import select
import pygame
import init
import unit
import color
import flag
import Get
import Draw


#文字列を表示する
def string(WIN, pre_text, size, colors, x, y):
    Font = pygame.font.get_fonts()
    FORMAT = pygame.font.SysFont(Font[29],size)
    text = FORMAT.render(pre_text, True, color.select(colors))
    WIN.blit(text, (x, y))

#背景のある文字列を表示する
def string_bg(WIN, pre_text, size, colors1, colors2, x, y):
    Font = pygame.font.get_fonts()
    FORMAT = pygame.font.SysFont(Font[29],size)
    text = FORMAT.render(pre_text, True, color.select(colors1), color.select(colors2))
    WIN.blit(text, (x, y))
    

#マウスカーソルがあるマスを強調表示する
def pos_cursor(WIN):
    
    x_ren, y_ren = Get.pos_grid()
    if x_ren != -1 and y_ren != -1:
        x = 100*x_ren+10*x_ren+init.X_ORIGIN-1
        y = 100*y_ren+10*y_ren+init.Y_ORIGIN-1
        Draw.empty_square(WIN, "WHITE", 4, x, y, x, y+102, x+102, y+102, x+102, y)

#どのユニットが選択されているか強調表示する
def pos_cursor_unit(WIN):
    selection = Get.pos_select_list()
    if selection != -1:
        x = init.X_MID2 + 20
        y = 75*selection+240
        Draw.line(WIN, "WHITE", 4, x, y, x+350, y)

#どれが選択されているか強調表示する
def pos_cursor_infor_unit(WIN):
    selection = Get.pos_select_infor_unit()
    if selection != -1:
        x = 1520+selection*200
        y = 660
        Draw.line(WIN, "WHITE", 4, x, y, x+150, y)
    



#メニューを表示する
def infor_menu(WIN):

    string(WIN, "- Help -", 50, "WHITE", 1700, 100)
    string(WIN, "m : List of unit", 40, "WHITE", 1700, 160)


#選択された情報を表示する
def infor_selection(WIN):

    x_ren, y_ren = Get.pos_grid()
    if x_ren != -1 and y_ren != -1:
        pre_text = "Coordinate "+str(x_ren+1)+" "+str(y_ren+1)
        string(WIN, pre_text, 40, "WHITE", init.X_MID+5, 100)
      


#ユニットの一覧を表示する
def list_unit(WIN, unit_data):

    pos_cursor_unit(WIN)

    string(WIN, "- List of Unit -", 50, "WHITE", 1700, 100)
    for i in range(unit.NUMBER):
        string(WIN, unit_data[i].name, 50, "WHITE", 1700, 175+i*75)




#ユニットの情報を表示する
def infor_unit(WIN, unit_data, selection):

    pos_cursor_infor_unit(WIN)

    string(WIN, "- Infor of Unit -", 50, "WHITE", 1700, 100)
    string(WIN, unit_data[selection].name, 50, "WHITE", 1700, 175)
    string(WIN, "Power", 40, "WHITE", 1740, 205+50)
    string(WIN, "Health", 40, "WHITE", 1740, 205+100)
    string(WIN, "Action", 40, "WHITE", 1740, 205+150)
    string(WIN, "Range", 40, "WHITE", 1740, 205+200)
    string(WIN, "Time", 40, "WHITE", 1740, 205+250)
    string(WIN, "Cost", 40, "WHITE", 1740, 205+300)
    string(WIN, str(unit_data[selection].power), 40, "WHITE", 1900, 205+50)
    string(WIN, str(unit_data[selection].health), 40, "WHITE", 1900, 205+100)
    string(WIN, str(unit_data[selection].action), 40, "WHITE", 1900, 205+150)
    string(WIN, str(unit_data[selection].range), 40, "WHITE", 1900, 205+200)
    string(WIN, str(unit_data[selection].time), 40, "WHITE", 1900, 205+250)
    string(WIN, str(unit_data[selection].cost), 40, "WHITE", 1900, 205+300)

    string(WIN , "Deploy", 45, "WHITE", 1720, 600)
    string(WIN , "BACK", 45, "WHITE", 1920, 600)

def deploy_unit(WIN, unit_data, selection):

    string(WIN, "- Depley Unit -", 50, "WHITE", 1700, 100)
    string(WIN, unit_data[selection].name, 50, "WHITE", 1700, 175)
    string(WIN, "is selected", 50, "WHITE", 1740, 255)