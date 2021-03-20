#!/usr/env/bin python
#-*- coding:utf-8 -*-

import pygame
import sys
from pygame.locals import *

# Starting globals
pygame.init()
clock = pygame.time.Clock()
size = (800, 420)
surface = pygame.display.set_mode(size)

start = (0, 0)
size = (0, 0)
drawing = False


running = True
while running:
    for event in pygame.event.get():
    # events
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        
        elif event.type ==MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
            print(event)
        elif event.type ==MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False
            print(event)
        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            # print(event)

    # exit
    if running == False:
        pygame.quit()
        sys.exit(0)

    # background
    surface.fill('black')
    # pygame.draw.rect(surface, 'lightgray', (start, size))
    pygame.draw.rect(surface, 'lightblue4', (start, size), 1)

    # Updates
    clock.tick(60)
    pygame.display.update()
