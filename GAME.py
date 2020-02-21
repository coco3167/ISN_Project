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
                            (1400,700,'assets/backgroundLevel0.png',0,[PLATEFORME.Plateforme(0,650,1400,50),PLATEFORME.Plateforme(0,343,91,323)],[DOOR.Door('Left',0,45,120,1)]),#Level 0
                            (1400,700,None,1,[PLATEFORME.Plateforme(0,780,1000,20),PLATEFORME.Plateforme(100,550,800,20)],[DOOR.Door('Right',100,45,120,0)]),#Level 1
                          ]
        

    def update(self,screen):
        self.player.update(self.level.listePlateforme)
        numDoorCollided = self.player.rect.collidelist(self.level.listeDoor)
        if numDoorCollided != -1:
            doorCollided = self.level.listeDoor[numDoorCollided]
            self.changeLevel(doorCollided.destination,screen)

    def changeLevel(self,numberLevel,screen):
        self.level = LEVEL.Level(*self.listeLevel[numberLevel])
        screen.blit(self.level.background,(0,0))
        pygame.display.flip()