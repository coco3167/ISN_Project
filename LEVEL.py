import pygame
class Level():
    def __init__(self,width,height,background,number,listePlateforme):
        self.width = width
        self.height = height
        self.listePlateforme = pygame.sprite.Group()
        for plateforme in listePlateforme:
            self.listePlateforme.add(plateforme)
        self.background = background
        self.number = number
