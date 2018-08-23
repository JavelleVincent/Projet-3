import pygame
from pygame.locals import *
import land as ld
import character as ch
import Event as ev
class Control():
	cont=True
##define all controls
	def __init__(self,x,y, fenetre):
		self.x=x
		self.y=y
		self.fenetre=fenetre
		self.tab_land=ld.Land(self.fenetre).tab_land

		clock = pygame.time.Clock()
		
		while self.cont==True:
		    for event in pygame.event.get():
		    	keys_pressed = pygame.key.get_pressed()

		    	if keys_pressed[pygame.K_ESCAPE]:
		    		pygame.quit()
		    		#a modif
		    	if keys_pressed[pygame.K_LEFT]:
		        	self.left()
		    	if keys_pressed[pygame.K_RIGHT]:
		        	self.right()
		    	if keys_pressed[pygame.K_UP]:
		        	self.up()
		    	if keys_pressed[pygame.K_DOWN]:
		        	self.down()	
		        		
		    	clock.tick(60)



	def right(self):
		if self.x>=14:
			pass
		elif self.tab_land[(self.y,self.x+1)]=="W":
			pass
		else:
			fond = pygame.image.load("ressource/floor.png").convert()
			self.fenetre.blit(fond, (self.x*20,self.y*20))
			char=ch.Character(self.fenetre)
			move=char.macgiver(self.x+1,self.y)
			self.x=self.x+1
			check_object=ev.Event(self.fenetre, self.x,self.y).check_object()
			end_condition=ev.Event(self.fenetre, self.x,self.y).end_game()
			if end_condition==False:
				self.cont=False
			



	def left(self):
		if self.x<=0:
			pass
		elif self.tab_land[(self.y,self.x-1)]=="W":
			pass
		else:
			fond = pygame.image.load("ressource/floor.png").convert()
			self.fenetre.blit(fond, (self.x*20,self.y*20))
			char=ch.Character(self.fenetre)
			move=char.macgiver(self.x-1,self.y)
			self.x=self.x-1
			check_object=ev.Event(self.fenetre, self.x,self.y).check_object()
			end_condition=ev.Event(self.fenetre, self.x,self.y).end_game()
			if end_condition==False:
				self.cont=False

	def up(self):
		if self.y<=0:
			pass
		elif self.tab_land[(self.y-1,self.x)]=="W":
			pass
		else:
			fond = pygame.image.load("ressource/floor.png").convert()
			self.fenetre.blit(fond, (self.x*20,self.y*20))
			char=ch.Character(self.fenetre)
			move=char.macgiver(self.x,self.y-1)
			self.y=self.y-1
			check_object=ev.Event(self.fenetre, self.x,self.y).check_object()
			end_condition=ev.Event(self.fenetre, self.x,self.y).end_game()
			if end_condition==False:
				self.cont=False

	def down(self):
		if self.y>=14:
			pass
		elif self.tab_land[(self.y+1,self.x)]=="W":
			pass
		else:
			fond = pygame.image.load("ressource/floor.png").convert()
			self.fenetre.blit(fond, (self.x*20,self.y*20))
			char=ch.Character(self.fenetre)
			move=char.macgiver(self.x,self.y+1)
			self.y=self.y+1
			check_object=ev.Event(self.fenetre, self.x,self.y).check_object()
			end_condition=ev.Event(self.fenetre, self.x,self.y).end_game()
			if end_condition==False:
				self.cont=False
