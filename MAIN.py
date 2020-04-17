#Licence cc
import pygame,GAME
pygame.init()

#Initialisation de la fenêtre
pygame.display.set_caption("Alpha")
screenWidth = 1000
screen = pygame.display.set_mode((screenWidth,500))#,pygame.FULLSCREEN)
#Initialisation des constantes et variables globales
WHITE = (255,255,255)#utile ?
BLACK = (0,0,0)#utile ?
done = False

#Création des objets du jeu
game = GAME.Game(screenWidth)
game.titleScreen(screen)
game.changeLevel(0,-1,screen)

#Boucle principale
while not done:
    #Input du joueur
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Test si une touche est appuyé
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:		# 'a' pour windows et 'q' pour linux
                game.player.eventKey("left",True)
            elif event.key == pygame.K_d:
                game.player.eventKey("right",True)
            elif event.key == pygame.K_SPACE:
                game.player.eventKey("jump",True)
            elif event.key == pygame.K_BACKSPACE:
                game.player.launchProjectile()
        #Test si une touche est relaché
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                game.player.eventKey("left",False)
            elif event.key == pygame.K_d:
                game.player.eventKey("right",False)
            elif event.key == pygame.K_SPACE:
                game.player.eventKey("jump",False)

    #Game Logic
    game.update(screen)
    #Drawing
    screen.fill(WHITE)
        #Background
    screen.blit(game.level.background,(0,0))
        #Foreground
    game.allSprites.draw(screen)
        #HUD

    #Actualisation de l'écran
    pygame.display.flip()

    if game.gameIsOver:
        game = GAME.Game(screenWidth)
        game.titleScreen(screen)
        game.changeLevel(0,-1,screen)

#Fermeture du programme
pygame.quit()
