import pygame as p
import time
import sys
from pygame.locals import *

p.init()

size = (1024, 768)
screen = p.display.set_mode(size)
clock = p.time.Clock()
counter = 64
menu = False

def button(x, y, w, h, inactive, active, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        gameDisplay.blit(active, (x, y))
        if click[0] == 1 and action is not None:
            action()
    else:
        gameDisplay.blit(inactive, (x, y))

def main():
    run = True
    global menu
    while run:
        for e in p.event.get():
            if e.type == QUIT:
                p.quit()
                sys.exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    p.quit()
                    sys.exit()
                elif e.key == K_i:
                    menu = True
            # if menu is True and e.key == K_i:
            #     menu = False
            # elif event.type == KEYUP:
            #     if e.key == K_i:



        clock.tick(5)
        p.display.update()
        p.display.set_caption("Sistema de menus ", str(counter))

if __name__ == '__main__':
    main()