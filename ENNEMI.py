import pygame,GAME
class Badboy(pygame.sprite.Sprite):
    """"Classe permettant de créer un ennemi"""
    def __init__(self):
        super().__init__()

        self.apparence = pygame.apparence.load('assets/mechant.jpeg')
