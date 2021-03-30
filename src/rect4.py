import pygame
from pygame.locals import *
import sys
import os


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


dir = {K_a: (-5, 0), K_d: (5, 0), K_w: (0, -5), K_s: (0, 5)}
rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()

def main_game():
    # show_fonts()
    running =  True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running == False
                if event.key in dir:
                    v = dir[event.key]
                    rect.move_ip(v)
            # Modificar
            # elif event.type == KEYUP:
            #     if event.key in dir:
            #         v = dir[event.key]
            #         rect.move_ip(v)
            

        screen.fill('gray')

        # Continue...
        pygame.draw.rect(screen, 'blue', rect0, 1)
        pygame.draw.rect(screen, 'red', rect, 4)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ =='__main__':
    main_game()
