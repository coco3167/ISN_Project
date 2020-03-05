import pygame
class Plateforme():
    def __init__(self,x,y,width,height):
		#Son rectangle de collision
        self.rect = pygame.Rect(x,y,width,height)
