#/usr/bin/python
# -*- coding:utf-8 -*-
# 

import pygame, pygame_gui
from pygame import mouse
from pygame import display
from pygame.locals import *
import time
from datetime import datetime
import os, random, sys, math
from random import randrange, randint

pygame.init()

print(f"\nMecaro Games X Inc.\n")

W, H = 1280//1.5, 960//1.5
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{0},{0}"
screen = pygame.display.set_mode((int(W), int(H)), flags=HWACCEL|RESIZABLE|DOUBLEBUF|NOFRAME)
mx, my = 0, 0

#inverse_player_movement
# IMP = [0,0]

t0 = time.time()
tnow = [0, True]
tfull = 720
hora_real = 0
vday = 0.0
# Tiempo, horas etc.
clock = pygame.time.Clock()

# Agregando Pygame_GUI
ui_manager = pygame_gui.UIManager((W, H), '/home/restor/Documents/game-develop/mk2/theme.json')

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


def pygexit():
    """Salir definitivamente del prigrama y cerrar la aplicacion del sistema"""
    pygame.quit()
    sys.exit()


class TExtra:
    def __init__(self, text='text here...', position=[0, 0], textcolor='gold', brcolor=None, twidth=0, bgcoltext=(255,255,255,0), bgcolor=None, tl=0, tr=0, bl=0, br=0, surface=screen):
        """Renderiza texto, opcional con borde, color, fondo, color del 
        borde, transparencia, etc

        Falta mejorar esta clase.

        """

        self.fontxtra('comicoro', 20)

        # if bgcoltext is not None:
        #     texto = font.render(text, True, color, bgcoltext)
        # else:
        self.texto = self.font.render(text, True, textcolor)

        self.texto_rect = self.texto.get_rect()

        self.border = []
        self.textrabr(tl,tr,bl,br)
        
        # print(self.border)
        # for k, w in kwargs:
        #     self.border = []
        #     self.border.append(w)
        # print(self.border)
        # Si el color es agregado se agrega el marco de color.
        if bgcolor is not None:
            pygame.draw.rect(surface, bgcolor, (position[0]-3,
                                        position[1],
                                        self.texto_rect.width+4,
                                        self.texto_rect.height), 0,
                                        int(self.border[0]),
                                        int(self.border[1]),
                                        int(self.border[2]),
                                        int(self.border[3]))

        surface.blit(self.texto, (position[0], position[1]))

        if brcolor is not None:
            pygame.draw.rect(surface, brcolor, (position[0]-3,
                                        position[1],
                                        self.texto_rect.width+4,
                                        self.texto_rect.height), twidth,
                                        int(self.border[0]),
                                        int(self.border[1]),
                                        int(self.border[2]),
                                        int(self.border[3]))

    def fontxtra(self, font_name='comicoro', size=12):
        """Genera nombre y tamanio de la fuente"""
        self.font = pygame.font.SysFont(font_name, size)

    def textrabr(self, tl, tr, bl, br):
        self.border.append(tl)
        self.border.append(tr)
        self.border.append(bl)
        self.border.append(br)
        # return border





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
            self.dialogues = ['Hola, ', 'Hey, ', 'Que onda!, ', 'Buen dia, ', "Que tal, "]
            
            self.actionbadges_rand = random.randrange(0,len(self.actionbadges))
            # return actionbadges_rand
            self.actionbadge = self.actionbadges[self.actionbadges_rand]
            
            self.dialogues_rand = random.randrange(0,len(self.dialogues))
            # return actionbadges_rand
            self.dialogues = self.dialogues[self.dialogues_rand]
            

        def drawbadge(self):
            return self.actionbadge

        def drawresponse(self):
            return self.dialogues

        def __str__(self):
            return self.actionbadge

def character_selected():
    '''Selecciona el tipo de personaje a mostrar'''
    diccionario = ['verde', 'azul', 'rojo', 'nanaranjas']
    char = random.randrange(0, len(diccionario))
    return diccionario[char]


def t(input):
    '''Traductor simple de palabras'''
    for p in diccionario:
        pass

