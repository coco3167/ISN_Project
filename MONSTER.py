import pygame
class Monster(pygame.sprite.Sprite):
    """Classe permettant la création d'ennemies"""
    def __init__(self,position):
        super().__init__()
       
        #Variables pour l'animation
        self.time = pygame.time.get_ticks()
        self.images = (
                        (pygame.image.load('assets/monster/monster1.png')),
                        (pygame.image.load('assets/monster/monster2.png')),
                      )
        self.imageIndex = 0
        self.image = self.images[self.imageIndex]

        #Variable pour la position et le rectangle de collision
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = position

        #Variable pour la vie
        self.life = 30

    def update(self):
        #Idle animation
        if pygame.time.get_ticks()-self.time>=500:
            self.imageIndex = (self.imageIndex + 1)%2
            self.time = pygame.time.get_ticks()
        self.image = self.images[self.imageIndex]