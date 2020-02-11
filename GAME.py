import PLAYER,PLATEFORME,LEVEL,pygame
class Game():
    def __init__(self):
        #Création d'une liste de tout les sprites
        self.allSprites = pygame.sprite.Group()
        #Création du joueur
        self.player = PLAYER.Player()
        self.allSprites.add(self.player)
        #Musique
        pygame.mixer.music.load('assets/Theme.ogg')
        pygame.mixer.music.play(loops = -1)
        self.level = None

    def level1(self):
        #Retirement des sprites de l'ancien niveau
        try:
            self.allSprites.remove(self.level.listePlateforme)
        except:
            pass
        self.level = LEVEL.Level(1000,800,None,1)
        self.level.listePlateforme.add(PLATEFORME.Plateforme(100,680))
        #Ajout des sprites du niveau aux sprites généraux
        self.allSprites.add(self.level.listePlateforme)
