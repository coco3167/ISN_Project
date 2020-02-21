import pygame
class Level():
    def __init__(self,width,height,backgroundAdress,number,listePlateforme,listeDoor):
        self.width = width
        self.height = height
        self.listePlateforme = listePlateforme
        self.listeDoor = listeDoor
        if backgroundAdress != None:
            self.background = pygame.transform.scale(pygame.image.load(backgroundAdress),(self.width,self.height))
        self.number = number