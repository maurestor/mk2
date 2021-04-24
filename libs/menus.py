import pygame
from pygame.locals import *
from .pygamextras import W, H


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

    def show(self, surface):
        # Dibujar el menu en medio
        surface.blit(self.menu, (((W//2)-self.w/2), ((H//2)-self.h/2)))
    