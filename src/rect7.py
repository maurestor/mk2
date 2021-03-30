import pygame
from pygame.locals import *
import sys
import os


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


rect = Rect(50, 60, 200, 80)
moving = False

# dir = {K_a: (-5, 0), K_d: (5, 0), K_w: (0, -5), K_s: (0, 5)}

def main_game():
    # show_fonts()
    global moving
    running =  True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            elif event.type == MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    moving = True
            
            elif event.type == MOUSEBUTTONUP:
                moving = False

            elif event.type == MOUSEMOTION and moving:
                rect.move_ip(event.rel)

        screen.fill('darkgray')
        # Continue...
        pygame.draw.rect(screen, 'orange', rect)
        print (event)
        if moving:
            pygame.draw.rect(screen, 'green', rect, 1)


        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ =='__main__':
    main_game()
