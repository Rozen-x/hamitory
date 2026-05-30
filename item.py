import pygame
from abc import abstractmethod
import random
from utils import resource_path

class Item(pygame.sprite.Sprite):
    def __init__(self,path,posX,posY):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.centerx = posX
        self.rect.centery = posY
        self.activation = True
        self.selected = False

    def is_clicked(self,mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def set_pos(self,posX,posY):
        self.rect.centerx = posX
        self.rect.centery = posY
    
    @abstractmethod
    def operation(self,mouse_pos):
        pass

class Marker(Item):
    def __init__(self, posX, posY):
        super().__init__(resource_path("images//marker_BTN.png"), posX, posY)

    def operation(self,grid,monitor):
        self.activation = False
        self.rect.centery += 13
        grid.marking_caccess = True
        monitor.change_text("active")
        
class Reverser(Item):
    def __init__(self, posX, posY):
        super().__init__(resource_path("images//reverse_BTN.png"), posX, posY)

    def operation(self,grid,monitor):
        self.activation = False
        self.rect.centery += 13

        for A in range(len(grid.matris)):
            for B in range(len(grid.matris[A])):
                if grid.matris[A][B] != None:
                    grid.matris[A][B] = 1 - grid.matris[A][B]
                    
        for cell in grid.cell_group.sprites():
            if cell.activation == False:
                cell.change_to_roten()

        monitor.change_text("reversed")
        
class KindKey(Item):
    def __init__(self, posX, posY):
        super().__init__(resource_path("images//kind_key_BTN.png"), posX, posY)

    def operation(self,grid,monitor):
        self.activation = False
        self.rect.centery += 13
        blue_cell = None
        attempts = 0
        while blue_cell is None and attempts < 100:
            row,col = random.randint(0,5),random.randint(0,5)
            cell_val = grid.matris[row][col]
            cell_obj = grid.get_cell(row,col)
            if cell_val == 0 and cell_obj.tag == "default":
                blue_cell = cell_obj
            attempts += 1
        monitor.change_text("safe")
        blue_cell.change_to_suggested()

class FiftyFifty(Item):
    def __init__(self, posX, posY):
        super().__init__(resource_path("images//50_50_BTN.png"), posX, posY)

    def operation(self,grid,monitor):
        self.activation = False
        self.rect.centery += 13

        blue_cell = None
        attempts = 0
        while blue_cell is None and attempts < 100:
            row,col = random.randint(0,5),random.randint(0,5)
            cell_val = grid.matris[row][col]
            cell_obj = grid.get_cell(row,col)
            if cell_val == 0 and cell_obj.tag == "default":
                blue_cell = cell_obj
            attempts += 1

        red_cell = None
        attempts = 0
        while red_cell is None and attempts < 100:
            row,col = random.randint(0,5),random.randint(0,5)
            cell_val = grid.matris[row][col]
            cell_obj = grid.get_cell(row,col)
            if cell_val == 1 and cell_obj.tag == "default":
                red_cell = cell_obj
            attempts += 1
        monitor.change_text("guess")
        blue_cell.change_to_guess()
        red_cell.change_to_guess()

        

            


        


        

        


