# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
 
pygame.init()
 
pantalla = pygame.display.set_mode((320,240),0,32)
imagen = pygame.image.load("img/pnj/player.png")
 
x = 10
y = 10
 
reloj = pygame.time.Clock()
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
 
    reloj.tick(25)
    pantalla.fill((0,0,0))
    pantalla.blit(imagen,(x,y))
    x,y = pygame.mouse.get_pos()
    pygame.display.update()