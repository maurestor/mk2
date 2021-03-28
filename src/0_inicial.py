try:
    import pygame
    from pygame.locals import *
    import sys
    import time
    from src.poswin import PosWin
except ImportError:
    print('No se  pudieron importar librerias. ImportError')

pygame.init()
pos = PosWin()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
font = pygame.font.SysFont('arial', 18)
# reloj pygame
clock = pygame.time.Clock()
t0 = time.time()


def draw_text(text, color, x, y, bg=None):
    dialogo = font.render(text, True, color, bg)
    screen.blit(dialogo, (x, y))


def main():
    runnig = True
    while runnig:
        screen.fill('darkgray')
        for event in pygame.event.get():
            if event.type == QUIT:
                runnig = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    runnig = False



        clock.tick(60)
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()