import pygame
from pygame.locals import *
import Land as ld

class Event():
	inventory=0

	def __init__(self, fenetre,x,y):
		self.fenetre=fenetre
		self.x=x
		self.y=y
		self.tab_land=ld.Land(self.fenetre).tab_land

	def end_game(self):
		tab_land=ld.Land(self.fenetre).tab_land
		position_guard=list(tab_land.keys())[list(tab_land.values()).index("E")]
		if position_guard[0]==self.y and position_guard[1]==self.x:
			if type(self).inventory==3:
				print("VICTOIRE")

				myfont = pygame.font.SysFont("monospace", 15)
				label = myfont.render("Bravo vous avez gagné !", 1, (255,255,255))
				self.fenetre.blit(label, (20, 150))
				pygame.display.flip()
				


			else:
				print("DEFAITE")
				self.defeat=pygame.image.load("ressource/items.png").convert()
				self.defeat=pygame.transform.scale(self.defeat, (20, 20))
				self.fenetre.blit(self.defeat, (self.x*20,self.y*20))
				pygame.display.flip()

			
			return False

	def check_object(self):
		if self.tab_land[(self.x,self.y)]=="O":
			myfont = pygame.font.SysFont("monospace", 15)
			type(self).inventory=self.inventory+1
			label = myfont.render("Inventaire : {}".format(type(self).inventory), 1, (255,255,255), (0,0,0))
			self.fenetre.blit(label, (80, 350))
			self.tab_land[(self.x,self.y)]="P"
