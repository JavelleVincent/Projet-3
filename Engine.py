import pygame
from pygame.locals import *
import Land as ld
from Land import *
import Control
from Control import *


class Engine():
	def __init__(self):
		pygame.init()

		self.fenetre_debut = pygame.display.set_mode((600, 100))
		myfont = pygame.font.SysFont("monospace", 15)

		# render text
		label = myfont.render("Pour commencer appuyer sur Espace", 1, (255,255,255))
		self.fenetre_debut.blit(label, (100, 40))
		pygame.display.flip()
		clock = pygame.time.Clock()
		self.cont=True
		
		while self.cont==True:
		    for event in pygame.event.get():
		    	keys_pressed = pygame.key.get_pressed()

		    	if keys_pressed[pygame.K_SPACE]:
		    		self.launch_game()
		    		self.cont=False
		    		pygame.QUIT		    	
		   
		    	clock.tick(60)



		while pygame.event.wait().type != pygame.QUIT: pass

		

	def launch_game(self):
		self.fenetre = pygame.display.set_mode((300, 400))
		land=ld.Land(self.fenetre)
		background=land.background()
		maps=land.map()
		control=Control(maps[0], maps[1], self.fenetre)
		while pygame.event.wait().type != pygame.QUIT: pass

 
