import pygame
from pygame.locals import *
import sys
import time
from src.pygamextras import poswin, pygexit
from libs.player import Player
import pprint
import random

pygame.init()
W, H = 800, 600

poswin(100, 100)

screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont('arial', 18)

# reloj pygame
clock = pygame.time.Clock()
t0 = time.time()

player = Player(location=[0,0])

player_group = pygame.sprite.Group(player)


for x in range(10):
    for y in range(10):
        ranx = random.randrange(16, 100)
        rany = random.randrange(32, 100)
        exec(f'player{x} = Player(location=[{ranx}*{x}, {rany}*{y}])')
        exec(f'player_group.add(player{x})')
        exec(f'print(player{x}.rect)')


pprint.pprint(locals())

movex = 1
def main():
    global movex
    run = 1
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = 0
                if event.key in (K_UP, K_w):
                    player.vars['up'] = True
                if event.key in (K_DOWN, K_s):
                    player.vars['down'] = True
                if event.key in (K_LEFT, K_a):
                    player.vars['left'] = True 
                if event.key in (K_RIGHT, K_d): 
                    player.vars['right'] = True
            elif event.type == KEYUP:
                if event.key in (K_UP, K_w):
                    player.vars['up'] = False
                if event.key in (K_DOWN, K_s): 
                    player.vars['down'] = False 
                if event.key in (K_LEFT, K_a): 
                    player.vars['left'] = False
                if event.key in (K_RIGHT, K_d): 
                    player.vars['right'] = False

        screen.fill('darkgray')
        player_group.update()
        player_group.draw(screen)

        movex +=1
        if movex > W:
            movex = 0
        
        player4.rect.x = movex
        


        clock.tick(60)
        pygame.display.update()

    pygexit()

if __name__ == '__main__':
    main()