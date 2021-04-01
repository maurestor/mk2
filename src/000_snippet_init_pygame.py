#!/usr/env/bin python
#-*- coding:utf-8 -*-
import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Plantilla")
# pygame.display.set_icon()
clock = pygame.time.Clock()

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

        # Start for here



        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    main()
