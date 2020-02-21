#Licence cc
import pygame,GAME
pygame.init()

#Initialisation de la fenêtre
pygame.display.set_caption("Alpha")
screen = pygame.display.set_mode((1400,700))
#Initialisation des constantes et variables globales
WHITE = (255,255,255)
BLACK = (0,0,0)
done = False

#Création des objets du jeu
game = GAME.Game()
game.changeLevel(0,screen)

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
    #Draw on screen
    screen.fill(WHITE)
    screen.blit(game.level.background,(0,0))
    game.allSprites.draw(screen)
    pygame.display.update(game.player.renderRect) #Il y a moyen d'optimiser avec pygame.display.update si on fait une liste de rectangle ou il faut render uniquement ce dont on a besoin

#Fermeture du programme
pygame.quit()
