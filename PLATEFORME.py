import pygame
class Plateforme(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/plateforme.png'),(800,20))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
