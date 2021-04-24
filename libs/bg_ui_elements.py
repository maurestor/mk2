from .pygamextras import *
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



class Stats:
    def __init__(self):
        str_dia = str_time['dia']
        mx, my = pygame.mouse.get_pos()
        if key_press['F4_key']:
            
            # Muestra el mouse
            textra(f"Mouse, X: {mx}, Y: {my}", (20, 60), 'black', 'black', 1, None, 'white', 5,5,5,5)
            textra(f'{str_dia} dias {tnow[0]:6.3f}',(20, 80), 'black', 'black', 1, None, 'white', 5,5,5,5)


            # Muestra la hora real.
            textra(f'Hora: {hora_real}', (50+(W/2), 34), 'black', 'black', 1, None, 'white', 5,5,5,5)
            # Muestra el momento del dia
            textra('{}'.format(str_time['moment_time']), (50+(W/2), 55), 'black', 'black', 1, None, 'white', 5,5,5,5)
            textra(f'{vday}', (50+(W/2), 75), 'black', 'black', 1, None, 'white', 5,5,5,5)


class UserInterface():
    def __init__(self):
        self.gui()
    
    def gui(self):
        '''Dibuja la interface de usuario general de estadisticas y conroles del mercado'''

        str_dia = str_time['dia']
        
        # pygame.draw.arc(screen, 'green', [W-100, 0, 250, 250], math.pi, 3*math.pi/2)
        
        pygame.draw.rect(screen, 'chartreuse4', [W-202, 0, 302, 37], 0, 0, 5, 0, 15)
        pygame.draw.ellipse(screen, 'chartreuse4', [W-102, -102, 205, 205])
        pygame.draw.rect(screen, 'chartreuse3', [W-200, 0, 300, 35], 0, 0, 5, 0, 15)
        pygame.draw.ellipse(screen, 'chartreuse3', [W-100, -100, 200, 200])

        textra(f'Counter {str_dia}, {tnow[0]:6.1f}', [W-190, 8], 'black')


