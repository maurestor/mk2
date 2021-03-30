import pygame
from pygame.locals import *
import sys
import time
from src.poswin import PosWin


pygame.init()
W, H = 600, 400

pos = PosWin()
pos.pos_rand(W, H)

screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont('arial', 18)

# reloj pygame
clock = pygame.time.Clock()
t0 = time.time()



def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running == False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running == False

        screen.fill('gray')

        pygame.draw.rect(screen, 'red', (100, 100, 100, 100), 3, 10,10,10,10)

        clock.tick(60)
        pygame.display.flip()
        # pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()