import pygame
import sys
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Juego Nuevo')

RED, GREEN, BLUE, = (0, 0, 0)
r_inver, g_inver, b_inver = False, False, False
rgb = [RED, GREEN, BLUE, r_inver, g_inver, b_inver]

clock = pygame.time.Clock()



running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:

            if event.key == K_q:
                pygame.quit()
                sys.exit()

    # si la opacidad es menor a 255 y no se decrementa
    if RED < 255 and r_inver is False:
        RED += 1  # Suma al color + 1
    # Si no se cumple la sentencia anterior y el color e igual a  igual a 255
    elif RED == 255:
        r_inver = True  # Se establece a True la inversa

    # Si el color es menor o igual a 255 y la inversa es verdadera
    if RED <= 255 and r_inver is True:
        RED -= 1  # resta al color - 1
    if RED == 0:  # al llegar la opacidad a cero
        r_inver = False

    RED = RED
    print(str(RED) + ' ' + str(r_inver))

    screen.fill((RED, GREEN, BLUE))
    # pygame.time.delay(10)
    pygame.display.update()
    clock.tick(60)
