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
                            ('assets/backgroundLevel0.png',0,[PLATEFORME.Plateforme(0,245,65,230),PLATEFORME.Plateforme(0,480,1000,1)],[DOOR.Door('Left',0,30,85,1,(31,0))]),#Level 0
                            ('assets/backgroundLevel1.png',1,[PLATEFORME.Plateforme(0,425,1000,1),PLATEFORME.Plateforme(0,185,1000,1)],[DOOR.Door('Right',100,10,85,0,(939,20))]),#Level 1
                          ]
        

    def titleScreen(self,screen):
        #Variables pour la mise en place du menu de l'écran titre
        done = False
        index = 0
        time = pygame.time.get_ticks()
        images = [pygame.image.load('assets/titleScreen/titleScreen1.png'),pygame.image.load('assets/titleScreen/titleScreen2.png')]
        image = images[index]
        while not done:
            #Test appui espace pour sortir de la boucle
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        done = True

            #Animation
            if pygame.time.get_ticks()-time>=2000:
                time = pygame.time.get_ticks()
                index = (1+index)%2
                image = images[index]
            screen.blit(image,(0,0))
            pygame.display.flip()

        
    def update(self,screen):
        #Update du player
        self.player.update(self.level.listePlateforme)
        
        #Rajout des projectiles dans les éléments à dessiner
        self.allSprites.add(self.player.allProjectile)
        
        #Test collision pour le changement de niveau
        numDoorCollided = self.player.rect.collidelist(self.level.listeDoor)
        if numDoorCollided != -1:
            doorCollided = self.level.listeDoor[numDoorCollided]
            self.changeLevel(doorCollided.destination,numDoorCollided,screen)

    def changeLevel(self,numberLevel,numDoorCollided,screen):
        self.level = LEVEL.Level(*self.listeLevel[numberLevel])
        
        #Actualisation de la position du joueur quand il prend une porte
        doorDestination = self.level.listeDoor[numDoorCollided]
        if numDoorCollided != -1:
            (self.player.rect.x,self.player.rect.y) = doorDestination.coordPlayer

        screen.blit(self.level.background,(0,0))
        pygame.display.flip()