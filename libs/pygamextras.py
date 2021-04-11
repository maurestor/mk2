#/usr/bin/python
# -*- coding:utf-8 -*-
# 

import pygame
from pygame.locals import *
import os, random, sys, math

W, H = 800, 600


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
    if horizontal == 30 and vertical == 30:
        pass
    else:
        horizontal = random.randint(30, horizontal)
        vertical = random.randint(30, vertical)

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (horizontal, vertical)


def pygexit():
    """Salir definitivamente del prigrama y cerrar la aplicacion del sistema"""
    pygame.quit()
    sys.exit()


def fontxtra(font_name:str, size:int):
    """Genera nombre y tamanio de la fuente"""
    font = pygame.font.SysFont(font_name, size)
    return font

def textrabr(tl, tr, bl, br):
    b = []
    b.append(tl)
    b.append(tr)
    b.append(bl)
    b.append(br) 
    return b

def textra(screen, text='text here...', pos=[0, 0], color='gold', brcolor=None, twidth=0, bgcoltext=None, bgcolor=None, tl=0, tr=0, bl=0, br=0 ):
    """Renderiza texto, opcional border.

    """
    font = fontxtra('comicoro', 18)

    # if bgcoltext is not None:
    #     texto = font.render(text, True, color, bgcoltext)
    # else:
    texto = font.render(text, True, color)

    texto_rect = texto.get_rect()

    border = textrabr(tl,tr,bl,br)
    print(border)
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


