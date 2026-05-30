import pygame
from utils import resource_path
pygame.font.init()
class Monitor(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        super().__init__()
        self.image = pygame.image.load(resource_path('images//monitor.png'))
        self.rect = self.image.get_rect()
        self.rect.centerx = posX
        self.rect.centery = posY
        self.font = pygame.font.SysFont("Fixedsys",25)
        self.text = "-- : --" 
        self.text_color = (225,225,0)
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def change_text(self,text):
        self.text = text
        self.update()

    def reset_monitor(self):
        self.text = "-- : --"
        self.update()

    def update(self):
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
