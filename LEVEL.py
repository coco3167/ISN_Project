import pygame
class Level():
    """Classe permettant la création de niveaux"""
    def __init__(self,backgroundAdress,number,listePlateforme,listeDoor):
        self.listePlateforme = listePlateforme
        self.listeDoor = listeDoor
        self.background = pygame.image.load(backgroundAdress)
        self.number = number
