import pygame
from pygame.locals import *
import sys
import os


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

font = pygame.font.Font(os.path.join('./assets/fonts/comicoro.ttf'), 32)

rect = Rect(50, 40, 250, 80)
pts = ('topleft', 'topright', 'bottomleft', 'bottomright',
        'midtop', 'midright', 'midbottom', 'midleft', 'center')

def draw_point(text, pos):
    img = font.render(text, True, 'black')
    pygame.draw.circle(screen, 'red', pos, 3)
    screen.blit(img, pos)

def main_game():
    # show_fonts()
    running =  True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running == False

        screen.fill('gray')

        # Continue...
        pygame.draw.rect(screen, 'orange', rect, 4)

        for pt in pts:
            draw_point(pt, eval('rect.'+pt))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ =='__main__':
    main_game()
