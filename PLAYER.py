import pygame,GAME,PROJECTILE
class Player(pygame.sprite.Sprite):
    """Classe permettant de créer et gêrer les comportements du joueur"""
    def __init__(self,screenWidth):
        super().__init__()

        #Mise en place de l'animation
        self.time = pygame.time.get_ticks()
        self.shootTime = 0
        self.images = {
                        "Idle Animation" : [pygame.image.load('assets/player/player_idle_1.png'),pygame.image.load('assets/player/player_idle_2.png'),],
                        "Walk Animation" : [pygame.image.load('assets/player/player_walk_1.png'),pygame.image.load('assets/player/player_walk_2.png'),],
                        "Jump Animation" : [pygame.image.load('assets/player/player_jump.png'),],
                        "Crouch Animation" : [pygame.image.load('assets/player/player_crouch_1.png'),pygame.image.load('assets/player/player_crouch_2.png'),pygame.image.load('assets/player/player_crouch_3.png'),],
                        "Shoot Animation" : [pygame.image.load('assets/player/player_shoot.png'),],
                    }

        #Redimensionnement des images
        listeRedimensionnements = {
                                    "Idle Animation" : (57,171),
                                    "Walk Animation" : (66,171),
                                    "Jump Animation" : (138,147),
                                    "Crouch Animation" : (168,96),
                                    "Shoot Animation" : (78,171),
                                   }
        for keys,animations in self.images.items():
            for loop in range(len(animations)):
                self.images[keys][loop] = pygame.transform.scale(self.images[keys][loop],listeRedimensionnements[keys])

        #Ajout d'éléments après coup pour éviter un problème de redimensionnement (pas les mêmes dimensions)
        self.images["Walk Animation"].insert(1,self.images["Jump Animation"][0])
        self.images["Walk Animation"].insert(3,self.images["Jump Animation"][0])

        #Quelques variables pour l'animation
        self.imageIndex = 0
        self.imageAnimation = "Idle Animation"
        self.image = self.images[self.imageAnimation][self.imageIndex]
        self.isCrouching = False

        #Variable pour la vie
        self.life = 99

        #Largeur de l'écran
        self.screenWidth = screenWidth

        #Le sens correspond à si le player regarde à droite ou à gaucherd
        self.sens = 1

        #Variable pour la position et le rectangle de collision
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = 415,480-self.rect.height

        #Variables pour le mouvement
        self.vector = pygame.math.Vector2()
        self.key = {"left":False,"right":False,"jump":False,"shoot":False}
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

    def inertie(self):
        #Quand il tombe
        if self.vector.y > self.gravite-self.accelerationGravite:
            self.vector.y = self.gravite
        else:
            self.vector.y += self.accelerationGravite


    def launchProjectile(self):
        self.allProjectile.add(PROJECTILE.Projectile(self.rect.x + (self.rect.width/2),self.rect.y,self.sens))


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
            if self.vector.y != 0:
                self.onPlateforme = False
        else:
            for plateforme in self.listeCollided:
                if self.vector.y > 0:
                    self.rect.y = plateforme.rect.y - self.rect.height
                    self.onPlateforme = True
                    self.vector.y = 0
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


    def animation(self,imageAnimation,animationTime):
        if self.imageAnimation != imageAnimation:
                self.imageAnimation = imageAnimation
                self.imageIndex = 0
                self.time = pygame.time.get_ticks()
        elif pygame.time.get_ticks()-self.time>=animationTime:   #Temps avant un changement de frame
                self.imageIndex = (self.imageIndex + 1)%len(self.images[imageAnimation])   #Pour ne pas dépasser l'index
                self.time = pygame.time.get_ticks()


    def update(self,allPlateforme,allMonster):
        if pygame.time.get_ticks()-self.shootTime >= 1000:  #Si le joueur tire il ne bouge pas donc cette partie devient inutile
            
            #Calcul du vecteur y en fonction de son état et détection d'un saut.
            if not(self.onPlateforme):
                self.weightLeftRight = 1.5  #Déplacement plus lourd (lent) si en l'air
            
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
            #Débugage : le joueur n'était pas détecté comme n'étant plus sur une plateforme si il n'en sautait pas mais ne faisait que marcher en dehors
            if not(self.isJumping):
                for plateforme in allPlateforme:
                    self.onPlateforme = plateforme.rect.x<self.rect.right and plateforme.rect.right>self.rect.x and self.rect.bottom+1>plateforme.rect.y
                    if self.onPlateforme:
                        break

            #Actualisation du sens du player
            if self.key["right"]:
                self.sens = 1
            elif self.key["left"]:
                self.sens = -1

            #Test de la collision avec des dégats
            self.collisionHurt(allMonster)

            #Animation
            if not(self.onPlateforme):
                self.animation("Jump Animation",0)
            elif self.vector.x != 0:
                self.animation("Walk Animation",250)
            else:
                self.animation("Idle Animation",1000)
        
         #Si le joueur est immobile et qu'il tire, on change l'image
        if self.vector == pygame.math.Vector2() and self.key["shoot"]:
            self.launchProjectile()
            self.imageAnimation,self.imageIndex = "Shoot Animation",0
            self.shootTime = pygame.time.get_ticks()
        self.key["shoot"] = False

        self.image = self.images[self.imageAnimation][self.imageIndex]

        if self.sens != 1:
            self.image = pygame.transform.flip(self.image,True,False)

        #Déplacement des projectiles
        self.allProjectile.update()
      
        print(self.isCrouching)