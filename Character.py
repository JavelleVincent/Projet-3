import pygame
from pygame.locals import *

class Character():
    """
        Initialize characters
    """

    def __init__(self, window):
        self.window = window
        self.mcgiver = pygame.image.load("ressource/MacGyver.png").convert()
        self.mcgiver = pygame.transform.scale(self.mcgiver, (20, 20))
        self.guard = pygame.image.load("ressource/Gardien.png").convert()
        self.guard = pygame.transform.scale(self.guard, (20, 20))

    def macgiver(self, x, y):
        """
            For initialize mcGiver position
        """
        self.window.blit(self.mcgiver, (x*20, y*20))
        pygame.display.flip()

    def guardian(self, x, y):
        """
            For initialize Guardian position
        """
        self.window.blit(self.guard, (x*20, y*20))
        pygame.display.flip()
