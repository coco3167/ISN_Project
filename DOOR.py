import pygame
class Door(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/door.png'),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.destination = destination