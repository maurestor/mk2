import pygame
from pygame.locals import *
import sys
import os

"""Lista de fuentes chidoris para utilizar...

    Comicoro
    Nokia
    pf tempesta seven
    retroville
    retrogaming


"""

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


font = pygame.font.Font(os.path.join('./assets/fonts/comicoro.ttf'), 32)
# font = pygame.font.SysFont('./assets/fonts/', 12)
# font2 = pygame.font.Font(os.path.join('/', 'otros', 'docus.ttf'), 16)


rect = Rect(50, 40, 250, 80)
pts = ('topleft', 'topright', 'bottomleft', 'bottomright',
        'midtop', 'midright', 'midbottom', 'midleft', 'center')
print(rect.center)

# def show_fonts():
#     """ Muestra una lista de las fuentes del OS """
#     fonts = pygame.font.get_fonts()
#     print(len(fonts))
#     for f in fonts:
#         print(f)


def draw_point(text, pos):
    img = font.render(text, True, 'black')
    pygame.draw.circle(screen, 'red', pos, 3)
    screen.blit(img, pos)

def draw_text(text, pos):
    tx = font.render(text, pos)
    screen.blit(tx, pos[0]+30, pos[1])


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
            draw_point(pt, eval('rect.' + pt))

        pygame.display.flip()
        clock.tick(60)


    pygame.quit()
    sys.exit()


if __name__ =='__main__':
    main_game()
