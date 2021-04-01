import pygame, sys
from pygame.locals import *


reloj = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Menus')

screen = pygame.display.set_mode((500, 500), 0, 32)

fuente = pygame.font.SysFont(None, 20)

color = (255, 255, 255)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def btn_hover(btn, point, color_active, color_hover):
    ''' Cambia color al pasar el raton sobre el elemento'''
    collide = btn.collidepoint(point)
    color = color_hover if collide else color_active
    pygame.draw.rect(screen, color, btn)


# click = False
def main_menu():
    ''' Menu principal de la aplicacion '''
    while True:
        screen.fill((0, 0, 0))
        draw_text('Menu principal', fuente, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 190, 45)
        button_2 = pygame.Rect(50, 150, 190, 45)
        button_exit = pygame.Rect(50, 200, 190, 45)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_exit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit(0)

        #coloreando al pasar
        point = pygame.mouse.get_pos()

        # pygame.draw.rect(screen, color, button_1)
        # pygame.draw.rect(screen, color, button_2)
        btn_hover(button_1, point, (100, 100, 100), (255, 100, 100))
        btn_hover(button_2, point, (100, 100, 100), (255, 100, 100))
        btn_hover(button_exit, point, (100, 0, 100), (255, 100, 100))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        reloj.tick(60)


def game():
    ''' Loop principal del juego'''
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Juego', fuente, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        reloj.tick(60)


def options():
    ''' Menu opciones '''
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Opciones', fuente, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        reloj.tick(60)


if __name__ == '__main__':
    main_menu()