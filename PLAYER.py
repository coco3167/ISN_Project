import pygame,GAME,PROJECTILE
class Player(pygame.sprite.Sprite):
    """Classe permettant de créer et gêrer les comportements du joueur"""
    def __init__(self,screenWidth):
        super().__init__()

        #Variable pour l'animation
        self.time = pygame.time.get_ticks()
        self.images = (
                        (pygame.image.load('assets/player/player1.png')),
                        (pygame.image.load('assets/player/player2.png')),
                      )
        self.imageIndex = 0
        self.image = self.images[self.imageIndex]

        #Variable pour la vie
        self.life = 99

        #Largeur de l'écran
        self.screenWidth = screenWidth

        #Le sens correspond à si le player regarde à droite ou à gauche
        self.sens = 1

        #Variable pour la position et le rectangle de collision
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = 415,200

        #Variables pour le mouvement
        self.vector = pygame.math.Vector2()
        self.key = {"left":False,"right":False,"jump":False}
        self.listeCollided = []

        #Variables pour le deplacement gauche droite
        self.vitesseMax = 300
        self.vitesseMin = 10
        self.acceleration = 10
        self.weightLeftRight = 2

        #Variables pour le saut
        self.isJumping = False
        self.onPlateforme = False
        self.t = 0
        self.vitesseAccelerationSaut = 111 #b
        self.vitesseDescelerationSaut = 15 #a
        self.hauteurMaxSaut = -self.vitesseAccelerationSaut/(2*-self.vitesseDescelerationSaut) #-b/2a
        self.gravite = 300
        self.accelerationGravite = 10

        #Groupe pour stocker les projectiles
        self.allProjectile = pygame.sprite.Group()


    def eventKey(self,keyWord,action):
        #Permet de détecter comment sont les différentes touches
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
        self.allProjectile.add(PROJECTILE.Projectile(self.rect.x + (self.rect.width/2),self.rect.y,self.sens))

    def inertie(self):
        #Quand il tombe
        if self.vector.y > self.gravite-self.accelerationGravite:
            self.vector.y = self.gravite
        else:
            self.vector.y += self.accelerationGravite


    def collisionLeftRight(self,allPlateforme):
        #On teste les collisions à gauche et à droite puis on déplace le joueur à l'endroit requis si il est en collision avec une plateforme
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > self.screenWidth-self.rect.width:
            self.rect.x = self.screenWidth-self.rect.width
        self.listeCollided = pygame.sprite.spritecollide(self,allPlateforme,False)
        for plateforme in self.listeCollided:
            if self.vector.x > 0:
                self.rect.x = plateforme.rect.x - self.rect.width
            elif self.vector.x < 0:
                self.rect.x = plateforme.rect.x + plateforme.rect.width

    def collisionUpBottom(self,allPlateforme):
        #On teste les collisions en haut et en bas puis on déplace le joueur à l'endroit requis si il est en collision avec une plateforme (+ on test s'il est sur une plateforme pour pouvoir dire s'il peut sauter
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

    def collisionHurt(self,allMonster):
        #Fonction pour tester la collision avec ce qui fait des dégats et les appliquer s'il y en a.
        listeMonsterCollided = pygame.sprite.spritecollide(self,allMonster,False)
        if listeMonsterCollided != []:
            monsterCollided = listeMonsterCollided[0]
            self.life -= 10
            if monsterCollided.rect.x < self.rect.x:  #On décale le joueur pour qu'il ne se soit pas tapé en boucle.
                self.rect.x += 100
            else:
                self.rect.x -= 100


    def update(self,allPlateforme,allMonster):
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

        #Actualisation du sens du player
        if self.key["right"]:
            self.sens = 1
        elif self.key["left"]:
            self.sens = -1

        #Test de la collision avec des dégats
        self.collisionHurt(allMonster)

        #Idle animation
        if self.vector.x != 0:
            self.time = pygame.time.get_ticks()
            self.imageIndex = 0
        elif pygame.time.get_ticks()-self.time>=1000: #Temps avant un changement de frame de 1 seconde
            self.imageIndex = (self.imageIndex + 1)%2 #Pour pas dépasser l'index
            self.time = pygame.time.get_ticks()
        self.image = self.images[self.imageIndex]

        if self.sens != 1:
            self.image = pygame.transform.flip(self.image,True,False)

        #Déplacement des projectiles
        self.allProjectile.update()