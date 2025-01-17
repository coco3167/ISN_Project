import pygame

class Projectile(pygame.sprite.Sprite):
    """Classe permettant la création de projectiles pour le joueur"""
    def __init__(self,x,y,sens):
        super().__init__()

        #Vitesse pour son déplacement dans l'espace
        self.velocity = 5

        #Son image
        self.image = pygame.image.load('assets/projectile.png')

        #Son rectangle de collision
        self.rect = self.image.get_rect()
        self.sens = sens
        self.rect.y,self.rect.x = y + 75,x + 50*self.sens - 10

    def update(self):
        #Déplacement du projectile
        self.rect.x += self.velocity*self.sens

        #Supression du projectile s'il sort de l'écran
        if self.rect.x > 1000 or self.rect.x < 0-self.rect.width:
            self.kill()
