import pygame
class Plateforme(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/plateforme.png'),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
