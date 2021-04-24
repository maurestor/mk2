#/usr/bin/python
# -*- coding:utf-8 -*-
# 

import pygame
from pygame.locals import *
import time
from datetime import datetime
import os, random, sys, math
from random import randrange

W, H = 1280, 960
screen = pygame.display.set_mode((W, H), pygame.HWACCEL)

mx, my = 0, 0

t0 = time.time()
tnow = [0, True]
tfull = 720
hora_real = 0
vday = 0.0


# Declaración de constantes y variables
str_time = {'hora': 60, 'seg': 0, 'dia': 0, 'tick': 3141569, 'start': 'start', 'moment_time': '?' }
key_press = {"TAB_key": False, 'F4_key': False, "p_key": False, }
stats = {"frame_counter": 0, "extras": ''}


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


def audio_effect(name, stop_time=False, vol=0.5):
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
        pygame.mixer.music.set_volume(0.1)
        sound = pygame.mixer.music.play()

    if name == 'exit' and stop_time:
        pygame.mixer.music.load(asset('assets/music', 'desktop-logout.ogg'))
        pygame.mixer.music.set_volume(vol)
        sound = pygame.mixer.music.play()
        time.sleep(3000)  # sound.get_length())


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


def fontxtra(font_name='comicoro', size=12):
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


def textra(text='text here...', position=[0, 0], textcolor='gold', brcolor=None, twidth=0, bgcoltext=(255,255,255,0), bgcolor=None, tl=0, tr=0, bl=0, br=0):
    """Renderiza texto, opcional border.

    """
    font = fontxtra('comicoro', 20)

    # if bgcoltext is not None:
    #     texto = font.render(text, True, color, bgcoltext)
    # else:
    texto = font.render(text, True, textcolor)

    texto_rect = texto.get_rect()
    border = textrabr(tl,tr,bl,br)
    # print(border)
    # for k, w in kwargs:
    #     border = []
    #     border.append(w)
    # print(border)
    # Si el color es agregado se agrega el marco de color.
    if bgcolor is not None:
        pygame.draw.rect(screen, bgcolor, (position[0]-3,
                                       position[1],
                                       texto_rect.width+4,
                                       texto_rect.height), 0,
                                       int(border[0]),
                                       int(border[1]),
                                       int(border[2]),
                                       int(border[3]))

    screen.blit(texto, (position[0], position[1]))

    if brcolor is not None:
        pygame.draw.rect(screen, brcolor, (position[0]-3,
                                       position[1],
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

diccionario = {'hola':'hello', }

def t(input):
    '''Traductor simple de palabras'''
    for p in diccionario:
        pass
