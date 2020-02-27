import pygame
class Plateforme():
    def __init__(self,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)