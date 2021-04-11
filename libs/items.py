import pygame
from pygame.locals import *
from .pygamextras import asset, H, W
from random import randint

class Items(pygame.sprite.Sprite):
    def __init__(self, image='items_lvls.png', location=[randint(0, W), randint(0, H)]):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.location = location


    def render(self):
        pass