from .pygamextras import asset, screen, key_press
from .player import Player
import pygame
from pygame.locals import *
from random import randrange

class Background:
    def __init__(self, pos=[0,0]):
        """Dibujando el fondo, se mueve cuando el juagdor toca el border
        """
        self.image = pygame.image.load(asset('assets/img', 'floor_background.png'))
        self.rect = self.image.get_rect()
        self.sprites = []
        self.sprites.append(self.image.subsurface(0, 0, 128, 128))


    def update(self, surf, pos=[0,0]):

        surf.blit(self.image, (-512+pos[0], 0+pos[1]))
        surf.blit(self.image, (-512+pos[0], 512+pos[1]))
        surf.blit(self.image, (0+pos[0], 0+pos[1]))
        surf.blit(self.image, (512+pos[0], 0+pos[1]))
        surf.blit(self.image, (0+pos[0], 512+pos[1]))
        surf.blit(self.image, (512+pos[0], 512+pos[1]))



        if key_press['F4_key']:
            mouse = pygame.mouse.get_pressed()
            mousepos = pygame.mouse.get_pos()
            mouserel = pygame.mouse.get_rel()
            if mousepos:
                if self.rect.collidepoint(mousepos):
                    pygame.draw.polygon(screen, 'chocolate1', [(0+pos[0], 128+pos[1]), (100+pos[0], 128+pos[1]), (128+pos[0], 100+pos[1]), (28+pos[0], 100+pos[1])], 2 )
                    moving = True
            elif mouse[0] == False:
                moving = False
        # Si hay colision con el cursor y esta cerca el jugador debe dibujarse
        # screen.blit(background, (1024,0))
        # screen.blit(background, (1024,512))
        # screen.blit(background, (512,1024))
        # screen.blit(background, (1024,0))



    def draw_(self):
        pass

    def cuadricula_posicion(self):
        pass
# class cuadro_posiscion:
#     def __init__(self):
#         '''Dibuja
#         pass
#     def update(self):
#         pass


class UserInterface():
    def __init__(self):
        '''Dibuja la interface de usuario general de estadisticas y conroles del mercado'''
        pass      
