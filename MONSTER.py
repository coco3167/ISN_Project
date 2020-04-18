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
        self.isFlipp = False

        #Variable pour la position et le rectangle de collision
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = position

        #Variable pour la vie
        self.life = 30

        #Création d'uune image blanche du monster
        self.whiteImage = self.image.copy()
        self.whiteImage.fill((255,255,255),None,pygame.BLEND_MAX)

    def idleAnimation(self,timeLimit):
        if pygame.time.get_ticks()-self.time>=timeLimit:
            self.imageIndex = (self.imageIndex + 1)%2
            self.time = pygame.time.get_ticks()
            self.image = self.images[self.imageIndex]

    def update(self,allProjectile,playerRect):
        #Test collision monster/projectile
        if len(pygame.sprite.spritecollide(self,allProjectile,True)):

            #Le monster est touché par un projectile
            if self.life<=10:
                #Mort du monster
                self.kill()

            else:
                #Le monster perd de la vie
                self.life -= 10
                #Effet visuel pour le montrer au joueur
                self.image = self.whiteImage
                self.time = pygame.time.get_ticks()

        elif self.image == self.whiteImage:
            self.idleAnimation(75)

        else:
            #Mouvement du monstre à partir du moment où il est à moins de 500 pixels ou quand il est blessé
            if abs(self.rect.x-playerRect.x)>500 and self.life == 30:
                #Idle animation
                self.idleAnimation(500)
            else:
                #Mouvement du monstre vers le joueur avec l'image dans le bon sens vers le joueur
                if self.rect.x<playerRect.x:
                    self.rect.x += 2
                    if not self.isFlipp:
                        self.image = pygame.transform.flip(self.image,True,False)
                        self.isFlipp = True
                else:
                    self.rect.x -= 2
                    if self.isFlipp:
                        self.image = pygame.transform.flip(self.image,True,False)
                        self.isFlipp = False