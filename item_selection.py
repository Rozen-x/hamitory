import pygame
from item import *
from utils import resource_path
  
class ItemSlot(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        super().__init__()
        self.all_sprites = pygame.sprite.Group()
        self.items_sprites = pygame.sprite.Group()
        self.image = pygame.image.load(resource_path("images//slot.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = posX
        self.rect.centery = posY
        self.item_1 = Marker(self.rect.x + 33,self.rect.y + 20)
        self.item_2 = FiftyFifty(self.rect.x + 113,self.rect.y + 20)
        self.item_3 = KindKey(self.rect.x + 193,self.rect.y + 20)
        self.item_4 = Reverser(self.rect.x + 273,self.rect.y + 20)
        self.all_sprites.add(self)
        self.set_all_sprites()
        
    def set_all_sprites(self):  
        self.all_sprites.add(self.item_1)
        self.items_sprites.add(self.item_1)

        self.all_sprites.add(self.item_2)
        self.items_sprites.add(self.item_2)

        self.all_sprites.add(self.item_3)
        self.items_sprites.add(self.item_3)

        self.all_sprites.add(self.item_4)
        self.items_sprites.add(self.item_4)     

    def reset(self):
        for item in self.items_sprites.sprites():
            item.kill()
        self.item_1 = Marker(self.rect.x + 33,self.rect.y + 20)
        self.item_2 = FiftyFifty(self.rect.x + 113,self.rect.y + 20)
        self.item_3 = KindKey(self.rect.x + 193,self.rect.y + 20)
        self.item_4 = Reverser(self.rect.x + 273,self.rect.y + 20)
        self.set_all_sprites()

    def draw(self,screen):
        self.all_sprites.draw(screen)

class TwinItemSlot(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        super().__init__()
        self.all_sprites = pygame.sprite.Group()
        self.items_sprites = pygame.sprite.Group()
        self.image = pygame.image.load(resource_path("images//twin_slot.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = posX
        self.rect.centery = posY
        self.all_pos = [(self.rect.x + 33,self.rect.y + 20),(self.rect.x + 113,self.rect.y + 20)]
        self.all_sprites.add(self)

    def add_item(self,item_list:list):
        for index in range(2):
            item = item_list[index]
            item.set_pos(self.all_pos[index][0],self.all_pos[index][1])
            self.all_sprites.add(item)
            self.items_sprites.add(item)

    def draw(self,screen):
        self.all_sprites.draw(screen)

    def reset(self):
        self.items_sprites.empty()

class ItemSelection:
    def __init__(self,posX,posY):
        self.slot = ItemSlot(posX,posY) 
        self.count_of_selected = 0
        self.item_list = list()

    def check_selection(self):
        if self.count_of_selected == 2:
            for item in self.slot.items_sprites.sprites():
                if not item.selected:
                    item.activation = False

        if self.count_of_selected < 2:
            for item in self.slot.items_sprites.sprites():
                item.activation = True

    def draw(self,screen):
        self.slot.draw(screen)

    def operation(self,mouse_pos):
        for item in self.slot.items_sprites.sprites():
            if item.is_clicked(mouse_pos) and item.activation:
                item.selected = not item.selected

                if item.selected == True:
                    self.item_list.append(item)
                    item.rect.centery += 13
                    self.count_of_selected += 1
     
                if item.selected == False:
                    self.item_list.remove(item)
                    item.rect.centery -= 13
                    self.count_of_selected -= 1

    def pass_the_item_list(self):
        return self.item_list

    def enter_selection(self):
        return self.count_of_selected == 2
    
    def reset(self):
        self.slot.reset()
        self.item_list = list()
        self.count_of_selected = 0


