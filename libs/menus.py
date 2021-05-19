import pygame
from pygame.locals import *
from .pygamextras import *


class Menu:
    
    def __init__(self):
        # menu = Menu Item Player
        #
        self.w = int((W/100)*80)
        self.h = int((H/100)*80)
        self.menu = pygame.Surface((self.w, self.h))
        # menu_h_center, menu_w_center = menu.get_height()/2, menu.get_width()/2
        self.menu.get_rect()
        # menu.center
        self.menu.set_alpha(200)
        self.menu.fill('white')

    def show(self):
        # Dibujar el menu en medio
        screen.blit(self.menu, (((W//2)-self.w/2), ((H//2)-self.h/2)))


class Dialogue(Menu):
    def __init__(self):
        self.moving = [0, True]

    def show(self, position=[]):
        # Dialogues - exchange system
        if self.moving[0] < 10 and self.moving[1] == True:
            self.moving[0] += 1
            if self.moving[0] >= 10:
                self.moving[1] = False
        elif self.moving[1] == False and self.moving[0] <= 10:
            self.moving[0] -= 1
            if self.moving[0] <= -10:
                self.moving[1] = True
            
        # elif self.moving[0] > 100 and self.moving[1]:
        #     self.moving[1] = False
        
        pygame.draw.rect(screen, 'white', position, 0, 5)