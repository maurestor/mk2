import pygame 
from pygame.locals import *
import sys
import time

pygame.init()
W, H = 640, 480
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Textos 2')
clock = pygame.time.Clock()
t0 = time.time()

font = pygame.font.SysFont('Serif', 20)
text = 'This text is editable'
img = font.render(text, True, 'black')
rect = img.get_rect()

rect.topleft = (20, 20)
cursor = Rect(rect.topright, (3, rect.height))


run = True
moving = False

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = 0
            if event.key == K_BACKSPACE:
                if len(text) > 0:
                    text = text[:-1]
                else:
                    text += event.unicode

                img = font.render(text, True, 'red')
                rect.size = img.get_size()
                cursor.topleft = rect.topright

    screen.fill('darkgray')

    screen.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, 'orangered', cursor)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()        
