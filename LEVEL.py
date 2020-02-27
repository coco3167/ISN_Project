import pygame
class Level():
    def __init__(self,backgroundAdress,number,listePlateforme,listeDoor):
        self.listePlateforme = listePlateforme
        self.listeDoor = listeDoor
        self.background = pygame.image.load(backgroundAdress)
        self.number = number