#!/usr/env/bin python
#-*- coding:utf-8 -*-
import pygame
import sys
from pygame.locals import *

pygame.init()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dibujando formas (shapes)")
# pygame.display.set_icon()
clock = pygame.time.Clock()



def drawing_shapes():
    w_rect, h_rect = 50, 50
    pygame.draw.rect(screen, 'orange', (W//2-w_rect//2, H//2-h_rect//2, w_rect, h_rect))
    w_ellipse, h_ellipse = 100, 100
    pygame.draw.ellipse(screen, 'violet', (W//3-w_ellipse//2, H//3-h_ellipse//2, w_ellipse, h_ellipse ))
    pygame.draw.ellipse(screen, 'violet', (W//3-w_ellipse//2, H//2-h_ellipse//2, w_ellipse, h_ellipse ))
    pygame.draw.circle(screen, "orange", (550, 350), 50)



def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_q:
                    run = False
            if run is False:
                pygame.quit()
                sys.exit()


        # Background
        screen.fill('darkgray')

        # Start for here
        drawing_shapes()
        # rectangulo
        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    main()
