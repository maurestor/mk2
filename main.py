#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame
import os
import sys
import time
from pygame.locals import *
from datetime import datetime
import json


from libs.pygamextras import *
from libs.stores import Store, MultiShop
from libs.bg_ui_elements import Background
from libs.menus import Menu


from libs.player import Player
import pprint
# from libs.items import Items


"""Caracteristicas por agregar
    
    USA DE TODO.
    NO CAMBIAR LO QUE YA FUNCIONA!
    NO TE CASES CON LAS COSAS!
    
    # Ten cuidado de usar la linea 1 incorrectamente, en linux causa conflicto el interprete
    
    Colisiones
        
    Sistema de dialogos

    Sistema de logros!!!

    ✔ Sistema de movimiento
    
    Sistema de efectos
        Quiza lo tenga cada objeto...

    ✔ Mostrar menu items jugador
        » Menus: Pestanias
    
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

"""
# ############################################################################
# Cargando funciones y metodos
# ############################################################################


def dialogos(logro_id):
    """Dibuja el dialogo a partir del logro realizado.
    Se le introduce el id de logro, o logros en cola?
    Guarda los logros en un archivo o una base de datos.
        si se grabro continua
    Devuelve el dialogo correspondiente al logro

    """
    pass


def audio_effect(name, stop_time=False, vol=0.3):
    """Cargar efectos de audio con su nombre 
    name: menu, start, exit
    stop_time: Boulean
    vol: 0.1, 0.5, 1
    """
    # sound = None
    if name == 'menu':
        # pygame.mixer.music.load('./assets'assets/music',/effect_nicholasdaryl_swing.wav')
        pygame.mixer.music.load(asset('assets/music', 'effect_nicholasdaryl_swing.wav'))
        pygame.mixer.music.set_volume(vol)
        sound = pygame.mixer.music.play()

    if name == 'start':
        # pygame.mixer.music.load('./assets'assets/music',/desktop-login.ogg')
        pygame.mixer.music.load(asset('assets/music', 'desktop-login.ogg'))
        pygame.mixer.music.set_volume(vol)
        sound = pygame.mixer.music.play()

    if name == 'exit' and stop_time:
        pygame.mixer.music.load(asset('assets/music', 'desktop-logout.ogg'))
        pygame.mixer.music.set_volume(vol)
        sound = pygame.mixer.music.play()
        time.sleep(3000)  # sound.get_length())


def run_time():
    tfull = 720  # Ciclo completo, dia entero
    thour = tfull/24  # Una hora
    if tnow[0] >= 0 and tnow[0] < thour*7:
        str_time['moment_time'] = 'Es muy temprano'
    elif tnow[0] > 7 and tnow[0] < thour*12:
        str_time['moment_time'] = 'Es de maniana'
    elif tnow[0] > thour*12 and tnow[0] < thour*19:
        str_time['moment_time'] = "Es de tarde"
    elif tnow[0] > thour*19 and tnow[0] < tfull:
        str_time['moment_time'] = 'Es de noche'


def time_control():
    """Inicia el control de tiempo global 

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
    """
    global t0, hora_real, tfull, vday
    # Control del tiempo
    if tnow[1] == False or tnow[0] >= tfull:
        tnow[0], tnow[1] = 0, True
        t0 = time.time()
        str_time['dia'] += 1
    elif tnow[1]:
        tnow[0] = time.time() - t0

    pygame.draw.rect(screen, 'yellow', (0, 0, tnow[0], 10))

    vday = tfull / 86400
    now = datetime.now()
    hora_real = now.strftime("%I:%M:%S %p")


# sustituir por textra desde pygamextras
def draw_text(text, font, color, surface, x, y):
    """ Dibuja texto en pantalla """

    surface = font.render(text, True, (0, 0, 0), (255, 255, 255, 100))
    # surface.get_rect()
    # surface = surface.center
    screen.blit(surface, (x, y))


# Meter el sistema de botones y menus a una clase por favor :)
def btn_draw(btn, point, color_active, color_hover):
    """Cambia color al pasar el raton sobre el elemento"""
    collide = btn.collidepoint(point)
    color = color_hover if collide else color_active
    pygame.draw.rect(screen, color, btn)


# Meter el sistema de botones y menus a una clase por favor :)
def options():
    global count
    print("Llamando a opciones: %s :) " % str(count))
    count += 1


# def debug(var):
#     return pygame.draw.rect(screen, 'gold', var, 1)
#     # print(rect)


