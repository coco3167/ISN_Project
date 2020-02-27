import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,sens):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('assets/projectile.png')
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y,self.sens = x,y,sens

    def update(self):
        self.rect.x += self.velocity*self.sens
        print(self.rect.x)
        if self.rect.x > 1000 or self.rect.x < 0-self.rect.width:
            self.kill()