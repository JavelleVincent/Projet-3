import pygame
from pygame.locals import *
import Land as ld
from Land import *
import Control
from Control import *

class Engine():
    """
        Class which create the game
    """
    def __init__(self):
        pygame.init()
        self.start_window = pygame.display.set_mode((600, 100))
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Pour commencer appuyer sur Espace", 1, (255, 255, 255))
        self.start_window.blit(label, (100, 40))
        pygame.display.flip()
        clock = pygame.time.Clock()
        self.cont = True
        while self.cont is True:
            for event in pygame.event.get():
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_SPACE]:
                    self.launch_game()
                    self.cont = False
                    pygame.QUIT                
                clock.tick(60)
        while pygame.event.wait().type != pygame.QUIT: pass

    def launch_game(self):
        """
            Launch the game
        """
        self.window = pygame.display.set_mode((300, 400))
        land = ld.Land(self.window)
        land.background()
        maps = land.map()
        control = Control(maps[0], maps[1], self.window)
        if control == None:
            pygame.display.quit()
        while pygame.event.wait().type != pygame.QUIT: pass

 
