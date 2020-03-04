import pygame
class Door():
    def __init__(self,LeftOrRight,y,width,height,destination,coordPlayer):
        if LeftOrRight == 'Left':
            x = 0
        elif LeftOrRight == 'Right':
            x = 1000-width
        self.rect = pygame.Rect(x,y,width,height)
        self.destination = destination
        self.coordPlayer = coordPlayer
