import pygame
class Door():
    def __init__(self,LeftOrRight,y,width,height,destination):
        if LeftOrRight == 'Left':
            x = 0
        elif LeftOrRight == 'Right':
            x = 940
        self.rect = pygame.Rect(x,y,width,height)
        self.destination = destination
