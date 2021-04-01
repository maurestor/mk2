import pygame
from pygame.locals import *
import sys
import time
from datetime import datetime
from poswin import PosWin


pygame.init()
pos = PosWin()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
font = pygame.font.SysFont('arial', 18)

# reloj pygame
clock = pygame.time.Clock()
t0 = time.time() # tiempo desde los 70's en segundos

time_vars = 

def exit():
    pygame.quit()
    sys.exit()

def draw_text(text, color, x, y, bg=None):
    dialogo = font.render(text, True, color, bg)
    screen.blit(dialogo, (x, y))


def main():
    global tnow
    runnig = True
    while runnig:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_r:
                    tnow = 0

        screen.fill('gray')

        t1 = time.time()
        if t1 - t0 < 5 or tnow == 0:
            tnow = t1 - t0
        if t1 - t0 > 5:
            tnow = 0




        draw_text('Barra Porcentaje: {:3.2f}'.format(tnow), 'yellow', 20, 60, 'black')
        pygame.draw.rect(screen, 'yellow', (0, 500, tnow*5, 20))
        # pygame.display.flip()
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()