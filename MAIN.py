#Licence cc
import pygame,GAME
pygame.init()

#Initialisation de la fenêtre
pygame.display.set_caption("Alpha")
screenWidth = 1000
screen = pygame.display.set_mode((screenWidth,500))#,pygame.FULLSCREEN)

#Constantes
WHITE = (255,255,255)

#Variable pour sortir de la boucle quand la fenêtre est fermée
done = False

#Création des objets du jeu
game = GAME.Game(screenWidth)
game.titleScreen(screen)
game.changeLevel(0,-1,screen)

#On apprend au joueur les touches
game.tutorial(screen)

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
    if game.player.life>0:  #Affichage de la vie en temps réel (peut-être remplacer le texte par une barre
        game.HUDRender(screen)

    #Actualisation de l'écran
    pygame.display.flip()

    #Réinitialisation du jeu quand le joueur meurt
    if game.gameIsOver:
        game = GAME.Game(screenWidth)
        game.titleScreen(screen)
        game.changeLevel(0,-1,screen)

#Fermeture du programme
pygame.quit()
