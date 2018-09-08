import pygame
from pygame.locals import *
import Land as ld

class Event():
    """
        Class that manages events
    """
    inventory = 0

    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.tab_land = ld.Land(self.window).tab_land
        self.ether = pygame.image.load("ressource/ether.png").convert()
        self.ether = pygame.transform.scale(self.ether, (20, 20))
        self.seringue = pygame.image.load("ressource/seringue.png").convert()
        self.seringue = pygame.transform.scale(self.seringue, (20, 20))
        self.aiguille = pygame.image.load("ressource/aiguille.png").convert()
        self.aiguille = pygame.transform.scale(self.aiguille, (20, 20))

    def end_game(self):
        """
            end of game event
        """
        tab_land = ld.Land(self.window).tab_land
        position_guard = list(tab_land.keys())[list(tab_land.values()).index("E")]
        myfont = pygame.font.SysFont("monospace", 15)
        if position_guard[0] == self.y and position_guard[1] == self.x:
            if type(self).inventory == 3:
                print("VICTOIRE")
                
                label = myfont.render("Bravo vous avez gagné !", 1, (255, 255, 255))
                self.window.blit(label, (60, 150))
                label = myfont.render("Espace pour recommencer", 1, (255, 255, 255))
                self.window.blit(label, (60, 180))
                pygame.display.flip()
                
            else:
                print("DEFAITE")
                self.defeat = pygame.image.load("ressource/items.png").convert()
                self.defeat = pygame.transform.scale(self.defeat, (20, 20))
                self.window.blit(self.defeat, (self.x*20, self.y*20))
                label = myfont.render("Espace pour recommencer", 1, (255, 255, 255))
                self.window.blit(label, (60, 180))
                pygame.display.flip()

            
            return False

    def check_object(self):
        """
            check if you are on an object
        """
        if self.tab_land[(self.x, self.y)] == "O1" or self.tab_land[(self.x, self.y)] == "O2" or self.tab_land[(self.x, self.y)] == "O3":
            myfont = pygame.font.SysFont("monospace", 15)
            type(self).inventory = self.inventory+1
            i = 100
            y = 40
           
            if self.tab_land[(self.x, self.y)] == "O1":
                self.window.blit(self.ether, (i + y * type(self).inventory, 350))

            if self.tab_land[(self.x, self.y)] == "O2":
                self.window.blit(self.seringue, (i + y * type(self).inventory, 350))

            if self.tab_land[(self.x, self.y)] == "O3":
                self.window.blit(self.aiguille, (i + y * type(self).inventory, 350))

            self.tab_land[(self.x, self.y)] = "P"
            pygame.display.flip()

    def reset(self):
        """
            For reset the inventory
        """
        type(self).inventory = 0
