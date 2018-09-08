import sys
import pygame
from pygame.locals import *
import Land as ld
import Character as ch
import Event as ev
import Engine as en

class Control():
    """
        Define all controls
    """
    cont = True

    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.window = window
        self.tab_land = ld.Land(self.window).tab_land
        clock = pygame.time.Clock()
        quit = 0
        while self.cont is True:
            for event in pygame.event.get():
                keys_pressed = pygame.key.get_pressed()
                if event.type == QUIT:    
                    self.cont = False
                    quit = 1

                if keys_pressed[pygame.K_ESCAPE]:
                    self.cont = False
                    quit = 1
                    
                if keys_pressed[pygame.K_LEFT]:
                    self.left()
                if keys_pressed[pygame.K_RIGHT]:
                    self.right()
                if keys_pressed[pygame.K_UP]:
                    self.up()
                if keys_pressed[pygame.K_DOWN]:
                    self.down()           
                clock.tick(60)
        ev.Event(self.window, self.x, self.y).reset()
        if quit == 1:
            pygame.quit()
            sys.exit()
        else:
            self.cont = True
            while self.cont is True:
                for event in pygame.event.get():
                    keys_pressed = pygame.key.get_pressed()
                    if event.type == QUIT:    
                        self.cont = False
                        pygame.quit()
                        sys.exit()
                    if keys_pressed[pygame.K_SPACE]:
                        self.cont = False
                        pygame.quit()
                        en.Engine().launch_game()
                    clock.tick(60)

    def right(self):
        """
            For the right movement
        """
        if self.x >= 14 or self.tab_land[(self.y, self.x+1)] == "W":
            pass
        else:
            fond = pygame.image.load("ressource/floor.png").convert()
            self.window.blit(fond, (self.x*20, self.y*20))
            char = ch.Character(self.window)
            char.macgiver(self.x+1, self.y)
            self.x = self.x+1
            ev.Event(self.window, self.x, self.y).check_object()
            end_condition = ev.Event(self.window, self.x, self.y).end_game()
            if end_condition is False:
                self.cont = False

    def left(self):
        """
            For the left movement
        """
        if self.x <= 0 or self.tab_land[(self.y, self.x-1)] == "W":
            pass
        else:
            fond = pygame.image.load("ressource/floor.png").convert()
            self.window.blit(fond, (self.x*20, self.y*20))
            char = ch.Character(self.window)
            char.macgiver(self.x-1, self.y)
            self.x = self.x-1
            ev.Event(self.window, self.x, self.y).check_object()
            end_condition = ev.Event(self.window, self.x, self.y).end_game()
            if end_condition is False:
                self.cont = False

    def up(self):
        """
            For the up movement
        """
        if self.y <= 0 or self.tab_land[(self.y-1, self.x)] == "W":
            pass
        else:
            fond = pygame.image.load("ressource/floor.png").convert()
            self.window.blit(fond, (self.x*20, self.y*20))
            char = ch.Character(self.window)
            char.macgiver(self.x, self.y-1)
            self.y = self.y-1
            ev.Event(self.window, self.x, self.y).check_object()
            end_condition = ev.Event(self.window, self.x, self.y).end_game()
            if end_condition is False:
                self.cont = False

    def down(self):
        """
            For the down movement
        """
        if self.y >= 14 or self.tab_land[(self.y+1, self.x)] == "W":
            pass
        else:
            fond = pygame.image.load("ressource/floor.png").convert()
            self.window.blit(fond, (self.x*20, self.y*20))
            char = ch.Character(self.window)
            char.macgiver(self.x, self.y+1)
            self.y = self.y+1
            ev.Event(self.window, self.x, self.y).check_object()
            end_condition = ev.Event(self.window, self.x, self.y).end_game()
            if end_condition is False:
                self.cont = False
