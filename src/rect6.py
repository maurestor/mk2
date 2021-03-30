import pygame
from pygame.locals import *
import sys
import os


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


r0 = Rect(50, 60, 200, 80)
r1 = Rect(100, 100, 200, 140)


def main_game():
    # show_fonts()
    running =  True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key in dir:
                    r1.move_ip(dir[event.key])


        # Continue...
        clip = r0.clip(r1)
        union = r0.union(r1)

        screen.fill('darkgray')
        pygame.draw.rect(screen, 'yellow', clip)
        pygame.draw.rect(screen, 'green', union)
        pygame.draw.rect(screen, 'red', r0, 2)
        pygame.draw.rect(screen, 'blue', r1, 2)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ =='__main__':
    main_game()
