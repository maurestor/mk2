#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pygame import sprite
from overlapping import Actor
import pygame
from pygame import display
from pygame.draw import rect
# from pygame import examples
# import os
# import sys
# import time
from pygame.locals import *
# from datetime import datetime
import json

from pygame.surface import Surface

import pygame_gui # Explicit import

# Define Color Constants
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT_GRAY = (211, 211, 211) # Standard light gray
COLOR_GRAY_TEXT = (100, 100, 100) # Used for button text
COLOR_GRAY_BUTTON = (100, 100, 100) # Used for button background
COLOR_HOVER_BUTTON = (150, 150, 150) # Used for button hover
COLOR_BLUE_VIOLET_BUTTON = ('blueviolet')
COLOR_RED_HOVER_BUTTON = (255, 100, 100)
COLOR_MENU_BG = COLOR_BLACK
COLOR_MAIN_MENU_BG = COLOR_LIGHT_GRAY
COLOR_MENU_TITLE = COLOR_WHITE


from libs.pygamextras import *
from libs.player import Player
# from libs.stores import Stores, StoreBg
from libs.bg_ui_elements import Background, Stats, UserInterface
from libs.menus import Menu, MenuManager # Import MenuManager
from libs.particles import ParticlesPrinciple
# from libs.dialogues import DialogueBox


import pprint
# from libs.items import Items


# Helper function (keep if still needed elsewhere, or remove if specific to old buttons)
# def btn_draw(button_rect, mouse_pos, default_color, hover_color):
#     if button_rect.collidepoint(mouse_pos):
#         pygame.draw.rect(screen, hover_color, button_rect)
#     else:
#         pygame.draw.rect(screen, default_color, button_rect)

