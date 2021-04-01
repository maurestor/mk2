import pygame
import os
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode(10, 10)

def draw_text(text: str, color: tuple, x: int, y: int, bg=None, screen=screen):
    """Dibuja texto en la pantalla

    Esta funcion dibuja texto en la pantalla, con su color, ubicacion,
    fondo y mas cosillas...

    :Parameters:
    `text`: str
        Agrega una cadena de texto para ser mostrada
    `color`: tuple
        Agrega un color con codigo de color, grb, rgba, etc...
    `x`: int
        Agrega la medida del eje X, Vertical
    `y`: int
        Agrega la medida del eje Y, Horizontal
    `bg`: str
        Agrega el color del fondo del campo de texto

    """
    font = pygame.font.Font(os.path.join('./assets/fonts/comicoro.ttf'), 32)
    dialogo = font.render(text, True, color, bg)
    screen.blit(dialogo, (x, y))

if __name__ == "__main__":
    draw_text()