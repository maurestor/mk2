#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame
from pygame import examples
import os
import sys
import time
from pygame.locals import *
from datetime import datetime
import json


from libs.pygamextras import *
from libs.player import Player, PlayerUi
from libs.stores import Stores, StoreBg
from libs.bg_ui_elements import Background, Stats, UserInterface
from libs.menus import Menu
from libs.particles import ParticlesPrinciple


import pprint
# from libs.items import Items


"""Caracteristicas por agregar
    
    USA DE TODO.
    NO CAMBIAR LO QUE YA FUNCIONA!
    AUN MÍNIMO QUE PAREZCA CADA DETALLE ES MUY IMPORTANTE!
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
    main_game()
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
    global tnow, mx, my, t0, str_time, stats, playerui

    contador = 0
    moving = False
    running = True  # Activador del menu
    der = 0  # Restableciendo el movimiento.
    # Bucle principal
    while running:
        screen.fill('black')
        # Renderizar el piso
        # background.update(screen, (player.bg[0], player.bg[1]))
        background.tiles((player.bg[0], player.bg[1]))

        stats['frame_counter'] += 1

        # Estadisticas
        active_stats()
        # mx, my = pygame.mouse.get_pos()

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
                        player_dump = []
                        player_dump.append(player.vars)
                        player_dump.append(player.exis)

                        json.dump(player_dump, f, indent=4, sort_keys=True)

                if event.key == K_ESCAPE:
                    key_press["TAB_key"] = False
                    audio_effect('menu')
                    quit()
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

            # Moviendo la rueda del raton
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:
                    contador += 1
                    print('adelante'+ str(contador))
                elif event.button == 5:
                    contador += 1
                    print('atras' + str(contador))
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
                    store_bg.control(event.rel[0],event.rel[1])
                # print(event.rel)

            # Iniciando el evento particulas
            if event.type == PARTICLE_EVENT:
                particle1.add_particles([player.rect.x, player.rect.y])


        if key_press['F4_key']:
            player.debug()
            store.debug()
            store_bg.debug()
            # Desactivar particulas
            # particle1.emit()
            run_time()


        # renderizar las tiendas
        store_group.update()
        store_group.draw(screen)

        # renderizar jugador
        player_group.update()
        player_group.draw(screen)


        # Abrir menu items
        if key_press["TAB_key"]:
            menu.show(screen)

        #Colisiones checar esta declaracion...
        # Importante con el uso de las mecanicas y los sprites....
        # collidegroup = pygame.sprite.groupcollide(player_group, store_group, False, False)
        colliderect = pygame.Rect.colliderect(player.rect, store_bg.rect)

        if colliderect:
            # if playerui == 'exclamation':
            #     player.debug(playerui)
            # else:
            store.debug()
            player.debug(playerui.drawbadge())
        elif not colliderect:
            # Reiniciando el contador aleatorio.
            playerui = ActionBadges()
            # audio_effect('menu', 0.5)

        # number = 3
        # for x in range(number):
        #     for y in range(number):
        #         pygame.draw.rect(screen, 'orange', ((x*256),(y*256), 128, 128), 1)

        # Renderizando la interfaz de usuario
        statistic=Stats()
        Ui.gui()

        #Renderizar particulas
        

        time_control()
        pygame.display.update()


if __name__ == '__main__':

    # ###########################################F#################################
    # Loading Starting System...
    # ############################################################################
    # pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
    
    pygame.init()
    # screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    pygame.display.set_caption("Local Market ")

    fps = 60.0

    # Tiempo, horas etc.
    clock = pygame.time.Clock()

    count = None  # Global
    playtime_total = None  # Global


    background = Background()
    menu = Menu()

    # Cargando el fondo de la tienda
    #Cargando la tienda
    store = Stores([200,200])
    store_bg = StoreBg([store.rect.x, store.rect.y])
    # Loading background, please pos before the background
    
    store_group = pygame.sprite.Group(store)
    store_group.add(store_bg)
    # store_collider = pygame.sprite.Group(store.collide_rect)
    
    player = Player(character=character_selected(), speed=6)
    # player_collider = pygame.sprite.Group(player.collide_rect)
    player_group = pygame.sprite.Group(player)
    
    everything = pygame.sprite.Group(player)
    everything.add(store)
    # everything.add(background)

    # Cargando la interfaza de usuario
    Ui = UserInterface()

    # Particulas effects, efectos
    particle1 = ParticlesPrinciple()
    
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 25)


    audio_effect('start')
    main_menu()
