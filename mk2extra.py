import pygame
from pygame.locals import *
import sys
import time
from datetime import datetime
from src.poswin import PosWin


pygame.init()
pos = PosWin()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
font = pygame.font.SysFont('arial', 18)
t0 = time.time()

# reloj pygame
clock = pygame.time.Clock()
 # tiempo desde los 70's en segundos

tnow = [0, True]

def exit():
    pygame.quit()
    sys.exit()

def draw_text(text, color, x, y, bg=None):
    dialogo = font.render(text, True, color, bg)
    screen.blit(dialogo, (x, y))

def main():
    global t0
    runnig = True
    while runnig:
        screen.fill('gray')
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_r:
                    tnow[1] = False

        if tnow[1] == False:
            tnow[0] = 0
            tnow[1] = True
            t0 = time.time()
        elif tnow[1]:
            tnow[0] = time.time() - t0
            
        print(tnow)

        draw_text('Barra Porcentaje: {:3.2f}'.format(tnow[0]), 'yellow', 20, 60, 'black')
        pygame.draw.rect(screen, 'yellow', (0, 200, tnow[0]*10, 20))
        clock.tick(60)
        # pygame.display.flip()
        pygame.display.update()

if __name__ == '__main__':
    main()