def options_menu():
    """Refactored Options Menu using MenuManager."""
    global mx, my, assets # mx, my still needed for hover detection passed to MenuManager
    # click global is no longer the primary mechanism for button clicks

    audio_effect('menu', assets=assets)

    options_menu_manager = MenuManager()

    # Button actions defined below use these colors via constants now
    # text_color = COLOR_WHITE (already used by default in MenuManager button creation)
    # button_color = COLOR_GRAY_BUTTON
    # hover_color = COLOR_HOVER_BUTTON
    # action_button_color = COLOR_BLUE_VIOLET_BUTTON
    # action_hover_color = COLOR_RED_HOVER_BUTTON

    # Define actions for buttons
    def option_1_action():
        audio_effect('menu', assets=assets)
        print("Option 1 clicked") # Placeholder action

    def option_2_action():
        audio_effect('menu', False, 0.1, assets=assets)
        print("Option 2 clicked") # Placeholder action

    def back_to_main_menu_action():
        audio_effect('menu', assets=assets)
        main_menu()

    # Add buttons to the manager
    options_menu_manager.add_button(pygame.Rect(50, 100, 190, 45), "Button 1", assets['font_comicoro_24'], COLOR_WHITE, COLOR_BLUE_VIOLET_BUTTON, COLOR_RED_HOVER_BUTTON, option_1_action)
    options_menu_manager.add_button(pygame.Rect(50, 150, 190, 45), "Button 2", assets['font_comicoro_24'], COLOR_WHITE, COLOR_GRAY_BUTTON, COLOR_HOVER_BUTTON, option_2_action)
    options_menu_manager.add_button(pygame.Rect(50, 200, 190, 45), "Volver", assets['font_comicoro_24'], COLOR_WHITE, COLOR_GRAY_BUTTON, COLOR_HOVER_BUTTON, back_to_main_menu_action)

    while True:
        mx, my = pygame.mouse.get_pos()
        screen.fill(COLOR_MENU_BG) # Use constant for options menu background
        active_stats() # Assuming this is a general stats display
        draw_text('Menu Options', assets['font_comicoro_24'], COLOR_MENU_TITLE, screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu() # Or main_game() depending on desired UX

            options_menu_manager.handle_event(event)

        options_menu_manager.draw(screen, (mx, my))

        pygame.display.update()
        pygame.display.set_caption("Local Market » Options")
        clock.tick(fps)


# ############################################################################
# Inicio del juego
# ############################################################################
def main_menu():
    """Refactored Main Menu using MenuManager."""
    global mx, my, tnow, assets # tnow usage needs clarification for caption, click is less relevant

    main_menu_manager = MenuManager()

    # Button actions defined below use these colors via constants now
    # text_color = COLOR_WHITE
    # button_color = COLOR_GRAY_BUTTON
    # hover_color = COLOR_HOVER_BUTTON
    # jugar_button_color = COLOR_BLUE_VIOLET_BUTTON
    # jugar_hover_color = COLOR_RED_HOVER_BUTTON

    # Define actions
    def start_game_action():
        audio_effect('menu', assets=assets)
        main_game()

    def options_menu_action():
        audio_effect('menu', assets=assets)
        options_menu()

    def exit_game_action():
        audio_effect('menu', assets=assets)
        exit()

    # Add buttons
    main_menu_manager.add_button(pygame.Rect(50, 100, 190, 45), "Jugar", assets['font_comicoro_24'], COLOR_WHITE, COLOR_BLUE_VIOLET_BUTTON, COLOR_RED_HOVER_BUTTON, start_game_action)
    main_menu_manager.add_button(pygame.Rect(50, 150, 190, 45), "Opciones", assets['font_comicoro_24'], COLOR_WHITE, COLOR_GRAY_BUTTON, COLOR_HOVER_BUTTON, options_menu_action)
    main_menu_manager.add_button(pygame.Rect(50, 200, 190, 45), "Salir", assets['font_comicoro_24'], COLOR_WHITE, COLOR_GRAY_BUTTON, COLOR_HOVER_BUTTON, exit_game_action)

    while True:
        mx, my = pygame.mouse.get_pos()
        screen.fill(COLOR_MAIN_MENU_BG) # Use constant for main menu background
        active_stats() # Assuming this is a general stats display
        draw_text('Menu MK2', assets['font_comicoro_24'], COLOR_MENU_TITLE, screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    exit() # Exit from main menu on ESC
                if event.key == K_r:
                    # tnow = 0 # This needs tnow to be properly defined/initialized
                    print("R pressed - tnow reset functionality placeholder")

            main_menu_manager.handle_event(event)

        main_menu_manager.draw(screen, (mx, my))

        pygame.display.update()
        # pygame.display.set_caption("Local Market » " + str(tnow[0])) # tnow usage needs to be clear
        pygame.display.set_caption("Local Market") # Simplified caption
        clock.tick(fps)


# ############################################################################
# Loop Principal
# ############################################################################
"""Caracteristicas por agregar
    (Omitted for brevity in this example, but it's in the actual file)
"""

def main_game():
    """Función principal del juego.
    NOTE: This function is very long and could benefit from further refactoring
    into smaller functions or classes for better organization.
    """

    global tnow, mx, my, t0, str_time, stats, badge, time_delta, assets # Ensure these globals are correctly managed

    contador = 0
    moving = False
    running = True
    der = 0

    player = Player(assets['player_anim_sheet'], (W//2,H//2)) # Use pre-loaded asset
    # Actor is the parent of Player, Player's __init__ should pass the image_surface to Actor's __init__
    # So, direct instantiation of Actor here for the player sprite is not needed if Player handles it.
    sprites = YAwareGroup(
        player
        # Actor(assets['player_anim_sheet'], (W//2,H//2)) # This was the duplicate loading
    )
    player_group = pygame.sprite.Group(player)

    while running:
        screen.fill('black')
        bg.update(screen, (player.bg[0], player.bg[1]))

        for id2, imp in enumerate(bg.list_imp):
            store_pos = (imp[0]+player.bg[0], imp[1]+player.bg[1])
            tot_price = []
            tot_items = []

            for id, store in enumerate(bg.list_store):
                if id == id2:
                    store.movement(store_pos)
                tot_price.append(store.vars['total_store'])
                tot_items.append(store.vars['total_items'])

            for id3, store_bg_instance in enumerate(bg.list_store_bg): # Renamed for clarity
                if id2 == id3:
                    store_bg_instance.movement(store_pos)

        time_delta = clock.tick(60)/1000.0
        stats['frame_counter'] += 1
        active_stats()

        for event in pygame.event.get():
            player.get_event(event)
            for store in bg.list_store:
                store.get_event(event)

            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE and key_press['F4_key'] == True:
                    print('Guardando el juego!!! Savegame!!! ;)')
                    print('####################################\n')
                    save_path = 'savegame.json'
                    try:
                        # NOTE: Savegame logic manually constructs a list.
                        # Consider refactoring to use a dictionary for better structure
                        # or dedicated save/load functions within classes.
                        with open(save_path, "w") as f:
                            game_dump = []
                            game_dump.append('Player vars')
                            game_dump.append(player.vars)
                            game_dump.append('Player items')
                            game_dump.append(player.items.list)
                            for store_instance in bg.list_store:
                                game_dump.append(f'Store {store_instance} vars')
                                game_dump.append(store_instance.vars)
                                game_dump.append(store_instance.items.list)
                            json.dump(game_dump, f, indent=4, sort_keys=True)
                        print(f"Game saved to {save_path}")
                    except Exception as e:
                        print(f"Error saving game: {e}")

                if event.key == K_ESCAPE:
                    key_press["TAB_key"] = False
                    audio_effect('menu', assets=assets)
                    main_menu()

                if event.key in (K_UP, K_w): player.vars['up'] = True; key_press["TAB_key"] = False
                if event.key in (K_DOWN, K_s): player.vars['down'] = True; key_press["TAB_key"] = False
                if event.key in (K_LEFT, K_a): player.vars['left'] = True; key_press["TAB_key"] = False
                if event.key in (K_RIGHT, K_d): player.vars['right'] = True; key_press["TAB_key"] = False
            elif event.type == KEYUP:
                if event.key in (K_UP, K_w): player.vars['up'] = False
                if event.key in (K_DOWN, K_s): player.vars['down'] = False
                if event.key in (K_LEFT, K_a): player.vars['left'] = False
                if event.key in (K_RIGHT, K_d): player.vars['right'] = False
                if event.key == K_F5: key_press["F5_key"] = True # tnow[1] = False
                if event.key == K_TAB and key_press["TAB_key"] == False: key_press["TAB_key"] = True
                elif event.key == K_TAB and key_press["TAB_key"]: key_press["TAB_key"] = False
                if event.key == K_F4 and key_press["F4_key"] == False: key_press["F4_key"] = True
                elif event.key == K_F4 and key_press["F4_key"]: key_press["F4_key"] = False

            if event.type == MOUSEBUTTONDOWN and key_press["F4_key"]:
                if player.rect.collidepoint(event.pos): moving = True
                for store_instance in bg.list_store:
                    if store_instance.rect.collidepoint(event.pos): moving = True; # print('shop', id(store_instance))

            if event.type == MOUSEBUTTONUP and key_press["F4_key"]: moving = False
            elif event.type == MOUSEMOTION and moving and key_press["F4_key"]:
                if player.rect.collidepoint(event.pos):
                    player.control(event.rel[0],event.rel[1])
                    if event.rel[0] > 0: player.vars['last_dir'] = 'right'
                    if event.rel[0] < 0: player.vars['last_dir'] = 'left'
                    if event.rel[1] > 0: player.vars['last_dir'] = 'down'
                    if event.rel[1] < 0: player.vars['last_dir'] = 'up'
                for store_instance in bg.list_store:
                    if store_instance.rect.collidepoint(event.pos): store_instance.control(event.rel[0],event.rel[1])
                # This logic for store_bg_instance seemed potentially buggy, needs review if it's still relevant
                # for store_bg_instance in bg.list_store_bg:
                #     if store_instance.rect.collidepoint(event.pos):
                #         store_bg_instance.control(event.rel[0],event.rel[1])

            if event.type == PARTICLE_EVENT: particle1.add_particles([player.rect.x, player.rect.y])
            ui_manager.process_events(event)

        if key_press['F4_key']:
            for store_instance in bg.list_store: store_instance.interaction()
            for store_bg_instance in bg.list_store_bg: store_bg_instance.interaction()
            player.interaction()
            run_time()

        bg.store_group.update()
        bg.store_group.draw(screen)
        player_group.update()
        player_group.draw(screen)

        for id, store_bg_instance in enumerate(bg.list_store_bg):
            colliderect = pygame.Rect.colliderect(player.collide_rect, store_bg_instance.rect)
            if colliderect:
                for id2, store_instance in enumerate(bg.list_store):
                    if id == id2: store_instance.dialogue_box()
                player.dialogue_box()
            elif not colliderect:
                badge = ActionBadges()

        if key_press["TAB_key"]: menu.show()
        statistic=Stats()
        tot_price.append(player.vars['total_store'])
        tot_items.append(player.vars['total_items'])
        # player_tot = player.vars['total_items'] # player_tot not used
        # print(f'Player {player.vars["total_items"]}') # Avoid printing every frame
        ui.gui(sum_totals(tot_price), sum_totals(tot_items))
        time_control()
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    pygame.display.set_caption("Local Market ")

    app_icon_surface = pygame.image.load(asset('assets/img', 'icon-32.png')) # Load separately for clarity
    pygame.display.set_icon(app_icon_surface)

    fps = 60.0

    try:
        game_font = pygame.font.SysFont('comicoro', 24)
    except pygame.error:
        print("Comicoro font not found, using default system font.")
        game_font = pygame.font.Font(None, 30)

    # Asset Loading
    assets = {
        'player_anim_sheet': pygame.image.load(asset('assets/img', 'player-anim.png')).convert_alpha(),
        'stores_anim_sheet': pygame.image.load(asset('assets/img', 'stores-anim.png')).convert_alpha(),
        'floor_image': pygame.image.load(asset('assets/img', 'floor.png')).convert_alpha(),
        'icon32': app_icon_surface, # Use the loaded surface
        'font_comicoro_24': game_font, # Use the loaded font
        'sound_menu_select': pygame.mixer.Sound(asset('assets/music', 'effect_nicholasdaryl_swing.wav')),
        'sound_start': pygame.mixer.Sound(asset('assets/music', 'desktop-login.ogg')),
        'sound_exit': pygame.mixer.Sound(asset('assets/music', 'desktop-logout.ogg')),
    }
    assets['sound_menu_select'].set_volume(0.5)
    assets['sound_start'].set_volume(0.1)
    assets['sound_exit'].set_volume(0.5)

    # Global variables
    mx, my = 0, 0
    tnow = [0, False]
    clock = pygame.time.Clock()
    key_press = {"TAB_key": False, "F4_key": False, "F5_key": False}
    stats = {'frame_counter': 0}
    t0 = pygame.time.get_ticks()
    str_time = ""
    badge = None
    time_delta = 0.0

    # Pass assets to Background constructor
    bg = Background(assets)
    bg.tiles()

    menu = Menu()
    ui = UserInterface()
    particle1 = ParticlesPrinciple()

    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 25)

    # Pass assets to audio_effect
    audio_effect('start', assets=assets)
    main_menu()
