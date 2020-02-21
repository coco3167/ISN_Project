import PLAYER,PLATEFORME,LEVEL,DOOR,pygame
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
                            (1600,800,'assets/backgroundLevel0.png',0,[PLATEFORME.Plateforme(100,680,800,20)],[DOOR.Door('Left',220,1)]),#Level 0
                            (1000,800,None,1,[PLATEFORME.Plateforme(0,780,1000,20),PLATEFORME.Plateforme(100,550,800,20)],[DOOR.Door('Right',190,0)]),#Level 1
                          ]

    def update(self):
        self.player.update(self.level.listePlateforme)
        self.level.update(self.player)
        doorCollided = pygame.sprite.spritecollide(self.player,self.level.listeDoor,False)
        if doorCollided != []:
            self.changeLevel(doorCollided[0].destination)

    def changeLevel(self,numberLevel):
        #Retirement des sprites de l'ancien niveau
        try:
            self.allSprites.remove(self.level.listePlateforme,self.level.listeDoor)
        except:
            pass
        self.level = LEVEL.Level(*self.listeLevel[numberLevel])
        #Ajout des sprites du niveau aux sprites généraux
        self.allSprites.add(self.level.listePlateforme,self.level.listeDoor)
