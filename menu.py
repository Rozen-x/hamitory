from typing import Any
import pygame
from button import Button
from abc import abstractmethod
from utils import resource_path

class Menu:
    def __init__(self,screen_width,screen_height):
        self.sprites = pygame.sprite.Group()

    def draw(self,screen):
        for button in self.sprites.sprites():
            button.draw(screen)

    @abstractmethod
    def set_all_sprites(self):
        pass

    @abstractmethod
    def operation(self,mouse_pos):
        pass

class StartMenu(Menu):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.guide_button = Button(resource_path("images//empty_BTN.png"),(screen_width//2),(screen_height//2),"Guide")
        self.start_button = Button(resource_path("images//empty_BTN.png"),(screen_width//2),(screen_height//2)-50,"Start")
        self.quit_button =  Button(resource_path("images//empty_BTN.png"),(screen_width//2),(screen_height//2)+50,"Quit")
        self.set_all_sprites()

    def set_all_sprites(self):
        self.sprites.add(self.guide_button)
        self.sprites.add(self.start_button)
        self.sprites.add(self.quit_button)
        
    def operation(self,mouse_pos):
        if self.start_button.is_clicked(mouse_pos):
            return "play"
        if self.quit_button.is_clicked(mouse_pos):
            return "quit"
        if self.guide_button.is_clicked(mouse_pos):
            return "guide"

class StopMenu(Menu):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.restart_button = Button(resource_path("images//empty_BTN.png"),(screen_width//2) + 120,screen_height//2,"Restart")
        self.exit_button = Button(resource_path("images//empty_BTN.png"),(screen_width//2) - 120,screen_height//2,"Main Menu")
        self.win_pic = Button(resource_path('images//win_pic.png'),300,150)
        self.lose_pic = Button(resource_path('images//lose_pic.png'),300,150)
        self.set_all_sprites()

    def set_all_sprites(self):
        self.sprites.add(self.restart_button)
        self.sprites.add(self.exit_button)

    def operation(self,mouse_pos):
        if self.exit_button.is_clicked(mouse_pos):
            return "exit"
        if self.restart_button.is_clicked(mouse_pos):
            return "restart"

class GuideMenu(Menu):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.slide1 = Slide(resource_path("images//Slide1.PNG"),300,300)
        self.slide2 = Slide(resource_path("images//Slide2.PNG"),900,300)
        self.slide1_pos = (300,300)
        self.slide2_pos = (900,300)
        self.set_all_sprites()

    def set_all_sprites(self):
        self.sprites.add(self.slide1)
        self.sprites.add(self.slide2)
    
    def draw(self,screen):
        self.sprites.draw(screen)

    def update(self):
        self.slide1.update()
        self.slide2.update()

    def reset_slides(self):
        for slide in self.sprites.sprites():
            slide.moving = False
        self.slide1.rect.right = 600
        self.slide2.rect.right = 1200
        
    def operation(self,event_key):
        if event_key == pygame.K_RIGHT:
            self.slide1.start_animate_to_left(0)
            self.slide2.start_animate_to_left(600)

        elif event_key == pygame.K_LEFT:
            self.slide1.start_animate_to_right(600)
            self.slide2.start_animate_to_right(1200)

        elif event_key == pygame.K_RETURN:
            self.reset_slides()
            return "continue"

class Slide(pygame.sprite.Sprite):
    def __init__(self,path,posX,posY):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.centerx = posX
        self.rect.centery = posY
        self.moving = False
        self.limit = 0
        self.changeX_rate = 0

    def start_animate_to_left(self,limit):
        self.moving = True
        self.limit = limit
        self.changeX_rate = -30

    def start_animate_to_right(self,limit):
        self.moving = True
        self.limit = limit
        self.changeX_rate = 30

    def update(self):
        if self.moving:
            if self.rect.right != self.limit:
                self.rect.centerx += self.changeX_rate
            else : self.moving = False



        
