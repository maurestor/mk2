import pygame
import sys
import time
from pygame.locals import *

pygame.init()

size = 640, 320
width, height = size
GREEN = (150, 255, 150)
RED = (255, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Plantilla")
# pygame.display.set_icon()
clock = pygame.time.Clock()


pelota = pygame.image.load('../img/ball.png')
rect = pelota.get_rect()
speed = [2, 2]

def main_game():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_q:
                    run = False
            if run is False:
                pygame.quit()
                sys.exit()

        # Start for here
        global rect
        rect = rect.move(speed)

        if rect.left < 0 or rect.right > width:
            speed[0] = -speed[0]

        if rect.top < 0 or rect.bottom > height:
            speed[1] = -speed[1]

        screen.fill('green')
        pygame.draw.rect(screen, 'red', rect, 1)
        screen.blit(pelota, rect)


        # default
        clock.tick(5)
        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    main_game()
