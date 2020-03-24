import pygame,MONSTER
class Level():
    """Classe permettant la création de niveaux"""
    def __init__(self,backgroundAdress,number,listePlateforme,listeDoor,listePositionMonsters):
        self.listePlateforme = listePlateforme
        self.listeDoor = listeDoor
        self.background = pygame.image.load(backgroundAdress)
        self.number = number
        
        #Création des monstres du niveau
        self.listeMonster = pygame.sprite.Group()
        for position in listePositionMonsters:
            self.listeMonster.add(MONSTER.Monster(position))