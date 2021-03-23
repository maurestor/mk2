#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import pygame
from pygame.locals import *
from datetime import datetime
from src.poswin import PosWin


'''Caracteristicas por agregar
    
    Colisiones
        
    Sistema de dialogos

    Sistema de logros!!!

    Sistema de movimiento
    
    Sistema de efectos
        Quiza lo tenga cada objeto...

    Mostrar menu del jugador
        Menus:
    
    Estadisticas del personaje
        Caracteristicas fisicas
            Salud
            Hambre
            Resistencias
                calor, frio, agua, fuego, electricidad, amor, aburrimiento,
                tristeza, veneno, rechazo, friendzone :V, asfixia

        Economia (Dinero, propiedades, negocios)
            Dinero total
            Capacidad de almacenamiento
                items
                propiedades
            Propiedades / Negocios

    Establecer Reloj. ✔ 
        
        ✔ time_control()
        
        ✔ Mostrar informacion de los tiempos.
        Mostrar reloj real. hh:ms:ss, dd/mm/yy
        Mostrar hora virtual del juego. hh:mm:ss, 1er dia (1 sem, 1 mes, etc.)
        Bucle dia noche en juego.
            Establecido 10 mins y reinicia el tiempo.
    
    Crear un sistema de consola de comandos
        listar fuentes tipograficas
        tamanio de pantalla
        colores
        dimenciones
        tiempos reloj
    
    Fuentes propuestas:
        Nokia
        Comicoro
        pf tempesta seven
        retroville
        retrogaming

'''



# ############################################################################
# Loading Starting System...
# ############################################################################
# pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize

pos_win = PosWin()

# Iniciando pygame...
pygame.init()

W, H = (800, 600)
screen = pygame.display.set_mode((W, H))
fps = 60.0

# Tiempo, horas etc.
clock = pygame.time.Clock()
t0 = time.time()
tnow = 0

str_t = {'hora':24, 'seg':60, 'dia':30, 'tick':3141569, 'start':'start'}
# timer.tick()
# Fuente
font = pygame.font.SysFont('consolas', 14, bold=True)


