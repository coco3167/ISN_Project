import PLAYER,PLATEFORME,pygame
class Game():
    def __init__(self):
        #Création d'une liste de tout les sprites
        self.allSprites = pygame.sprite.Group()
        #Création du joueur
        self.player = PLAYER.Player()
        self.allSprites.add(self.player)
        #Création d'une liste de toute les plateformes et ajout d'une plateforme
        self.allPlateforme = pygame.sprite.Group()
        self.allPlateforme.add(PLATEFORME.Plateforme(100,780))
        self.allSprites.add(self.allPlateforme)
