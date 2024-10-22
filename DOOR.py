import pygame
class Door():
    """Classe permettant la création de portes"""
    def __init__(self,LeftOrRight,y,width,height,destination,coordPlayer,isPlayerCrouching,screenWidth):
        #Mur sur lequelle la porte se trouve
        if LeftOrRight == 'Left':
            x = 0
        elif LeftOrRight == 'Right':
            x = screenWidth - width
        #Son rectangle de collision
        self.rect = pygame.Rect(x,y,width,height)
        #Son niveau de destination
        self.destination = destination
        #Coordonnees auquelles le joueur sera mis lorsque il passera dans l'autre niveau
        self.coordPlayer = coordPlayer
        #Est-ce que le joueur devra s'accroupir pour aller à travers la porte
        self.isPlayerCrouching = isPlayerCrouching
