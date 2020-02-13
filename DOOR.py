import pygame
class Door(pygame.sprite.Sprite):
    def __init__(self,LeftOrRight,y,destination):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/door.png'),(60,60))#20*20
        self.rect = self.image.get_rect()
        if LeftOrRight == 'Left':
            self.rect.x = 0
        elif LeftOrRight == 'Right':
            self.rect.x = 940
            self.image = pygame.transform.flip(self.image,True,False)
        self.rect.y = y
        self.destination = destination
