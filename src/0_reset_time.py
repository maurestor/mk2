import pygame
from pygame.locals import *
import sys
import time
from datetime import datetime
from poswin import PosWin


pygame.init()
pos = PosWin()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
font = pygame.font.SysFont('arial', 18)

# reloj pygame
clock = pygame.time.Clock()
 # tiempo desde, creo que 1970's en segundos
t0 = time.time()
tnow = [0, True]

def exit():
    '''Obviamente salir de pygame'''
    pygame.quit()
    sys.exit()

def draw_text(text, color, x, y, bg=None):
    '''Dibujar texto en pantalla'''
    dialogo = font.render(text, True, color, bg)
    screen.blit(dialogo, (x, y))

def main():
    '''Ciclo principal
    La funcionalidad del programa es generar un contador que resete al 
    tiempo exacto de cierto tiempo.

    Se muestra analogamente una barra que aumenta el tamanio al 100% 
    del amanio de la ventana.
    '''

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
        velocity = 6
        if tnow[1] == False or tnow[0] >= W/velocity: 
            ''' la ultima comprobacion despues de or para definir el tiempo
            de reinicio del reloj '''
            tnow[0], tnow[1] = 0, True
            t0 = time.time()
        elif tnow[1]:
            tnow[0] = time.time() - t0

        # print(tnow)

        draw_text('Puedes resetear el tiempo y la barra con la tecla \'R\'',
                  'yellow', 20, 40, 'black')
        pygame.draw.rect(screen, 'yellow', (0, 200, tnow[0]*velocity, 20))
        draw_text('Tiempo: {:3.2f} Segs.  :) :O'.format(tnow[0]),
                  'black', int((tnow[0]*velocity/2)), 200)
        
        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()

if __name__ == '__main__':
    main()
