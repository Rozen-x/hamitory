import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self,path,posX,posY,text=""):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.centerx = posX
        self.rect.centery = posY
        self.font = pygame.font.SysFont("Comic Sans MS",18)
        self.text = text
        self.text_color = (0,0,0)
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.activation = True
        self.pressed = False
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self,mouse_pos):
        return self.rect.collidepoint(mouse_pos)