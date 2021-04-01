import pygame 
from pygame.locals import *
import sys
import time

pygame.init()
W, H = 640, 480
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Un juego chidito')
clock = pygame.time.Clock()
t0 = time.time()

font = pygame.font.SysFont('comicoro', 14)
dialoge = font.render("Hola, que onda!!!", True, 'black')
d_rect = dialoge.get_rect()

d_rect.w, d_rect.h = d_rect.w+5, d_rect.h+5 

img = pygame.image.load('./assets/img/player.old.png')
img.convert()
rect = img.get_rect()
rect.center = (W//2, H//2)

# angle = 0
# scale = 1.2
# d_rect = pygame.transform.rotozoom(d_rect, angle, scale)
run = True
moving = False

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = 0

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving= False
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    screen.fill('darkgray')
    screen.blit(img, rect)
    pygame.draw.rect(screen, 'orange', (rect[0]+15, rect[1]-18, d_rect[2], d_rect[3]), 2, 5,5,5,5)
  
    screen.blit(dialoge, (rect[0]+16, rect[1]-16))
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()        