count = None  # Global
playtime_total = None  # Global
player_x, player_y = (W//2, H//2)  # Posicion
direction = 'down'
mx, my = 0, 0
# Cargar fondo
fondo = pygame.image.load("img/backgrounds/fondo.png")
# Direccion velocidad del personaje
player_speed = 0.9

# Declaración de constantes y variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

key_press = {"left": False,
             "right": False,
             "up": False,
             "down": False,
             "p_key": False,
             "i_key": False
             }

# player_dialoge = {wellcome: "Hello"}
# narrator = {'Hola {}'}
# png_dialoge = {wellcome: 'Hello {}.'.format(name)}

# translate = {
#     esp: {},
#     rus: {},
#     jap: {}
# }

# ############################################################################
# Funciones de debugeo
# ############################################################################


def show_fonts():
    ''' Muestra una lista de las fuentes del OS '''
    fonts = pygame.font.get_fonts()
    print(len(fonts))
    for f in fonts:
        print(f)


# ############################################################################
# Cargando funciones y metodos
# ############################################################################
def exit():
    pygame.quit()
    sys.exit()


def dialogos(logro_id):
    '''Dibuja el dialogo a partir del logro realizado.
    Se le introduce el id de logro, o logros en cola?
    Guarda los logros en un archivo o una base de datos.
        si se grabro continua
    Devuelve el dialogo correspondiente al logro

    '''
    pass


def audio_effect(name, stop_time=False, vol=0.1):
    '''Cargar efectos de audio con su nombre 
    name: menu, start, exit
    stop_time: Boulean
    vol: 0.1, 0.5, 1
    '''
    # sound = None
    if name == 'menu':
        pygame.mixer.music.load('./music/effect_nicholasdaryl_swing.wav')
        pygame.mixer.music.set_volume(vol)
        sound = pygame.mixer.music.play()
    
    if name == 'start':
        pygame.mixer.music.load('./music/desktop-login.ogg')
        pygame.mixer.music.set_volume(vol)
        sound = pygame.mixer.music.play()
    
    if name == 'exit' and stop_time:
        pygame.mixer.music.load('./music/desktop-logout.ogg')
        pygame.mixer.music.set_volume(vol)
        sound = pygame.mixer.music.play()
        time.sleep(3000)# sound.get_length())


class PlayerMeca():
    '''set controls '''

    def __init__(self, name='', gender='', options=[], active='',
                 multi=''):
        pass

    def playerDraw(self, direction='down'):
        ''' Personaje principal '''

        player = pygame.image.load('img/png/playerSprite.png')

        if direction == 'down':
            player = player.subsurface(0, 0, 32, 64)
        elif direction == 'right':
            player = player.subsurface(32, 0, 32, 64)
        elif direction == 'up':
            player = player.subsurface(64, 0, 32, 64)
        elif direction == 'left':
            player = player.subsurface(96, 0, 32, 64)
        return player


class Player(pygame.sprite.Sprite):
    """Agregar personajes, jugadores etc..."""
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load("./img/spritegral.png")
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (W / 2, H / 2)


def run_time():
    pass

def time_control(*args):
    '''Inicia el control de tiempo global 
        
        Muestra informacion del tiempo, ticks, hora especifica

        Ticks                   Tiempo          Tiempo relativo
        1000                =   1 segundo
        60,000              =   1 minuto    =   60 segundos
        36,000,000          =   1 hora      =   60 minutos
        864,000,000         =   1 dia       =   24 horas
        6,048,000,000       =   1 semana    =   7 dias
        ...
        
        720 segundos son 12 minutos
        El tiempo del juego hace un reinicio cada 12 minutos
        Tiene sus ciclos de dia y noche.
        0 a 180 a 360 a 540 y 720, el dia se divide de esta forma.
    '''
    global tnow
    t1 = time.time()
    if t1 - t0 <= 5 or tnow == 0:
        tnow = t1 - t0

    # if tnow >= 5: # 720000 =  12 min
    #     tnow = 0

    hour_game = tnow / 24
    minute_game = hour_game / 60

    now = datetime.now()
    hora_real = now.strftime("%I:%M:%S %p")

    # if time_loop == True:
    draw_text('Estado del tiempo: {:6.2f}'.format(tnow),
              font, 'white', screen, 20, 80)

    draw_text('Hora: {}'.format(hora_real),
              font, 'white', screen, W/2, 34)


def draw_text(text, font, color, surface, x, y):
    """ Dibuja texto en pantalla """
    fw, fh = font.size(text)
    surface = font.render(text, True, (0, 0, 0), (255, 255, 255, 100))
    # surface.get_rect()
    # surface = surface.center
    screen.blit(surface, (x, y))


def btn_draw(btn, point, color_active, color_hover):
    '''Cambia color al pasar el raton sobre el elemento'''
    collide = btn.collidepoint(point)
    color = color_hover if collide else color_active
    pygame.draw.rect(screen, color, btn)


def options():
    global count
    print("Llamando a opciones: %s :) " % str(count))
    count += 1


def stats():

    # global playtime_total
    # milliseconds = clock.tick(fps_out)
    # playtime_total += milliseconds / 500.0
    global mx, my
    mx, my = pygame.mouse.get_pos()

    draw_text("Player_loc: x({:4.3f}), y({:4.3f})".format(player_x, player_y),
              font, WHITE, screen, 20, 40)

    draw_text("Mouse: x({:4.3f}), y({:4.3f})".format(mx, my),
              font, WHITE, screen, 20, 60)


def options_menu():
    '''Meca Menu inventario
    TODO
    Crear un rectangulo HW al 75%
    Transparentar el rectangulo
    Dibujar barra superior con titulo
    distinguir con otro color

    Dibujar pestanias
    Inventario personaje | opciones
    '''
    global click
    click = False
    audio_effect('menu')
    while True:

        screen.fill((0, 0, 0))

        stats()

        draw_text('Menu Options', font, (255, 255, 255), screen, 20, 20)

        button_1 = pygame.Rect(50, 100, 190, 45)
        button_2 = pygame.Rect(50, 150, 190, 45)
        button_back = pygame.Rect(50, 200, 190, 45)

        if button_1.collidepoint((mx, my)):
            if click:
                audio_effect('menu')
                options_menu()
        if button_2.collidepoint((mx, my)):
            if click:
                audio_effect('menu', False, 0.1)
                options_menu()
        if button_back.collidepoint((mx, my)):
            if click:
                main_menu()

        # coloreando al pasar
        point = pygame.mouse.get_pos()
        print(point)
        btn_draw(button_1, point, ('blueviolet'), (255, 100, 100))
        btn_draw(button_2, point, (100, 100, 100), (255, 100, 100))
        btn_draw(button_back, point, (100, 0, 100), (255, 100, 100))

        all_sprites = pygame.sprite.Group()
        player_one = Player()
        all_sprites.add(player_one)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    main_game()
                    # pygame.quit()
                    # sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            # 3.- Se actualiza la pantalla
        time_control()
        pygame.display.flip()
        # time_show()
        pygame.display.set_caption("Local Market » " + str(fps))
        pygame.display.update()


# ############################################################################
# Inicio del juego
# ############################################################################

def main_menu():
    '''Meca Menu inventario
    TODO
    Crear un rectangulo HW al 75%
    Transparentar el rectangulo
    Dibujar barra superior con titulo
    distinguir con otro color

    Dibujar pestanias
    Inventario personaje | opciones
    '''
    global mx, my, tnow, click
    
    click = False
    while True:

        screen.fill('lightgray')

        # Estadisticas de casi todo...
        stats()

        # ####################################################################
        # Range colitions
        # ####################################################################

        # pygame.draw.rect(screen, 'blue', (350, 20, 120, 100), 1)
        # pygame.draw.rect(screen, 'green', (400, 60, 120, 100), 4)
        # pygame.draw.rect(screen, 'red', (450, 100, 120, 100), 8)

        # ####################################################################

        draw_text('Menu Mercadito', font, (255, 255, 255), screen, 20, 20)

        button_1 = pygame.Rect(50, 100, 190, 45)
        button_2 = pygame.Rect(50, 150, 190, 45)
        button_exit = pygame.Rect(50, 200, 190, 45)

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    main_game()
                    # pygame.quit()
                    # sys.exit(0)
                if event.key == K_r:
                    tnow = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx, my)):
            if click:
                main_game()
        if button_2.collidepoint((mx, my)):
            if click:
                options_menu()
        if button_exit.collidepoint((mx, my)):
            if click:
                exit()

        # coloreando al pasar
        point = pygame.mouse.get_pos()

        btn_draw(button_1, point, ('blueviolet'), (255, 100, 100))
        btn_draw(button_2, point, (100, 100, 100), (255, 100, 100))
        btn_draw(button_exit, point, (100, 0, 100), (255, 100, 100))

        all_sprites = pygame.sprite.Group()
        player_one = Player()
        all_sprites.add(player_one)

        click = False

        # 3.- Se actualiza la pantalla
        time_control()
        pygame.display.flip()
        pygame.display.set_caption("Local Market » " + str(tnow))
        pygame.display.update()
        clock.tick(fps)


