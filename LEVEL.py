import pygame
class Level():
    def __init__(self,width,height,background,number,listePlateforme,listeDoor):
        self.width = width
        self.height = height
        self.listePlateforme = pygame.sprite.Group()
        for plateforme in listePlateforme:
            self.listePlateforme.add(plateforme)
        self.listeDoor = pygame.sprite.Group()
        for door in listeDoor:
            self.listeDoor.add(door)
        self.background = background
        self.number = number
