import pygame
import sys
from pygame.locals import *

pygame.init()
# Iniciando pygame...

s_width, s_height = (800, 600)
screen = pygame.display.set_mode((s_width, s_height), pygame.DOUBLEBUF)
pygame.display.set_caption("Local Market")

# Fuente
font = pygame.font.SysFont(None, 14, bold=True)
clock = pygame.time.Clock()
fps = 60

count = 0  # Global
playtime_total = 0.0  # Global
player_x, player_y = (0, 0)  # Posicion
direction = 'down'

# Cargar fondo
fondo = pygame.image.load("img/backgrounds/fondo.png")

# Direccion velocidad del personaje
player_speed = 4.0

# Declaración de constantes y variables
WHITE = (255, 255, 255)

key_press = {"left": False,
             "right": False,
             "up": False,
             "down": False,
             "p_key": False}


def draw_text(text, font, color, surface, x, y):
    """Center text in window"""
    fw, fh = font.size(text)
    surface = font.render(text, True, (0, 0, 0), (255, 255, 255, 100))
    screen.blit(surface, (x, y))


def btn_hover(btn, point, color_active, color_hover):
    ''' Cambia color al pasar el raton sobre el elemento'''
    collide = btn.collidepoint(point)
    color = color_hover if collide else color_active
    pygame.draw.rect(screen, color, btn)


def options():
    global count
    print("Llamando a opciones: %s :) " % str(count))
    count += 1


def main_menu():
    ''' Meca Menu inventario
    TODO
    Crear un rectangulo HW al 75%
    Transparentar el rectangulo
    Dibujar barra superior con titulo
    distinguir con otro color

    Dibujar pestanias
    Inventario personaje | opciones
    '''
    click = False
    while True:

        screen.fill((0, 0, 0))
        draw_text('Menu MK2', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 190, 45)
        button_2 = pygame.Rect(50, 150, 190, 45)
        button_exit = pygame.Rect(50, 200, 190, 45)

        if button_1.collidepoint((mx, my)):
            if click:
                main()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_exit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit(0)

        # coloreando al pasar
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
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    main()
                    # pygame.quit()
                    # sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            # 3.- Se actualiza la pantalla
        pygame.display.update()
        clock.tick(fps)


def stats():
    global playtime_total
    milliseconds = clock.tick(fps)
    playtime_total += milliseconds / 500.0

    if key_press['p_key']:
        draw_text("FPS: {:6.3} Tot time: {:6.3} segs".format(
                  clock.get_fps(), playtime_total),
                  font, (255, 255, 255), screen, 20, 20)
        draw_text("Loc(xy): {}, {}".format(player_x, player_y),
                  font, (255, 255, 255), screen, 20, 40)


class PlayerMeca():
    '''set controls '''

    def __init__(self, name='', gender='', options=[], active='',
                 multi=''):
        pass

    def playerDraw(self, direction='down'):
        ''' Personaje principal '''
        player = pygame.image.load('img/pnj/playerSprite.png')

        if direction == 'down':
            player = player.subsurface(0, 0, 32, 64)
        elif direction == 'right':
            player = player.subsurface(32, 0, 32, 64)
        elif direction == 'up':
            player = player.subsurface(64, 0, 32, 64)
        elif direction == 'left':
            player = player.subsurface(96, 0, 32, 64)
        return player


def main():
    '''Función principal del juego'''

    # Guardar posicion
    global player_x, player_y
    global direction

    player = PlayerMeca()

    running = True  # Activador del menu

    # Bucle principal
    while running:

        # Mostrar fondo
        screen.blit(fondo, (0, 0))

        # Se dibuja el personaje
        screen.blit(player.playerDraw(direction), (player_x, player_y))

        cubo = pygame.Rect(s_width / 2, s_height / 2, 60, 60)
        pygame.draw.rect(screen, WHITE, cubo)

        # 2.- Se comprueban los eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
                if event.key == K_LEFT or event.key == K_a:
                    key_press["left"] = True
                if event.key == K_RIGHT or event.key == K_d:
                    key_press["right"] = True
                if event.key == K_UP or event.key == K_w:
                    key_press["up"] = True
                if event.key == K_DOWN or event.key == K_s:
                    key_press["down"] = True
                if event.key == K_p:  # Comandos FPS
                    key_press["p_key"] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == K_a:
                    key_press["left"] = False
                if event.key == pygame.K_RIGHT or event.key == K_d:
                    key_press["right"] = False
                if event.key == pygame.K_UP or event.key == K_w:
                    key_press["up"] = False
                if event.key == pygame.K_DOWN or event.key == K_s:
                    key_press["down"] = False
                if event.key == pygame.K_p:
                    key_press["p_key"] = False

        if key_press["left"]:  # == Si left es verdadero
            if player_x <= 0:
                direction = 'left'
            else:
                direction = 'left'
                player_x -= player_speed
        if key_press["right"]:
            if player_x + 32 >= s_width:
                direction = 'right'
            else:
                direction = 'right'
                player_x += player_speed
        if key_press["up"]:
            if player_y <= 0:
                direction = 'up'
            else:
                direction = 'up'
                player_y -= player_speed
        if key_press["down"]:
            if player_y + 265 >= s_width:
                # Arregla la medida del sprite a 64
                direction = 'down'
            else:
                direction = 'down'
                player_y += player_speed

        # Estadisticas
        stats()

        # 3.- Se actualiza la pantalla
        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    # Este fichero es el que ejecuta el juego principal
    main_menu()
    # main()
