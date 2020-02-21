import pygame
class Level():
    def __init__(self,width,height,backgroundAdress,number,listePlateforme,listeDoor):
        self.width = width
        self.height = height
        self.listePlateforme = pygame.sprite.Group()
        for plateforme in listePlateforme:
            self.listePlateforme.add(plateforme)
        self.listeDoor = pygame.sprite.Group()
        for door in listeDoor:
            self.listeDoor.add(door)
        if backgroundAdress != None:
            self.background = pygame.transform.scale(pygame.image.load(backgroundAdress),(self.width,self.height))
        self.number = number
