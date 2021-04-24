from .pygamextras import *
from .player import Player
import pygame
from pygame.locals import *
from random import randrange


class Background:
    def __init__(self):
        """Renderizando fondo, se mueve cuando el juagdor toca el border


        """

        # Asignado atributos del renderizado
        self.tile_floor = pygame.image.load(asset('assets/img', 'floor.png'))
        self.tile_store = pygame.image.load(
            asset('assets/img', 'store_only.png'))
        self.tile_bg = pygame.image.load(
            asset('assets/img', 'background_road.png'))

        self.image = pygame.image.load(
            asset('assets/img', 'floor_background.png'))
        self.rect = self.image.get_rect()
        self.sprites = []
        self.sprites.append(self.image.subsurface(0, 0, 128, 128))

        # Iniciando el renderizado

    def update(self, surf, pos=[0, 0]):

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
                    pygame.draw.polygon(screen, 'chocolate1', [(
                        0+pos[0], 128+pos[1]), (100+pos[0], 128+pos[1]), (128+pos[0], 100+pos[1]), (28+pos[0], 100+pos[1])], 2)
                    moving = True
            elif mouse[0] == False:
                moving = False
        # Si hay colision con el cursor y esta cerca el jugador debe dibujarse
        # screen.blit(background, (1024,0))
        # screen.blit(background, (1024,512))
        # screen.blit(background, (512,1024))
        # screen.blit(background, (1024,0))

    def tiles(posone=[0, 0], colorized=False):
        '''Corregir bien este metodo

        Multiplos de 128 hacia abajo
        ejemplos:
        128, 64, 32, 16, (8, 4, 2, 1)

        Paterns
        Crear un generador dinamico de mapas

        Wall
        ----------
        xxxxxxxxxx
        x        x
        x        x
        x        x
        x        x
        x        x
        xxxxxxxxxx
        ----------

        Only One
        ----------


            x     




        ----------

        Window
        xxxxxxxxxx
        x   xx   x
        x   xx   x
        x   xx   x
        x   xx   x
        x   xx   x
        xxxxxxxxxx
        ----------

        Noting
        ----------







        ----------

        Spiral
        xxxxxxxxxx
                 x
        xxxxxxxx x
        x      x x
        x xxxxxx x
        x        x
        xxxxxxxxxx
        ----------

        two
        ----------


        x     x   




        '''
        map_gral = """xxxxxxxxxx
         x
xxxxxxxx x
x      x x
x xxxxxx x
x        x
xxxxxxxxxx"""

        map_gral = map_gral.splitlines()
        print(f'Rendering that map :)\n{"-"*10}')
        for line in map_gral:
            print(line)
        print("-"*10)
        # print(posone[1])
        # Asignado atributos del renderizado
        tile_floor = pygame.image.load(asset('assets/img', 'floor.png'))
        tile_store = pygame.image.load(asset('assets/img', 'store_only.png'))
        tile_bg = pygame.image.load(asset('assets/img', 'background_road.png'))

        # def tiles(map0, colorized=None):
        # global tile_floor, tile_store
        for y, line in enumerate(map_gral):
            for x, c in enumerate(line):
                # print(pos[0])
                if c in (" ", "x"):
                    screen.blit(tile_bg, ((x*128), (y*128)))
                if c == "x":
                    screen.blit(tile_floor, (x*128, (y*128)+108))
                    screen.blit(tile_store, (x*128, y*128))

                    if colorized==True:
                        if x == 0 or y == 0:
                            if 0 == y and x == 0:
                                pygame.draw.rect(
                                    screen, colorized, ([x, y], [128, 128]), 1, 75)
                            elif y > 0:
                                pygame.draw.rect(
                                    screen, colorized, ([x, y*128], [128, 128]), 1, 75)
                            elif x > 0:
                                pygame.draw.rect(
                                    screen, colorized, ([x*128, y], [128, 128]), 1, 75)
                        elif not 0 in (x, y):
                            pygame.draw.rect(
                                screen, colorized, ([x*128, y*128], [128, 128]), 1, 75)

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
            textra(f"Mouse, X: {mx}, Y: {my}", (20, 60),
                   'black', 'black', 1, None, 'white', 5, 5, 5, 5)
            textra(f'{str_dia} dias {tnow[0]:6.3f}', (20, 80),
                   'black', 'black', 1, None, 'white', 5, 5, 5, 5)

            # Muestra la hora real.
            textra(f'Hora: {hora_real}', (50+(W/2), 34),
                   'black', 'black', 1, None, 'white', 5, 5, 5, 5)
            # Muestra el momento del dia
            textra('{}'.format(str_time['moment_time']), (50+(W/2),
                   55), 'black', 'black', 1, None, 'white', 5, 5, 5, 5)
            textra(f'{vday}', (50+(W/2), 75), 'black',
                   'black', 1, None, 'white', 5, 5, 5, 5)


class UserInterface():
    def __init__(self):
        self.gui()

    def gui(self):
        '''Dibuja la interface de usuario general de estadisticas y conroles del mercado'''

        str_dia = str_time['dia']

        # pygame.draw.arc(screen, 'green', [W-100, 0, 250, 250], math.pi, 3*math.pi/2)

        pygame.draw.rect(screen, 'chartreuse4', [
                         W-202, 0, 302, 37], 0, 0, 5, 0, 15)
        pygame.draw.ellipse(screen, 'chartreuse4', [W-102, -102, 205, 205])
        pygame.draw.rect(screen, 'chartreuse3', [
                         W-200, 0, 300, 35], 0, 0, 5, 0, 15)
        pygame.draw.ellipse(screen, 'chartreuse3', [W-100, -100, 200, 200])

        textra(f'Counter {str_dia}, {tnow[0]:6.1f}', [W-190, 8], 'black')
