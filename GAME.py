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
        #Matrice avec toutes les plateforme selon les niveaux
        self.listeLevel = [
                            (1000,800,None,0,[PLATEFORME.Plateforme(100,680,800,20)]),#Level 0
                            (1000,800,None,1,[PLATEFORME.Plateforme(0,780,1000,20),PLATEFORME.Plateforme(50,600,900,20)]),#Level 1
                            ]

    def changeLevel(self,numberLevel):
        #Retirement des sprites de l'ancien niveau
        try:
            self.allSprites.remove(self.level.listePlateforme)
        except:
            pass
        self.level = LEVEL.Level(*self.listeLevel[numberLevel])
        #Ajout des sprites du niveau aux sprites généraux
        self.allSprites.add(self.level.listePlateforme)
