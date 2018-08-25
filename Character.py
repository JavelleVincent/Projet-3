import pygame
from pygame.locals import *
import Event as ev

class Character():
	def __init__(self, fenetre):
		self.fenetre=fenetre
		self.mcgiver=pygame.image.load("ressource/MacGyver.png").convert()
		self.mcgiver=pygame.transform.scale(self.mcgiver, (20, 20))
		self.guard=pygame.image.load("ressource/Gardien.png").convert()
		self.guard=pygame.transform.scale(self.guard, (20, 20))
		

	def macgiver(self, x,y):
		self.fenetre.blit(self.mcgiver, (x*20,y*20))
		pygame.display.flip()

	def guardian(self, x,y):
		self.fenetre.blit(self.guard, (x*20,y*20))
		pygame.display.flip()

	
