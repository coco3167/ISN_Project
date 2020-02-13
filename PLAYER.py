import pygame,GAME,PROJECTILE
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Variable pour l'animation
        self.time = pygame.time.get_ticks()
        self.images = (
                        pygame.transform.scale(pygame.image.load('assets/player/player1.png'),(51,163)),#width = 3*17
                        pygame.transform.scale(pygame.image.load('assets/player/player2.png'),(51,163)),#height = 3*54
                      )
        self.imageIndex = 0
        self.image = self.images[self.imageIndex]

        #Variable pour la position et le mouvement
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.vector = pygame.math.Vector2()
        self.key = {"left":False,"right":False,"jump":False}
        self.listeCollided = []

        #Variables pour le deplacement gauche droite
        self.vitesseMax = 200
        self.vitesseMin = 10
        self.acceleration = 5
        self.weightLeftRight = 2

        #Variables pour le saut
        self.isJumping = False
        self.onPlateforme = False
        self.t = 0
        self.vitesseAccelerationSaut = 85 #b
        self.vitesseDescelerationSaut = 12 #a
        self.hauteurMaxSaut = -self.vitesseAccelerationSaut/(2*-self.vitesseDescelerationSaut) #-b/2a
        self.gravite = 150
        self.accelerationGravite = 5
        self.allProjectile = pygame.sprite.Group()


    def eventKey(self,keyWord,action):
        self.key[keyWord] = action


    def mouvement(self):
        if not(self.key["right"]) and self.vector.x > 0:
            #déscélération à droite
            if self.vector.x < self.vitesseMin:
                self.vector.x = 0
            else:
                self.vector.x /= self.weightLeftRight
        elif not(self.key["left"]) and self.vector.x < 0:
            #déscélération à gauche
            if self.vector.x > -self.vitesseMin:
                self.vector.x = 0
            else:
                self.vector.x /= self.weightLeftRight
        elif self.key["right"] and self.vector.x < self.vitesseMax:
            #accélération à droite
            self.vector.x += self.acceleration
        elif self.key["left"] and self.vector.x > -self.vitesseMax:
            #accélération à gauche
            self.vector.x -= self.acceleration

    def jump(self):
        #formule pour le saut.
        if self.t < self.hauteurMaxSaut:
            self.t += 1
            self.vector.y -= -self.vitesseDescelerationSaut*self.t*self.t + self.vitesseAccelerationSaut*self.t
        else:
            self.isJumping = False
            self.t = 0

    def launchProjectile(self):
        self.allProjectile.add(Projectile())

    def inertie(self):
        #Quand il tombe
        if self.vector.y > self.gravite-self.accelerationGravite:
            self.vector.y = self.gravite
        else:
            self.vector.y += self.accelerationGravite


    def collisionLeftRight(self,allPlateforme):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 1000-self.rect.width:
            self.rect.x = 1000-self.rect.width
        self.listeCollided = pygame.sprite.spritecollide(self,allPlateforme,False)
        for plateforme in self.listeCollided:
            if self.vector.x > 0:
                self.rect.x = plateforme.rect.x - self.rect.width
            elif self.vector.x < 0:
                self.rect.x = plateforme.rect.x + plateforme.rect.width

    def collisionUpBottom(self,allPlateforme):
        self.listeCollided = pygame.sprite.spritecollide(self,allPlateforme,False)
        if self.listeCollided == []:
            self.onPlateforme = False
        else:
            for plateforme in self.listeCollided:
                if self.vector.y > 0:
                    self.rect.y = plateforme.rect.y - self.rect.height
                    self.onPlateforme = True
                elif self.vector.y < 0:
                    self.rect.y = plateforme.rect.y + plateforme.rect.height
                    self.isJumping = False
                    self.t = 0
                    self.vector.y = 0


    def update(self,allPlateforme):

        #Déplacement plus lourd (lent) si en l'air
        if not(self.onPlateforme):
            self.weightLeftRight = 1.5

        #Calcul du vecteur y en fonction de son état et détection d'un saut.
        if not(self.onPlateforme):
            if self.isJumping:
                self.jump()
            else:
                self.inertie()
        else:
            #Saut à la prochaine actualisation
            self.isJumping = self.key["jump"]
            if self.isJumping:
                self.onPlateforme = False
            self.vector.y = 0
        self.rect.y = round(self.rect.y + self.vector.y/100)

        #Test des collisions
        self.collisionUpBottom(allPlateforme)

        #Ici calcul du mouvement et de la collision gauche droite
        self.mouvement()
        self.rect.x = round(self.rect.x + self.vector.x/100)
        self.collisionLeftRight(allPlateforme)

        #Idle animation
        if self.vector.x != 0:
            self.time = pygame.time.get_ticks()
            self.imageIndex = 0
        elif pygame.time.get_ticks()-self.time>=1000: #Temps avant un changement de frame
            self.imageIndex = (self.imageIndex+1)%2 #pour pas dépasser l'index
            self.time = pygame.time.get_ticks()
        self.image = self.images[self.imageIndex]