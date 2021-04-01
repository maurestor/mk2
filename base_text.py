import pygame 
from pygame.locals import *
import sys
import time

pygame.init()
W, H = 640, 480
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Un juego chidito')
clock = pygame.time.Clock()
t0 = time.time()

font = pygame.font.SysFont('magneto', 20)
img = font.render('magneto.ttf', True, 'royalblue')
rect = img.get_rect()


font1 = pygame.font.SysFont('lemon', 50)
img1 = font1.render('lemon.ttf', True, 'orangered')

font2 = pygame.font.SysFont('russoone', 50)
img2 = font2.render('russoone.ttf', True, 'pink')

fonts = pygame.font.get_fonts()
for f in fonts:
    print(f)

run = True
moving = False

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = 0
    screen.fill('gray70')

    # print(f"Tiempo desde que se creo el texto: {time.time()-t0:.2f}")
    # pygame.draw.rect()

    screen.blit(img, (20, 20))
    pygame.draw.rect(img, 'gold3', rect, 1)
    screen.blit(img1, (20, 50))
    screen.blit(img2, (20, 120))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()        
