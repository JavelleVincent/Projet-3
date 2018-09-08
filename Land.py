import random
import pygame
from pygame.locals import *
import Character
from Character import *

class Land:
    """
        Initialize land
    """
    tab_land = {}
    path_array = []

    def __init__(self, window):
        self.window = window
        self.ether = pygame.image.load("ressource/ether.png").convert()
        self.ether = pygame.transform.scale(self.ether, (20, 20))
        self.seringue = pygame.image.load("ressource/seringue.png").convert()
        self.seringue = pygame.transform.scale(self.seringue, (20, 20))
        self.aiguille = pygame.image.load("ressource/aiguille.png").convert()
        self.aiguille = pygame.transform.scale(self.aiguille, (20, 20))
        self.wall = pygame.image.load("ressource/wall.png").convert()
        self.wall = pygame.transform.scale(self.wall, (20, 20))

    def background(self):
        """
            Display background
        """
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Inventaire : ", 1, (255, 255, 255))
        self.window.blit(label, (20, 350))
        fond = pygame.image.load("ressource/floor.png").convert()
        i = 0
        for x in range(15):
            j = 0
            for y in range(15):
                self.window.blit(fond, (i*20, j*20))
                j += 1
            i += 1

    def map(self):
        """
            Create map
        """        
        with open("land.txt", "r") as f:
            i = 0
            for line in f.readlines():
                j = 0
                for x in range(15):
                    self.tab_land[(i, j)] = line[x]
                    if line[x] == 'S':
                        character = Character(self.window)
                        character.macgiver(j, i)
                        position_mg = [j, i]
                    if line[x] == 'E':
                        characters = Character(self.window)
                        characters.guardian(j, i)
                        self.guard_position = (j, i)
                    if line[x] == 'W':
                        self.walls(j, i)
                    if line[x] == 'P':
                        self.path_array.append((j*20, i*20))
                    j += 1
                    
                i += 1
        self.generate_object()
        return position_mg

    def walls(self, x, y):
        """
            Displays the walls
        """
        self.window.blit(self.wall, (x*20, y*20))
        pygame.display.flip()

    def generate_object(self):
        """
            Generate objects randomly and display them
        """
        rand1 = random.randint(1, len(self.path_array))
        rand2 = rand1
        rand3 = rand1
        self.window.blit(self.ether, self.path_array[rand1-1])
        self.tab_land[(self.path_array[rand1-1][0]/20, self.path_array[rand1-1][1]/20)] = "O1"
        while rand2 == rand1:
            rand2 = random.randint(1, len(self.path_array))
        self.window.blit(self.seringue, self.path_array[rand2-1])
        self.tab_land[(self.path_array[rand2-1][0]/20, self.path_array[rand2-1][1]/20)] = "O2"
        while rand3 == rand1 or rand2 == rand3:
            rand3 = random.randint(1, len(self.path_array))
        self.window.blit(self.aiguille, self.path_array[rand3-1])
        self.tab_land[(self.path_array[rand3-1][0]/20, self.path_array[rand3-1][1]/20)] = "O3"
        pygame.display.flip()
