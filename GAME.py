import PLAYER,PLATEFORME,LEVEL,DOOR,pygame
class Game():
    """Classe permettant de gêrer les différents élements du jeu"""
    def __init__(self,screenWidth):
        #Ajout d'une couleur pour le HUD
        self.color = (249,177,31)
        
        #Ajout des policse pour écricre du texte
        self.HUDFont = pygame.font.SysFont("arial",22)
        self.tutoFont = pygame.font.SysFont("arial",50)
        
        #Création de la variable pour le Game Over
        self.gameIsOver = False

        #Création d'une liste de tout les sprites
        self.allSprites = pygame.sprite.Group()

        #Création du joueur
        self.player = PLAYER.Player(screenWidth)
        self.allSprites.add(self.player)

        #Musique
        pygame.mixer.music.load('assets/Theme.ogg')
        pygame.mixer.music.play(loops = -1)

        #Matrice avec toutes les plateforme selon les niveaux
        self.listeLevel = [
                            ('assets/backgrounds/backgroundLevel0.png',0,[PLATEFORME.Plateforme(0,245,65,230),PLATEFORME.Plateforme(0,480,1000,1)],[DOOR.Door('Left',0,30,85,1,(31,0),screenWidth)],[]),#Level 0
                            ('assets/backgrounds/backgroundLevel1.png',1,[PLATEFORME.Plateforme(0,425,1000,1),PLATEFORME.Plateforme(0,185,1000,1)],[DOOR.Door('Right',100,10,85,0,(939,20),screenWidth)],[(50,60),]),#Level 1
                          ]
        self.level = None


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

            #Animation (1 Frame tous les 2 secondes)
            if pygame.time.get_ticks()-time>=2000:
                time = pygame.time.get_ticks()
                index = (1+index)%2
                image = images[index]
            #Drawing
            screen.blit(image,(0,0))
            pygame.display.flip()

    
    def tutorial(self,screen):
        #Les différentes touches à apprendre
        tutoPhrases = [["Press 'D' to go right",pygame.K_d],["Press 'Q' to go left",pygame.K_a],["Press 'Space' to jump",pygame.K_SPACE]]
        
        for loop in range(3):
            #On affiche le un fond noir pour effacer le message
            screen.fill((0,0,0))
            pygame.display.flip()
            
            #Création d'un évenement vide
            event = pygame.event.Event(0)
            event.key = 0

            #Affichage du texte du tutoriel
            screen.blit(self.tutoFont.render(tutoPhrases[loop][0],False,(255,255,255)),(300,200))
            pygame.display.flip()
            
            #On attend que le joueur appuit sur la touche qui sert à faire l'action décrite dans le jeu
            while event.key != tutoPhrases[loop][1]:
                event = pygame.event.wait()
                if event.type != pygame.KEYDOWN:
                    event = pygame.event.Event(0)
                    event.key = 0

    def update(self,screen):
        if self.player.life <= 0:
            self.gameOver()
        
        #Update du player et des monster
        self.player.update(self.level.listePlateforme,self.level.listeMonster)
        self.level.listeMonster.update(self.player.allProjectile,self.player.rect)

        #Rajout des projectiles dans les éléments à dessiner
        self.allSprites.add(self.player.allProjectile)

        #Test collision pour le changement de niveau
        numDoorCollided = self.player.rect.collidelist(self.level.listeDoor)
        if numDoorCollided != -1:
            doorCollided = self.level.listeDoor[numDoorCollided]
            self.changeLevel(doorCollided.destination,numDoorCollided,screen)

    def changeLevel(self,numberLevel,numDoorCollided,screen):
        if self.level != None:
            self.allSprites.remove(self.level.listeMonster)
        
        #Changement du niveau
        self.level = LEVEL.Level(*self.listeLevel[numberLevel])

        #Ajout des monstres dans les sprites à afficher
        self.allSprites.add(self.level.listeMonster)

        #Actualisation de la position du joueur quand il prend une porte
        doorDestination = self.level.listeDoor[numDoorCollided]
        if numDoorCollided != -1:
            (self.player.rect.x,self.player.rect.y) = doorDestination.coordPlayer

        #Drawing
        screen.blit(self.level.background,(0,0))
        pygame.display.flip()

    def gameOver(self):
        #Fonction permettant de gêrer un Game Over et de redémarrer le jeu si le joueur n'a plus de vie.
        self.gameIsOver = True  #Peut être changer le nom de la variable (pas de meilleur idée pour le moment)

    def HUDRender(self,screen):
        #Rectangle afin d'afficher la vie du joueur
        pygame.draw.rect(screen,self.color,pygame.Rect(40,10,self.player.life,20))
        #Texte en complément
        screen.blit(self.HUDFont.render(str(self.player.life),False,self.color),(55+self.player.life,8))
        