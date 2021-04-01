import pygame
from pygame.locals import *
import sys
import os


pygame.init()
W, H = 640, 480
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

rect = Rect(50, 60, 200, 80)

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

                if event.key == K_l:
                    rect.left = 0
                if event.key == K_c:
                    rect.centerx = W // 2
                if event.key == K_r:
                    rect.right = W

                if event.key == K_t:
                    rect.top = 0
                if event.key == K_m:
                    rect.centery = H // 2
                if event.key == K_b:
                    rect.bottom = H

        screen.fill('gray')
        # Continue...

        pygame.draw.rect(screen, 'blue', rect, 1)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()


if __name__ =='__main__':
    main_game()
