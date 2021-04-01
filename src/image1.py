import pygame
from pygame.locals import *
import sys
import time
from poswin import PosWin


pygame.init()
W, H = 600, 400
pos = PosWin()
pos.pos_rand(W, H)
screen = pygame.display.set_mode((W, H))
font = pygame.font.SysFont('comicoro', 16)
# reloj pygame
clock = pygame.time.Clock()
t0 = time.time()

# Cargar imagen
img = pygame.image.load("./assets/img/player.old.png")
# Convertir a transparecia, opcional para mi
img.convert()
#obtener las medidas de la imagen
rect = img.get_rect()
# centrar la copia de RectObj recta sin la imagen
rect.center = W//2, H//2

# Establecer el estado del mouse a Falso
moving = False

dialoge = font.render('Llamame!!!', True, 'darkorange')

def main():
    global moving
    running = True
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


        screen.fill('gray')
        # Continue... here...
        pygame.draw.line(screen, 'darkgray', (0, H//2), (W, H//2), 1)
        pygame.draw.line(screen, 'darkgray', (W//2, 0), (W//2, H), 1)
        
        pygame.draw.rect(screen, 'lightgray', rect, 0, 5,5,5,5)
        pygame.draw.rect(screen, 'orange', rect, 2, 0,5,5,5)
        screen.blit(dialoge, (rect[0]+int(16), rect[1]-int(16)))
        screen.blit(img, rect)

        clock.tick(60)
        pygame.display.update()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()