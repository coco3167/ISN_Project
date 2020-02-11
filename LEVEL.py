import pygame
class Level():
    def __init__(self,width,height,background,number):
        self.width = width
        self.height = height
        self.listePlateforme = pygame.sprite.Group()
        self.background = background
        self.number = number
