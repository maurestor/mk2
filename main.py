#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from pygame import display
# from pygame import examples
# import os
# import sys
# import time
from pygame.locals import *
# from datetime import datetime
import json

from pygame.surface import Surface


from libs.pygamextras import *
from libs.player import Player
# from libs.stores import Stores, StoreBg
from libs.bg_ui_elements import Background, Stats, UserInterface
from libs.menus import Menu
from libs.particles import ParticlesPrinciple
# from libs.dialogues import DialogueBox


import pprint
# from libs.items import Items



"""Caracteristicas por agregar
    
    CONTINUA CON OTRA COSA CUANDO NO PUEDAS CON ALGO BASTANTE COMPLEJO
    USA DE TODO.
    NO CAMBIAR LO QUE YA FUNCIONA!
    AUN MÍNIMO QUE PAREZCA CADA DETALLE ES MUY IMPORTANTE!
    NO TE CASES CON LAS COSAS!
    
    # Ten cuidado de usar la linea 1 incorrectamente, en linux causa conflicto el interprete
    
    ✔ Colisiones
        
    Sistema de dialogos GUI ya esta realizada por la mitad

    Sistema de logros!!!

    ✔ Sistema de movimiento 🏃‍♂️
    
    ✔ Sistema de efectos - particulas
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
        dimensiones
        tiempos reloj
    
    Fuentes propuestas:
        Nokia
        Comicoro
        pf tempesta seven
        retroville
        retrogaming

    Usare PyGameGUI

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
    global tnow, mx, my, t0, str_time, stats, badge, time_delta

    contador = 0
    moving = False
    running = True  # Activador del menu
    der = 0  # Restableciendo el movimiento.
    
    #Cargando sistema de dialogos?
    
    #Carga los tile con anterioridad...
    bg.tiles()

    while running:
        screen.fill('black')
        # Renderizar el piso
        bg.update(screen, (player.bg[0], player.bg[1]))

        time_delta = clock.tick(60)/1000.0

        # dialogue = DialogueBox()

        stats['frame_counter'] += 1

        # Estadisticas
        active_stats()
        #posicion global del mouse
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Enviando eventos a dialogue

            # Creando loop de mapa stores
            for store in bg.list_store:
                store.get_event(event)
            # store2.get_event(event)
            # player.get_event(event)
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE and key_press['F4_key'] == True:
                    # stores_vars = []
                    # for i in len(store_group.spritedict):
                    #     stores_vars.append(store_group.spritedict[i])

                    # with open('storevars.json',"w") as f:
                    #     json.dump(stores_vars, f, indent=4, sort_keys=True)
                    print('guardando savegame...')
                    with open('/home/restor/Documents/game-develop/mk2/savegame.json', "w") as f:
                        game_dump = []
                        game_dump.append('Player vars')
                        game_dump.append(player.vars)
                        game_dump.append('Player items')
                        game_dump.append(player.items.item_list)

                        for store in bg.list_store:
                            # game_dump.append(player.exis)
                            game_dump.append(f'Store {id(store)} vars')
                            # game_dump.append(store2.vars)
                            # game_dump.append('Store 2 vars')
                            game_dump.append(store.vars)
                            game_dump.append(store.items.item_list)

                        json.dump(game_dump, f, indent=4, sort_keys=True)

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

            # # Moviendo la rueda del raton
            # if event.type == MOUSEBUTTONDOWN:
            #     if event.button == 4:
            #         contador += 1
            #         print('adelante'+ str(contador))
            #     elif event.button == 5:
            #         contador += 1
            #         print('atras' + str(contador))

            if event.type == MOUSEBUTTONDOWN and key_press["F4_key"]:
                if player.rect.collidepoint(event.pos):
                    print('player')
                    moving = True
                if store.rect.collidepoint(event.pos):
                    for store in bg.list_store:
                        moving = True
                        print('shop')
                # if store2.rect.collidepoint(event.pos):
                #     moving = True
                #     print('shop2')

            if event.type == MOUSEBUTTONUP and key_press["F4_key"]:
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
                    # interaction(player.rect)
                elif store.rect.collidepoint(event.pos):
                    for store in bg.list_store:
                        store.control(event.rel[0],event.rel[1])
                    for store_bg in bg.list_store_bg:
                        store_bg.control(event.rel[0],event.rel[1])
                # elif store2.rect.collidepoint(event.pos): 
                #     store2.control(event.rel[0],event.rel[1])
                #     store_bg2.control(event.rel[0],event.rel[1])
                # print(event.rel)


            # Iniciando el evento particulas
            if event.type == PARTICLE_EVENT:
                particle1.add_particles([player.rect.x, player.rect.y])

            #Eventos de gui
            ui_manager.process_events(event)


        if key_press['F4_key']:
            for store in bg.list_store:
                store.interaction()
            for store_bg in bg.list_store_bg:
                store_bg.interaction()

            # store2.interaction()
            # store_bg2.interaction()

            player.interaction()
            # Desactivar particulas
            # particle1.emit()
            run_time()

        # Checar posision y desplazamiento...
        # for x, store in enumerate(bg.list_store):
        #     for y, imp in enumerate(bg.list_imp):
        #         store.rect.x = (x*128)+imp[0]
        #         store.rect.y = (y*128)+imp[1]
        #         print(imp, store.rect)
        
        # print(player.bg)
        for store_bg in bg.list_store_bg:
            #Colisiones checar esta declaracion...
            # Importante con el uso de las mecanicas y los sprites....
            # collidegroup = pygame.sprite.groupcollide(player_group, store_group, False, False)
            colliderect = pygame.Rect.colliderect(player.rect, store_bg.rect)
            # colliderect2 = pygame.Rect.colliderect(player.rect, store_bg2.rect)
            if colliderect:
                # if badge == 'exclamation':
                #     player.interaction(badge)
                # else:
                # for store in bg.list_store:
                store.interaction()
                player.interaction(badge.drawbadge())
            # elif colliderect2:

            #     # store2.interaction()
            #     player.interaction(badge.drawbadge())


            elif not colliderect:
                # Reiniciando el contador aleatorio.
                badge = ActionBadges()
                # audio_effect('menu', 0.5)

        # store.update(store.control(player.bg[0], player.bg[1]))
        # store2.update(store2.control(player.bg[0], player.bg[1]))
        # renderizar las tiendas
        
        bg.store_group.update()
        bg.store_group.draw(screen)

        # renderizar jugador
        player_group.update()
        player_group.draw(screen)

        # def movement():
        #     movex = store.rect.x + player.bg[0]
        #     movey = store.rect.y + player.bg[1]
        #     pos = [movex, movey]
        #     store.rect.move_ip(movex, movey)
        #     return pos



        # #crear efecto dia noche...
        # daynight = pygame.Surface([W, H], pygame.SRCALPHA, 32)
        # daynight.set_colorkey('white')
        # daynight = daynight.convert_alpha()

        # Abrir menu items
        if key_press["TAB_key"]:
            menu.show()


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

    # ############################################################################
    # Loading Starting System...
    # ############################################################################
    # pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
    
    # pygame.init()
    # screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    pygame.display.set_caption("Local Market ")
    
    app_icon = pygame.image.load(asset('assets/img', 'icon-32.png'))
    pygame.display.set_icon(app_icon)
    
    fps = 60.0
    font = pygame.font.SysFont('comicoro', 12)
    

    count = None  # Global
    playtime_total = None  # Global


    bg = Background()
    menu = Menu()

    
    player = Player(character=character_selected(), speed=6)
    # player_collider = pygame.sprite.Group(player.collide_rect)
    player_group = pygame.sprite.Group(player)
    
    # everything = pygame.sprite.Group(player)
    # everything.add(store)
    # everything.add(background)

    # Cargando la interfaza de usuario
    Ui = UserInterface()
    # Particulas effects, efectos
    particle1 = ParticlesPrinciple()
    
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 25)

    audio_effect('start')
    main_menu()