def active_stats():
    """ 
    global playtime_total
    milliseconds = clock.tick(fps_out)
    playtime_total += milliseconds / 500.0
    """
    global mx, my
    mx, my = pygame.mouse.get_pos()


pprint.pprint(locals())


# Meter el sistema de botones y menus a una clase por favor :)
def options_menu():
    """Meca Menu inventario
    TODO
    Crear un rectangulo HW al 75%
    Transparentar el rectangulo
    Dibujar barra superior con titulo
    distinguir con otro color

    Dibujar pestanias
    Inventario personaje | opciones
    """
    global click
    click = False
    audio_effect('menu')
    while True:

        screen.fill(('black'))

        active_stats()

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
        # print(point)
        btn_draw(button_1, point, ('blueviolet'), (255, 100, 100))
        btn_draw(button_2, point, (100, 100, 100), (255, 100, 100))
        btn_draw(button_back, point, (100, 0, 100), (255, 100, 100))

        # all_sprites = pygame.sprite.Group()
        # player_one = Player()
        # all_sprites.add(player_one)

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

        pygame.display.update()
        # time_show()
        pygame.display.set_caption("Local Market » " + str(fps))
        # pygame.display.update()


# ############################################################################
# Inicio del juego
# ############################################################################
def main_menu():
    """Meca Menu inventario. 
    TODO.
    Crear un rectangulo HW al 75%. 
    Transparentar el rectangulo. 
    Dibujar barra superior con titulo. 
    distinguir con otro color.

    Dibujar pestanias. 
    Inventario personaje | opciones. 
    """
    global mx, my, tnow, click

    click = False
    while True:

        screen.fill('lightgray')

        # Estadisticas de casi todo...
        active_stats()

        # ####################################################################
        # Range colitions
        # ####################################################################

        # pygame.draw.rect(screen, 'blue', (350, 20, 120, 100), 1)
        # pygame.draw.rect(screen, 'green', (400, 60, 120, 100), 4)
        # pygame.draw.rect(screen, 'red', (450, 100, 120, 100), 8)

        # ####################################################################

        draw_text('Menu MK2', font, (255, 255, 255), screen, 20, 20)

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

        click = False

        # 3.- Se actualiza la pantalla
        pygame.display.update()
        pygame.display.set_caption("Local Market » " + str(tnow[0]))
        # pygame.display.update()
        clock.tick(fps)
    
    
# ############################################################################
# Loop Principal
# ############################################################################

