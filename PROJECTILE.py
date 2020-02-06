import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 132
        self.image = pygame.image.load('assets/index.jpeg')
        self.rect = self.image.get_rect()