# ############################################################################
# Loop Principal
# ############################################################################

def main_game():
    '''Función principal del juego'''

    # Guardar posicion
    global player_x, player_y, direction, player_speed, tnow, mx, my

    t1 = time.time()
    jugador = PlayerMeca()

    running = True  # Activador del menu

    # Bucle principal
    while running:
        # screen.fill(WHITE)
        # Mostrar fondo
        screen.blit(fondo, (0, 0))


        # Estadisticas
        stats()


        # Se dibuja el personaje
        screen.blit(jugador.playerDraw(direction), (player_x, player_y))

        menu_player = pygame.Surface((W//5, H//5))
        menu_player.get_rect()
        menu_player.set_alpha(128)
        menu_player.fill('white')

        # 2.- Se comprueban los eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    audio_effect('menu')
                    main_menu()
                if event.key == K_r:
                    tnow = 0
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

                if event.key == K_r:  # Reset Time
                    key_press["r_key"] = True

                if event.key == K_i and key_press["i_key"] == False:
                    key_press["i_key"] = True
                elif event.key == K_i and key_press["i_key"]:
                    key_press["i_key"] = False



            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_a:
                    key_press["left"] = False
                if event.key == K_RIGHT or event.key == K_d:
                    key_press["right"] = False
                if event.key == K_UP or event.key == K_w:
                    key_press["up"] = False
                if event.key == K_DOWN or event.key == K_s:
                    key_press["down"] = False
                if event.key == K_p:
                    key_press["p_key"] = False
            # elif running == False:
            #     exit()

        if key_press["left"]:  # == Si left es verdadero
            if player_x <= 0:
                direction = 'left'
            else:
                direction = 'left'
                player_x -= player_speed
        if key_press["right"]:
            if player_x + 32 >= W:
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
            if player_y + 256 >= W:
                # Arregla la medida del sprite a 64
                direction = 'down'
            else:
                direction = 'down'
                player_y += player_speed

        # Abrir menu del jugador
        if key_press["i_key"]:
            screen.blit(menu_player, (H/2, W/2))



        # 3.- Se actualiza la pantalla
        time_control()
        pygame.display.flip()
        pygame.display.set_caption("Local Market » " + str(tnow))
        pygame.display.update()

if __name__ == '__main__':
    audio_effect('start')
    main_menu()
