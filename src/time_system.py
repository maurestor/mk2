import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Juego Nuevo')

RED, GREEN, BLUE, = (0, 0, 0)

clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:

            if event.key == K_q:
                pygame.quit()
                sys.exit()
    
    if RED < 255:
        RED += 2
    if RED > 255:
        RED = 0
    else:
        RED = 0
    if GREEN < 255:
        GREEN += 1
    else:
        GREEN = 0
    if BLUE < 255:
        BLUE += 1
    else:
        BLUE = 0
    # print(RED)
    screen.fill((RED, GREEN, BLUE))
    pygame.time.delay(10)
    pygame.display.update()
    clock.tick(120)