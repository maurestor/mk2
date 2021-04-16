#/usr/bin/python
# -*- coding:utf-8 -*-
# 

import pygame
from pygame.locals import *
import os, random, sys, math
from random import randrange

W, H = 1024, 768
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

 # Declaración de constantes y variables
str_time = {'hora': 60, 'seg': 0, 'dia': 0, 'tick': 3141569, 'start': 'start', 'moment_time': '?' }
key_press = {"TAB_key": False, 'F4_key': False, "p_key": False, }
stats = {"frame_counter": 0, "extras": '',}


def asset(folder_asset=None, file_asset='file.old.png'):
    """Busca la ruta absoluta de la carpeta \'assets\' en el OS actual

    `Params`:
    folder_asset: str
    file_asset: str

    Devuelve la imagen/audio/sprite/video/midi del juego.
    """
    source_dir_file = os.path.dirname(os.path.dirname(__file__))
    # print(source_dir_file)
    if folder_asset == None:
    # Carga de archivos, buscar asset()
        path_asset = os.path.join(source_dir_file, '/', file_asset)
    else:
        path_asset = os.path.join(source_dir_file, folder_asset+'/', file_asset)
    # print(path_asset)
    
    return path_asset


def poswin(horizontal=50, vertical=50):
    """Posiciona la ventana aleatoriamente dentro de un rango seleccionado
    
    mas caracteristicas
    """
    # if horizontal == 30 and vertical == 30:
    #     pass
    # else:
    #     x = horizontal = random.randint(30, horizontal)
    #     y = vertical = random.randint(30, vertical)

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (horizontal,vertical)



def pygexit():
    """Salir definitivamente del prigrama y cerrar la aplicacion del sistema"""
    pygame.quit()
    sys.exit()


def fontxtra(font_name:str, size:int):
    """Genera nombre y tamanio de la fuente"""
    font = pygame.font.SysFont(font_name, size)
    return font

def textrabr(tl, tr, bl, br):
    border = []
    border.append(tl)
    border.append(tr)
    border.append(bl)
    border.append(br) 
    return border

def textra(screen, text='text here...', pos=[0, 0], color='gold', brcolor=None, twidth=0, bgcoltext=None, bgcolor=None, tl=0, tr=0, bl=0, br=0):
    """Renderiza texto, opcional border.

    """
    font = fontxtra('comicoro', 20)

    # if bgcoltext is not None:
    #     texto = font.render(text, True, color, bgcoltext)
    # else:
    texto = font.render(text, True, color)

    texto_rect = texto.get_rect()
    border = textrabr(tl,tr,bl,br)
    # print(border)
    # for k, w in kwargs:
    #     border = []
    #     border.append(w)
    # print(border)
    # Si el color es agregado se agrega el marco de color.
    if bgcolor is not None:
        pygame.draw.rect(screen, bgcolor, (pos[0]-3,
                                       pos[1],
                                       texto_rect.width+4,
                                       texto_rect.height), 0,
                                       int(border[0]),
                                       int(border[1]),
                                       int(border[2]),
                                       int(border[3]))

    screen.blit(texto, (pos[0], pos[1]))

    if brcolor is not None:
        pygame.draw.rect(screen, brcolor, (pos[0]-3,
                                       pos[1],
                                       texto_rect.width+4,
                                       texto_rect.height), twidth,
                                       int(border[0]),
                                       int(border[1]),
                                       int(border[2]),
                                       int(border[3]))


# ############################################################################
# Funciones de debugeo
# ############################################################################

def show_fonts():
    """ Muestra una lista de las fuentes del OS """
    fonts = pygame.font.get_fonts()
    print(len(fonts))
    for f in fonts:
        print(f)


class ActionBadges:
        def __init__(self):
            '''Devuelve aleatoriamente un nombre de actionbadges'''
            self.actionbadges = ['interrogation','exclamation', 'bill','good_badge','normal_badge', 'regular_badge','bad_badge', 'premium_badge','lux_badge']
            self.actionbadges_rand = random.randrange(0,len(self.actionbadges))
            # return actionbadges_rand
            self.actionbadge = self.actionbadges[self.actionbadges_rand]

        def drawbadge(self):
            return self.actionbadge

        def __str__(self):
            return self.actionbadge

def character_selected():
    '''Selecciona el tipo de personaje a mostrar'''
    diccionario = ['verde', 'azul', 'rojo', 'nanaranjas']
    char = random.randrange(0, len(diccionario))
    return diccionario[char]
