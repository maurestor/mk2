import pygame
from pygame.locals import *
import sys

pygame.init()

surface = pygame.display.set_mode((800, 420))
pygame.display.set_caption('Primitivas')
clock = pygame.time.Clock()


run = True
while run:
    surface.fill('black')

    for event in pygame.event.get():
        if event.type is QUIT:
            run = False
        if event.type is KEYDOWN:
            if event.key is K_q:
                run = False
        if run is False:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(surface, 'orange', (50, 50, 100, 75))
    pygame.draw.ellipse(surface, 'blueviolet', (75, 75, 200, 150), 1)
    
    # ok
    clock.tick(60)
    pygame.display.update()
