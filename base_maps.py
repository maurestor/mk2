import pygame, random, os
from pygame.locals import *
import sys
import time
from colors_random import TextColors

pygame.init()
W, H = 1280, 960
screen = pygame.display.set_mode((W, H))
font = pygame.font.SysFont('comicoro', 20)
# reloj pygame
clock = pygame.time.Clock()
t0 = time.time()


''' 
Multiplos de 128 hacia abajo 
ejemplos:
128, 64, 32, 16, (8, 4, 2, 1)

'''

""" Paterns
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
          
          
          
          
"""
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

# def init_display():
    # global screen, tile
# screen = pygame.display.set_mode((W, H))
tile_floor = pygame.image.load('/home/restor/Documents/game-develop/Python manuals/floor.png')
tile_store = pygame.image.load('/home/restor/Documents/game-develop/Python manuals/store_only.png')

tile_bg = pygame.image.load('/home/restor/Documents/game-develop/Python manuals/background_road.png')

def tiles(map0, colorized=None):
    '''Corregir bien este metodo'''
# def tiles(map0):
    global tile_floor, tile_store
    for y, line in enumerate(map0):
        for x, c in enumerate(line):
            if c in (" ", "x"):
                screen.blit(tile_bg, (x*128, y*128))
            if c == "x":
                screen.blit(tile_floor, (x*128, y*128))
                screen.blit(tile_store, (x*128, y*128))


                if colorized:
                    if x == 0 or y == 0:
                        if 0 == y and x == 0:
                            pygame.draw.rect(screen, colorized, ([x, y], [128, 128]), 1, 75)
                        elif y > 0:
                            pygame.draw.rect(screen, colorized, ([x, y*128], [128, 128]), 1, 75)
                        elif x > 0:
                            pygame.draw.rect(screen, colorized, ([x*128, y], [128, 128]), 1, 75)
                    elif not 0 in (x, y):
                        pygame.draw.rect(screen, colorized, ([x*128, y*128], [128, 128]), 1, 75)

# init_display()


def main():
    running = True
    color=TextColors()
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()

            if event.type == MOUSEBUTTONDOWN:
                pass

        screen.fill('gray10')

        tiles(map_gral, color.colorize())

        # tiles(map_gral)


        clock.tick(60)
        pygame.display.flip()
        # pygame.display.update()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()