class TextColors:
    def __init__(self):
        '''Return color random in a text'''
        self.counter = 0
        self.color0 = self.color1 = self.color2 = (255)

    def colorize(self):
        '''Return color random range'''
        self.counter += 1
        if self.counter >= 5:
            self.counter = 0
            self.color0 = random.randrange(50, 255)
            self.color1 = random.randrange(50, 255)
            self.color2 = random.randrange(50, 255)
        return (self.color0, self.color1, self.color2)


    def render(self, text:str, colorized:bool=False):
        '''Update color &of text every "n" frames per second(1000fps)'''
        # self.counter += 1
        # if self.counter >= 10: #every frame in 1000
        #     self.counter = 0
        #     self.color0 = random.randrange(100, 255)
        #     self.color1 = random.randrange(100, 255)
        #     self.color2 = random.randrange(100, 255)
        if colorized:
            texto = font.render(text, True, self.colorize())
        else:
            # texto = font.render(f'Color {self.counter:.0f}', True, (self.color0, self.color1, self.color2))
            texto = font.render(text, True, (255,255,255))
        screen.blit(texto, [W//2-120, H//2-100])

#Movimiento Bounce :)
moving = [0, False]
def bounce(limit_a, limit_b, speed):
    '''Rebote de limite lineal, control de tiempo-espacio'''
    if moving[0] < limit_a and moving[1] == True:
        moving[0] += speed
        if moving[0] >= limit_b:
            moving[1] = False
    elif moving[1] == False and moving[0] <= limit_b:
        moving[0] -= speed
        if moving[0] <= -limit_a:
            moving[1] = True
    return moving[0]

def random_pixel_color(surface):
    rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
    rand_col_ = (randint(0, 255), randint(0, 255), randint(0, 255))
    
    for _ in range(1000):
        rand_pos = (randint(0, W-1), randint(0, H-1))
        rand_pos2 = (randint(0, W-1), randint(0, H-1))
        surface.set_at(rand_pos, rand_col)
        surface.set_at(rand_pos2, rand_col_)


class CubeRotate:
    def __init__(self):
        '''Instancea la clase para rotar un cubo'''
        self.surf_cube = pygame.Surface((100, 100), flags=SRCALPHA)
        self.surf_cube.fill(('green'))
        #Se hace copia, rect y se trabaja con ellos.
        self.rot_cube = self.surf_cube
        self.rect_cube = self.surf_cube.get_rect()
        
        self.angle = 0

    def cube(self, color, size):
        self.surf_cube = pygame.Surface((size), flags=SRCALPHA)
        self.surf_cube.fill((color))
        
    def rotate(self, color, rect, surface, debug=0):
        '''Rota el cubo
        color:
            Define al color del cubo
        surface:
            Establece la superficie donde el cubo rotara
        debug:
            En True muestra la posicion de renderizado y angulo de del cubo
        '''
        self.cube(color, [rect[0], rect[1]])
        mouse_pos = pygame.mouse.get_pos()
        self.angle += 5
        if self.angle > 360:
            self.angle = 0
        
        self.rot_cube = pygame.transform.rotate(self.surf_cube, self.angle)
        rect = self.rot_cube.get_rect(center=(0,0))
        surface.blit(self.rot_cube, [rect[2], rect[3]])

        if debug:
            print(f'Angle {self.angle} | mouse_pos: {mouse_pos}')


class Masking:
    def __init__(self, mask_size, position=False, debug=False):
        '''Generar la superficie mascara a un tamanio especifico'''
        self.mask_surf = pygame.Surface(mask_size)
        self.mask_size = mask_size
        if position:
            self.mask_rect = self.mask_surf.get_rect(topleft=position)
        else:
            self.mask_rect = self.mask_surf.get_rect()

        self.mask_surf.set_colorkey((0, 0, 0))

        self.debug = debug


    def draw(self, surface, mask_pos=[0,0], dest=[0,0], dest_offset=[0,0], area=None):
        '''Dibuja la mascara en la superficie

        '''
        relative_position = [-mask_pos[0], -mask_pos[1]]

        # self.mask_rect.x = mask_pos[0]; self.mask_rect.y = mask_pos[1]

        mascara = surface.copy()
        # Modify ofset?

        # print(mascara_rect)

        mascara.blit(self.mask_surf, (dest[0]+dest_offset[0], dest[1]+dest_offset[1]), (0, 0, 250, 100), pygame.BLEND_ALPHA_SDL2)
        
        self.mask_rect.x = dest[0]+dest_offset[0]
        self.mask_rect.y = dest[1]+dest_offset[1]
        self.mask_rect.w = self.mask_size[0]
        self.mask_rect.h = self.mask_size[1]
        
        surface.blit(mascara, (mask_pos))

        # Muestra el contorno de la mascara.
        if self.debug:
            pygame.draw.rect(screen, 'black', (dest,
                        [self.mask_rect.w, self.mask_rect.h]), 1)

        ## IMPORTANT NOTE: Recuerda establecer el rect de la mascara en el contexto donde se dibuja, no es posible aqui.

class DialogueButtons:
    def __init__(self, surface=screen, rel_position=None, color=None):
        
        self.shape = pygame.Surface((12, 12), SRCALPHA)
        if color != None:
            self.shape.fill(color)
        else:
            self.shape.fill((0,0,0,0))

        self.rect = Rect(rel_position[0], rel_position[1], 12, 12)

        screen.blit(self.shape, rel_position)
        

    def rect(self):
        return self.rect