def main_game():
    """Función principal del juego"""

    # Guardar posicion
    global tnow, mx, my, t0, str_time, stats

    moving = False
    running = True  # Activador del menu
    der = 0  # Restableciendo el movimiento.
    # Bucle principal
    while running:
        screen.fill('black')

        # Renderizar el piso
        background.update(screen, (player.bg[0], player.bg[1]))

        stats['frame_counter'] += 1
        
        # Estadisticas
        active_stats()
        

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE and key_press['F4_key'] == True:
                    # stores_vars = []
                    # for i in len(store_group.spritedict):
                    #     stores_vars.append(store_group.spritedict[i])

                    # with open('storevars.json',"w") as f:
                    #     json.dump(stores_vars, f, indent=4, sort_keys=True)

                    with open('savegame.json', "w") as f:
                        json.dump(player.vars, f, indent=4, sort_keys=True)

                if event.key == K_ESCAPE:
                    key_press["TAB_key"] = False
                    audio_effect('menu')
                    main_menu()

            # Movimiento del personaje.
                if event.key in (K_UP, K_w):
                    player.vars['up'] = True
                    key_press["TAB_key"] = False
                if event.key in (K_DOWN, K_s):
                    player.vars['down'] = True
                    key_press["TAB_key"] = False
                if event.key in (K_LEFT, K_a):
                    player.vars['left'] = True
                    key_press["TAB_key"] = False
                if event.key in (K_RIGHT, K_d):
                    player.vars['right'] = True
                    key_press["TAB_key"] = False
            elif event.type == KEYUP:
                if event.key in (K_UP, K_w):
                    player.vars['up'] = False
                if event.key in (K_DOWN, K_s):
                    player.vars['down'] = False
                if event.key in (K_LEFT, K_a):
                    player.vars['left'] = False
                if event.key in (K_RIGHT, K_d):
                    player.vars['right'] = False

                # resetear el tiempo
                if event.key == K_F5:  # Reset Time
                    key_press["F5_key"] = True
                    tnow[1] = False

                # Abrir el menu transparente, crear un evento de menus....
                if event.key == K_TAB and key_press["TAB_key"] == False:
                    key_press["TAB_key"] = True
                elif event.key == K_TAB and key_press["TAB_key"]:
                    key_press["TAB_key"] = False

                # Abctivar-Descartivar estadisticas
                if event.key == K_F4 and key_press["F4_key"] == False:
                    key_press["F4_key"] = True
                elif event.key == K_F4 and key_press["F4_key"]:
                    key_press["F4_key"] = False


            if event.type == MOUSEBUTTONDOWN and key_press["F4_key"]:
                if player.rect.collidepoint(event.pos):
                    print('player')
                    moving = True
                if store.rect.collidepoint(event.pos):
                    moving = True
                    print('shop')
            elif event.type == MOUSEBUTTONUP and key_press["F4_key"]:
                moving = False
            elif event.type == MOUSEMOTION and moving and key_press["F4_key"]:
                #Moviendo direccion del personaje con el mouse
                if player.rect.collidepoint(event.pos):
                    player.control(event.rel[0],event.rel[1])
                    if event.rel[0] > 0:
                        player.vars['last_dir'] = 'right'
                    if event.rel[0] < 0:
                        player.vars['last_dir'] = 'left'
                    if event.rel[1] > 0:
                        player.vars['last_dir'] = 'down'
                    if event.rel[1] < 0:
                        player.vars['last_dir'] = 'up'
                    # debug(player.rect)
                elif store.rect.collidepoint(event.pos):
                    store.control(event.rel[0],event.rel[1])
                    store.debug(store.rect)
                # print(event.rel)

        if key_press['F4_key']:
            player.debug('collider')
            # shop.debug(store.rect)
            run_time()

            # Muestra la ubicacion del juagor
            textra(screen, f"Player_loc: x({player.movex:4.3f}), y({player.movey:4.3f})", (20, 40), 'black', 'black', 1, None, 'white', 5,5,5,5)
            # Muestra el mouse
            textra(screen, f"Mouse: x({mx:4.3f}), y({my:4.3f})", (20, 60), 'black', 'black', 1, None, 'white', 5,5,5,5)
            str_dia = str_time['dia']
            textra(screen, f'{str_dia} dias {tnow[0]:6.2f}',(20, 80), 'black', 'black', 1, None, 'white', 5,5,5,5)
            # Muestra la hora real.
            textra(screen, f'Hora: {hora_real}', (50+(W/2), 34), 'black', 'black', 1, None, 'white', 5,5,5,5)
            # Muestra el momento del dia
            textra(screen, '{}'.format(str_time['moment_time']), (50+(W/2), 55), 'black', 'black', 1, None, 'white', 5,5,5,5)
            textra(screen, f'{vday}', (50+(W/2), 75), 'black', 'black', 1, None, 'white', 5,5,5,5)



        # renderizar las tiendas
        store_group.update()
        store_group.draw(screen)

        # renderizar jugador
        player_group.update()
        player_group.draw(screen)

        # Abrir menu items
        if key_press["TAB_key"]:
            menu.show(screen)

        # if pygame.sprite.groupcollide(player_group, store_group, False, False):
        if pygame.sprite.groupcollide(player_group, store_group, False, False):
            player.debug(True)
            # player.()
        else:
            audio_effect('menu')


        time_control()
        # 3.- Se actualiza la pantalla
        pygame.display.update()
        pygame.display.set_caption("Local Market » {:3.2f}".format(tnow[0]))
        # pygame.display.update()


if __name__ == '__main__':

    # ############################################################################
    # Loading Starting System...
    # ############################################################################
    # pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
    poswin = poswin(200, 200)
    pygame.init()
    # screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    fps = 60.0

    # Tiempo, horas etc.
    clock = pygame.time.Clock()
    t0 = time.time()
    tnow = [0, True]
    tfull = 720
    vday = 0.0
    hora_real = 0

    # Fuente
    font = pygame.font.SysFont('consolas', 12, bold=True)

    count = None  # Global
    playtime_total = None  # Global
    mx, my = 0, 0

    # Carga de sprites
    # Fondo
    background = Background() 
    menu = Menu()
    # Tiendas
    store = Store((0,0))
    store_group = pygame.sprite.Group(store)

    # Jugador/Personaje
    player = Player()
    player_group = pygame.sprite.Group(player)


    # Declaración de constantes y variables
    str_time = {'hora': 60, 'seg': 0, 'dia': 0, 'tick': 3141569, 'start': 'start', 'moment_time': '?' }
    key_press = {"TAB_key": False, 'F4_key': False, "p_key": False, }
    stats = {"frame_counter": 0, "extras": '',}

    # Cargando el juego :)
    audio_effect('start')
    main_menu()
