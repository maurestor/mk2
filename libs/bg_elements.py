from .pygamextras import asset
from .player import Player
import pygame
from pygame.locals import *

class Background:
    def __init__(self):
        self.background = pygame.image.load(asset('assets/img', 'floor_background.png'))
        # background_r = background.get_rect()


    def update(self, surf, pos=[0,0]):

        surf.blit(self.background, (0+pos[0], 0+pos[1]))
        surf.blit(self.background, (512+pos[0], 0+pos[1]))
        surf.blit(self.background, (0+pos[0], 512+pos[1]))
        surf.blit(self.background, (512+pos[0], 512+pos[1]))
        # screen.blit(background, (1024,0))
        # screen.blit(background, (1024,512))
        # screen.blit(background, (512,1024))
        # screen.blit(background, (1024,0))

