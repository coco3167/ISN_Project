import pygame
class Plateforme(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)