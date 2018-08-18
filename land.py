import pygame
from pygame.locals import *
 
pygame.init()
fenetre = pygame.display.set_mode((300, 300))

class Land:

	tab_land={}

	def __init__(self, fenetre):
		self.fenetre=fenetre
	

	def background(self):
		#create background 15*15
		fond = pygame.image.load("ressource/floor.png").convert()
		i=0
		for x in range(15):
			j=0
			for y in range(15):
				self.fenetre.blit(fond, (i*20,j*20))
				j+=1
			i+=1

	def map(self):
		## Map in tab
		with open("land.txt", "r") as f:
			i=0
			for line in f.readlines():
				j=0
				for x in range(15):
					self.tab_land[(i,j)]=line[x]
					if line[x]=='S':
						character=Character(self.fenetre)
						mcgiver=character.macgiver(j,i)
						position_mg=[j,i]
					if line[x]=='E':
						characters=Character(self.fenetre)
						guard=characters.guardian(j,i)
						self.guard_position=(j,i)
					if line[x]=='W':
						walls=Character(self.fenetre).walls(j,i)
					j+=1
					
				i+=1
		
		print(self.tab_land)
		return position_mg



		


#########################################################
class Character():
	def __init__(self, fenetre):
		self.fenetre=fenetre
		self.mcgiver=pygame.image.load("ressource/MacGyver.png").convert()
		self.mcgiver=pygame.transform.scale(self.mcgiver, (20, 20))
		self.guard=pygame.image.load("ressource/Gardien.png").convert()
		self.guard=pygame.transform.scale(self.guard, (20, 20))
		self.wall=pygame.image.load("ressource/wall.png").convert()
		self.wall=pygame.transform.scale(self.wall, (20, 20))

	def macgiver(self, x,y):
		self.fenetre.blit(self.mcgiver, (x*20,y*20))
		pygame.display.flip()

	def guardian(self, x,y):
		self.fenetre.blit(self.guard, (x*20,y*20))
		pygame.display.flip()

	def walls(self, x,y):
		self.fenetre.blit(self.wall, (x*20,y*20))
		pygame.display.flip()


##########################################################
class Control():
	cont=1
##define all controls
	def __init__(self,x,y, fenetre):
		self.x=x
		self.y=y
		self.fenetre=fenetre
		self.tab_land=Land(self.fenetre).tab_land

		clock = pygame.time.Clock()
		
		while self.cont==1:
		    for event in pygame.event.get():
		    	keys_pressed = pygame.key.get_pressed()
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
		if self.x==14:
			pass
		elif self.tab_land[(self.y,self.x+1)]=="W":
			pass
		else:
			fond = pygame.image.load("ressource/floor.png").convert()
			self.fenetre.blit(fond, (self.x*20,self.y*20))
			char=Character(self.fenetre)
			move=char.macgiver(self.x+1,self.y)
			self.x=self.x+1
			end_condition=Event(self.fenetre, self.x,self.y).end_game()
			if end_condition==False:
				self.cont=0
			



	def left(self):
		if self.x==0:
			pass
		elif self.tab_land[(self.y,self.x-1)]=="W":
			pass
		else:
			fond = pygame.image.load("ressource/floor.png").convert()
			self.fenetre.blit(fond, (self.x*20,self.y*20))
			char=Character(self.fenetre)
			move=char.macgiver(self.x-1,self.y)
			self.x=self.x-1
			end_condition=Event(self.fenetre, self.x,self.y).end_game()
			if end_condition==False:
				self.cont=0

	def up(self):
		if self.y==0:
			pass
		elif self.tab_land[(self.y-1,self.x)]=="W":
			pass
		else:
			fond = pygame.image.load("ressource/floor.png").convert()
			self.fenetre.blit(fond, (self.x*20,self.y*20))
			char=Character(self.fenetre)
			move=char.macgiver(self.x,self.y-1)
			self.y=self.y-1
			end_condition=Event(self.fenetre, self.x,self.y).end_game()
			if end_condition==False:
				self.cont=0

	def down(self):
		if self.y==14:
			pass
		elif self.tab_land[(self.y+1,self.x)]=="W":
			pass
		else:
			fond = pygame.image.load("ressource/floor.png").convert()
			self.fenetre.blit(fond, (self.x*20,self.y*20))
			char=Character(self.fenetre)
			move=char.macgiver(self.x,self.y+1)
			self.y=self.y+1
			end_condition=Event(self.fenetre, self.x,self.y).end_game()
			if end_condition==False:
				self.cont=0


#############################
class Event():

	def __init__(self, fenetre,x,y):
		self.fenetre=fenetre
		self.x=x
		self.y=y

	def end_game(self):
		tab_land=Land(self.fenetre).tab_land
		position_guard=list(tab_land.keys())[list(tab_land.values()).index("E")]
		if position_guard[0]==self.y and position_guard[1]==self.x:
			print("STOP")
			return False

land=Land(fenetre)
background=land.background()
map=land.map()
control=Control(map[0], map[1], fenetre)


while pygame.event.wait().type != pygame.QUIT: pass