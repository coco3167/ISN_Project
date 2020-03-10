import pygame
class Plateforme():
	"""Classe permettant la création de plateformes"""
	def __init__(self,x,y,width,height):
		#Son rectangle de collision
		self.rect = pygame.Rect(x,y,width,height)
