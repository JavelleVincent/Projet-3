import pygame
from pygame.locals import *
import land
from land import *
import Control
from Control import *


class Engine():
	def __init__(self):
		pygame.init()
		fenetre = pygame.display.set_mode((300, 400))
		land=Land(fenetre)
		background=land.background()
		map=land.map()
		control=Control(map[0], map[1], fenetre)
		while pygame.event.wait().type != pygame.QUIT: pass
 
lauch=Engine()