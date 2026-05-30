import pygame
from grid import *
from monitor import Monitor
from item_selection import *
from game_status import GameStatus
from menu import *
from data_base import DataBase
from utils import resource_path

pygame.init()
WHIDTH = 600
HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((WHIDTH,HEIGHT))
pygame.display.set_caption("Hamitory")
icon = pygame.image.load(resource_path("images//icon.png"))
pygame.display.set_icon(icon)
data_base = DataBase()
clock = pygame.time.Clock()

if data_base.get_data("is_first_time") == True:
    game_status = GameStatus.Guide_Menu
else:
    game_status = GameStatus.Play_Menu


monitor = Monitor(300,120)
item_sc = ItemSelection(300,300)
twin_slot = TwinItemSlot(HEIGHT//2,540)
grid = Grid(WHIDTH,HEIGHT)
guid_menu  = GuideMenu(WHIDTH,HEIGHT)
start_menu = StartMenu(WHIDTH,HEIGHT)
stop_menu = StopMenu(WHIDTH,HEIGHT)
game_wining = None

def restart():
    item_sc.reset()
    grid.reset_grid()
    monitor.reset_monitor()
    twin_slot.reset()

running = True
while running:
    dt = clock.tick(FPS)
    screen.fill((0,55,165))
    if game_wining == True:
        stop_menu.win_pic.draw(screen)
    
    elif game_wining == False:
        stop_menu.lose_pic.draw(screen)

    if game_status == GameStatus.Guide_Menu:
        guid_menu.draw(screen)
        guid_menu.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                resault = guid_menu.operation(event.key)
                if resault == "continue":
                    data_base.set_data("is_first_time",False)
                    game_status = GameStatus.Play_Menu

    if game_status == GameStatus.Play_Menu:
        start_menu.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    resault = start_menu.operation(mouse_pos)
                    if resault == "play":
                        game_status = GameStatus.Item_Selection
                    if resault == "guide":
                        game_status = GameStatus.Guide_Menu
                    if resault == "quit":
                        running = False

    if game_status == GameStatus.Item_Selection:
        item_sc.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if item_sc.enter_selection():
                        value = item_sc.pass_the_item_list()
                        twin_slot.add_item(value)
                        game_status = GameStatus.Game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    item_sc.operation(mouse_pos)
                    
                item_sc.check_selection()

    if game_status == GameStatus.Stop_Menu or game_status == GameStatus.End_Menu:
        stop_menu.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and game_status == GameStatus.Stop_Menu:
                    game_status = GameStatus.Game

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    resault = stop_menu.operation(mouse_pos)
                    if resault == "exit":
                        game_wining = None
                        restart()
                        game_status = GameStatus.Play_Menu
                    elif resault == "restart":
                        game_wining = None
                        game_status = GameStatus.Item_Selection
                        restart()

    if game_status == GameStatus.Game:
        monitor.draw(screen)
        grid.draw(screen)
        twin_slot.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_status = GameStatus.Stop_Menu 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for item in twin_slot.items_sprites.sprites():
                        if item.is_clicked(mouse_pos) and item.activation:
                            item.operation(grid,monitor)
                    grid.operation(mouse_pos,monitor)
                
                if event.button == 3:
                    grid.next_operation()
                 
        if grid.blue_count == grid.blue_limit:
            game_wining = True
            value = data_base.get_data('count_of_win') + 1
            data_base.set_data('count_of_win',value)
            game_status = GameStatus.End_Menu
        elif grid.red_count == grid.red_limit:
            game_wining = False
            stop_menu.lose_pic.draw(screen)
            value = data_base.get_data('count_of_lose') + 1
            data_base.set_data('count_of_lose',value)
            game_status = GameStatus.End_Menu

    pygame.display.flip()
pygame.quit()