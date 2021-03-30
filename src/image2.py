import pygame
from pygame.locals import *
import sys
from datetime import datetime
import time
import math


pygame.init()
clock = pygame.time.Clock()
W, H = 640, 480
screen = pygame.display.set_mode((W, H))

img0 = pygame.image.load('./assets/img/player.old.png')
rect0 = img0.get_rect()
img, rect  = img0, rect0

center = (W//2, H//2)
img1 = img0
rect1 = img0.get_rect()
rect1.center = center

scale = 1
angle = 0
mouse = pygame.mouse.get_pos()

moving = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
            elif event.key == K_r:
                if event.mod & KMOD_SHIFT:
                    angle -= 10
                else:
                    angle += 10
                img1 = pygame.transform.rotozoom(img0, angle, scale)
            elif event.key == K_s:
                if event.mod & KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1
                img1 = pygame.transform.rotozoom(img0, angle, scale)
            elif event.key == K_o:
                img1 = img0
                scale = 1
                angle = 0
            elif event.key == K_h:
                img1 = pygame.transform.flip(img1, True, False)
            elif event.key == K_v:
                img1 = pygame.transform.flip(img1, False, True)
            elif event.key == K_l:
                img1 = pygame.transform.laplacian(img1)
            elif event.key == K_2:
                img1 = pygame.transform.scale2x(img1)
        
            rect1 = img1.get_rect()
            rect1.center = center

        elif event.type == MOUSEMOTION:
            mouse = event.pos
            x = mouse[0] - center[0]
            y = mouse[1] - center[1]
            d = math.sqrt(x ** 2 + y ** 2)

            angle = math.degrees(-math.atan2(y, x))
            scale = abs(5 * d / W)
            img1 = pygame.transform.rotozoom(img0, angle, scale)
            rect1 = img1.get_rect()
            rect1.center = center

        elif event.type == MOUSEBUTTONDOWN:
            if rect0.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving:
            rect0.move_ip(event.rel)

    


    screen.fill('darkblue')

    print(clock)

    screen.blit(img1, rect1)
    pygame.draw.rect(screen, 'white', rect1, 1)
    pygame.draw.line(screen, 'green', center, mouse, 1)
    pygame.draw.circle(screen, 'red', center, 6, 1)
    pygame.draw.circle(screen, 'red', mouse, 6, 1)   
    
    
    screen.blit(img0, rect0)
    pygame.draw.rect(screen, 'white', rect0, 1)

    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
