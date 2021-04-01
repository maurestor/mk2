#!/usr/bin/env python
#-*- coding:utf-8 -*-

try:
    import pygame
    from pygame.locals import *
    import sys
    import time
    import random
    from src.poswin import PosWin
except ImportError:
    print('Se importaron mal esta/s librerias, ImportError.')


def draw_text(text, color, x, y, bg=None):
    dialogo = font.render(text, True, color, bg)
    screen.blit(dialogo, (x, y))


class Player(pygame.sprite.Sprite):
    def __init__(self, img, ):
        pass


player_img = pygame.image.load('./img/png/player.png')

pygame.init()
pos = PosWin()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
font = pygame.font.SysFont('arial', 18)

# reloj pygame
clock = pygame.time.Clock()
t0 = time.time()

center_W, center_H = W//2, H//2
# Posicion del personaje
player_x = 32
player_y = 64
# 
player_sprite = player_img.subsurface(0, 0, 32, 64)

# collider_size = player_sprite.get_rect()
collider_x = 32
collider_y = 64


def main():
    runnig = True
    while runnig:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == QUIT:
                runnig = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    runnig = False

        for i in range(50):
            collider = Rect(random.randrange(i-32, W), random.randrange(i-64, H), collider_x, collider_y)
            pygame.draw.rect(screen, 'gold', collider, 1)

        clock.tick(30)
        pygame.display.flip()
    
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()