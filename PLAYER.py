import pygame,GAME
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/player.png'),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.vector = pygame.math.Vector2()
        self.key = {"left":False,"right":False,"jump":False}

        self.vitesseMax = 200
        self.vitesseMin = 10
        self.acceleration = 5

        self.enSaut = False

    def eventKey(self,keyWord,action):
        self.key[keyWord] = action


    def mouvement(self):
        if not(self.key["right"]) and self.vector.x > 0:
            #déscélération à droite
            if self.vector.x < self.vitesseMin:
                self.vector.x = 0
            else:
                self.vector.x /= 2
        elif not(self.key["left"]) and self.vector.x < 0:
            #déscélération à gauche
            if self.vector.x > -self.vitesseMin:
                self.vector.x = 0
            else:
                self.vector.x /= 2
        elif self.key["right"] and self.vector.x < self.vitesseMax:
            #accélération à droite
            self.vector.x += self.acceleration
        elif self.key["left"] and self.vector.x > -self.vitesseMax:
            #accélération à gauche
            self.vector.x -= self.acceleration

    def jump(self):
        #formule pour le saut.
        pass


    def update(self,allPlateforme):
        #gravité si pas de collision avec une plateforme
        if (pygame.sprite.spritecollideany(self,allPlateforme)==None):
            pass


        #Ici calculer le mouvement gauche droite
        self.mouvement()
        print(self.vector.x)

        #deplacement gauche droite
        self.rect.x = round(self.rect.x + self.vector.x/100)
        self.rect.y += self.vector.y
