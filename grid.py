import pygame
from enum import Enum
from shuffle import Shuffle
from monitor import Monitor
from utils import resource_path

class CellState(Enum):
    State_1 = pygame.image.load(resource_path("images//HARD_state_1.png"))
    State_2 = pygame.image.load(resource_path("images//HARD_state_2.png"))
    State_3 = pygame.image.load(resource_path("images//HARD_state_3.png"))
    State_4 = pygame.image.load(resource_path("images//mark_state.png"))
    State_5 = pygame.image.load(resource_path("images//roten_state.png"))
    State_6 = pygame.image.load(resource_path("images//guess_state.png"))
    State_7 = pygame.image.load(resource_path("images//suggest_state.png"))

class GridCell(pygame.sprite.Sprite):
    def __init__(self,posX,posY,matris_pos:tuple):
        super().__init__()
        self.img_1 = CellState.State_1.value
        self.img_2 = CellState.State_2.value
        self.img_3 = CellState.State_3.value
        self.mark_img = CellState.State_4.value
        self.roten_img = CellState.State_5.value
        self.guess_img = CellState.State_6.value
        self.suggest_img = CellState.State_7.value
 
        self.image = self.img_1
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.matris_pos = matris_pos
        self.activation = True
        self.tag = "default"

    def is_clicked(self,mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def change_to_blue(self):
        self.image = self.img_2
        self.activation = False
        self.tag = "blue"

    def change_to_red(self):
        self.image = self.img_3
        self.activation = False
        self.tag = "red"

    def change_to_marked(self):
        self.image = self.mark_img
        self.tag = "mark"

    def change_to_roten(self):
        self.image = self.roten_img
        self.tag = 'roten'

    def change_to_guess(self):
        self.image = self.guess_img
        self.tag = "gues_mark"

    def change_to_suggested(self):
        self.image = self.suggest_img
        self.tag = "suggest_mark"

    def change_to_default(self):
        self.image = self.img_1
        self.tag = "default"

class Grid:
    def __init__(self,posX,posY):
        self.num_row = 6
        self.num_col = 6
        self.all_cells = 36
        self.margin = 50
        self.red_limit = 16
        self.blue_limit = 16
        self.red_count = 0
        self.blue_count = 0
        self.posX = posX
        self.posY = posY
        self.grid_size = 300
        self.marking_caccess = False
        self.cell_group = pygame.sprite.Group()
        self.create_matris()
        self.create_grid()

    def create_matris(self):
        self.matris = Shuffle.get_shuffled_matris(0,1,self.all_cells)
      
    def create_grid(self):
        startX = (self.posX - self.grid_size)/2
        startY = (self.posY - self.grid_size)/2
        for row in range(self.num_row):
            for col in range(self.num_col):
                cell = GridCell(startX+(col*self.margin),startY+(row*self.margin),(row,col))
                self.cell_group.add(cell)

    def draw(self,screen):
        self.cell_group.draw(screen)
        
    def check(self,row:int,col:int):
        if self.matris[row][col] == 1:
            return True
        return False
    
    def counting(self,col,row):
        inRow = 0
        inColumn = 0
        for _ in range(self.num_row):
            if self.matris[col][_] == 1:
                inRow += 1

        for _ in range(self.num_col):
            if self.matris[_][row] == 1:
                inColumn += 1

        return (inRow,inColumn)
    
    def reset_grid(self):
        for cell in self.cell_group.sprites():
            cell.activation = True
            cell.change_to_default()
        self.create_matris()
        self.red_count = 0
        self.blue_count = 0
        self.marking_caccess = False

    def unable_grid(self):
        for cell in self.cell_group.sprites():
            cell.activation = False
    
    def inable_grid(self):
        for cell in self.cell_group.sprites():
            if not cell.pressed:
                cell.activation = True

    def operation(self,mouse_pos,monitor:Monitor):
        for cell in self.cell_group.sprites():
            if cell.is_clicked(mouse_pos) and cell.activation:
                if self.check(cell.matris_pos[0],cell.matris_pos[1]):
                    self.red_count += 1
                    cell.change_to_red()
                    monitor.reset_monitor()
                else:
                    self.blue_count += 1
                    position = self.counting(cell.matris_pos[0],cell.matris_pos[1])
                    cell.change_to_blue()
                    monitor.change_text(f"{position[0]} : {position[1]}")
                self.matris[cell.matris_pos[0]][cell.matris_pos[1]] = None

    def next_operation(self):
        if self.marking_caccess == True:
            mouse_pos = pygame.mouse.get_pos()
            for cell in self.cell_group.sprites():
                if cell.is_clicked(mouse_pos) and cell.activation and cell.tag == 'default':
                    cell.change_to_marked()

                elif cell.is_clicked(mouse_pos) and cell.activation and cell.tag == 'mark':
                    cell.change_to_default()
                    
    def get_cell(self,posX,posY):
        for cell in self.cell_group.sprites():
            if cell.matris_pos == (posX,posY):
                return cell
                
                

        
                                                                                       
        

