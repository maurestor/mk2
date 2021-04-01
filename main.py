#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame, os, sys, time
from pygame.locals import *
from datetime import datetime
from src.poswin import PosWin


"""Caracteristicas por agregar
    
    USA DE TODO.
    NO CAMBIAR LO QUE YA FUNCIONA!
    NO TE CASES CON LAS COSAS!
    
    # Ten cuidado de usar la linea 1 incorrectamente, en linux causa conflicto el interprete
    
    Colisiones
        
    Sistema de dialogos

    Sistema de logros!!!

    Sistema de movimiento
    
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
# Loading Starting System...
# ############################################################################
# pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize

def asset(dir_asset='img/player.old.png'):
    """Busca la ruta absoluta de la carpeta \'assets\' en el OS actual
    
    `Params`:
    dir_asset: str

    Sin parametros se devuelve la imagen de un personaje del juego.
    """

    path_asset = os.path.join(source_dir_file, 'assets/', dir_asset)
    return path_asset


pos_win = PosWin()

# Iniciando pygame...
pygame.init()

W, H = (800, 600)
# Corregir los detalles de resizable
# Utilizar solo medidas relativas.
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE, pygame.DOUBLEBUF)
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
player_x, player_y = (W//2, H//2)  # Posicion
direct = 'down'
mx, my = 0, 0

# Carga de archivos, buscar asset()
source_dir_file = os.path.dirname(os.path.abspath(__file__))

# Cargar fondo
fondo = pygame.image.load(asset('img/fondo.png'))
# Carga textura del personaje

# Direccion velocidad del personaje
player_speed = 0.9

# Declaración de constantes y variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

str_time = {'hora':60,
            'seg':0, 
            'dia':0, 
            'tick':3141569,
            'start':'start',
            'moment_time':'?'
            }

key_press = {"left": False,
             "right": False,
             "up": False,
             "down": False,
             "TAB_key": False,
             'F4_key': False,
             "p_key": False,
             }

stats = {"frame_counter": 0,
         "extras":'',
        }

# player_dialoge = {wellcome: "Hello"}
narrator = dict()
# png_dialoge = {wellcome: 'Hello {}.'.format(name)}

# translate = {
#     esp: {},
#     rus: {},
#     jap: {}
# }


# ############################################################################
# Sprites
# ############################################################################


class Gamer(pygame.sprite.Sprite):
    """Crea al personaje con sus caracteristicas"""
    
    def __init__(self, img='img/player.old.png'):
        pygame.sprite.Sprite.__init__(self)
        self.img_player = pygame.image.load(asset(img))
        self.r_player = self.img_player.get_rect()


    def render(self, direct='down'):
        """Direccion del personaje principal """

        if direct == 'down':
            self.d = self.img_player.subsurface(0, 0, 32, 64)
        elif direct == 'right':
            self.d = self.img_player.subsurface(32, 0, 32, 64)
        elif direct == 'up':
            self.d = self.img_player.subsurface(64, 0, 32, 64)
        elif direct == 'left':
            self.d = self.img_player.subsurface(96, 0, 32, 64)
        
        # return self.d
        screen.blit(self.img_player, (player_x, player_y))


class Store(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        store = Rect(0, 0, 100, 100)




# ############################################################################
# Funciones de debugeo
# ############################################################################


def show_fonts():
    """ Muestra una lista de las fuentes del OS """
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
    """Dibuja el dialogo a partir del logro realizado.
    Se le introduce el id de logro, o logros en cola?
    Guarda los logros en un archivo o una base de datos.
        si se grabro continua
    Devuelve el dialogo correspondiente al logro

    """
    pass



def audio_effect(name, stop_time=False, vol=0.1):
    """Cargar efectos de audio con su nombre 
    name: menu, start, exit
    stop_time: Boulean
    vol: 0.1, 0.5, 1
    """
    # sound = None
    if name == 'menu':
        # pygame.mixer.music.load('./assets/music/effect_nicholasdaryl_swing.wav')
        pygame.mixer.music.load(asset('music/effect_nicholasdaryl_swing.wav'))
        pygame.mixer.music.set_volume(vol)
        sound = pygame.mixer.music.play()
    
    if name == 'start':
        # pygame.mixer.music.load('./assets/music/desktop-login.ogg')
        pygame.mixer.music.load(asset('music/desktop-login.ogg'))
        pygame.mixer.music.set_volume(vol)
        sound = pygame.mixer.music.play()
    
    if name == 'exit' and stop_time:
        pygame.mixer.music.load(asset('music/desktop-logout.ogg'))
        pygame.mixer.music.set_volume(vol)
        sound = pygame.mixer.music.play()
        time.sleep(3000)# sound.get_length())


def run_time():
    tfull = 720 # Ciclo completo, dia entero
    thour = tfull/24 # Una hora
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


def draw_text(text, font, color, surface, x, y):
    """ Dibuja texto en pantalla """

    surface = font.render(text, True, (0, 0, 0), (255, 255, 255, 100))
    # surface.get_rect()
    # surface = surface.center
    screen.blit(surface, (x, y))


def btn_draw(btn, point, color_active, color_hover):
    """Cambia color al pasar el raton sobre el elemento"""
    collide = btn.collidepoint(point)
    color = color_hover if collide else color_active
    pygame.draw.rect(screen, color, btn)


def options():
    global count
    print("Llamando a opciones: %s :) " % str(count))
    count += 1


def active_stats():
    """ 
    global playtime_total
    milliseconds = clock.tick(fps_out)
    playtime_total += milliseconds / 500.0
    """
    global mx, my
    mx, my = pygame.mouse.get_pos()


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
        
        pygame.display.flip()
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
        pygame.display.flip()
        pygame.display.set_caption("Local Market » " + str(tnow[0]))
        # pygame.display.update()
        clock.tick(fps)


# ############################################################################
# Loop Principal
# ############################################################################

def main_game():
    """Función principal del juego"""

    # Guardar posicion
    global player_x, player_y, direct, player_speed, tnow, mx, my, t0, str_time, stats

    player = Gamer(img='img/player.png')
    moving = False
    running = True  # Activador del menu
    der = 0 # Restableciendo el movimiento.
    # Bucle principal
    while running:
        screen.fill('black')
        # Mostrar fondo
        stats['frame_counter'] += 1
        der += 0.05
        screen.blit(fondo, (der, 0))

        # Estadisticas
        active_stats()

        # Se dibuja el personaje
        screen.blit(player.directi(direct), player.r_player)
        screen.blit(player.directi(direct), (player_x, player_y))


        # menu_player = Menu Item Player
        # 
        w_menu_player = int((W/100)*80)
        h_menu_player = int((H/100)*80)
        

        menu_player = pygame.Surface((w_menu_player, h_menu_player))
        # menu_player_h_center, menu_player_w_center = menu_player.get_height()/2, menu_player.get_width()/2
        menu_player.get_rect()
        # menu_player.center
        menu_player.set_alpha(200)
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
                # if event.key == K_p:  # Comandos FPS
                #     key_press["p_key"] = True

                # resetear el tiempo
                if event.key == K_F5:  # Reset Time
                    key_press["F5_key"] = True
                    tnow[1] = False

                # Abrir el menu )transparente=
                if event.key == K_TAB and key_press["TAB_key"] == False:
                    key_press["TAB_key"] = True
                elif event.key == K_TAB and key_press["TAB_key"]:
                    key_press["TAB_key"] = False

                # Abctivar-Descartivar estadisticas
                if event.key == K_F4 and key_press["F4_key"] == False:
                    key_press["F4_key"] = True
                elif event.key == K_F4 and key_press["F4_key"]:
                    key_press["F4_key"] = False

                # if event.key == K_p and key_press["p_key"] == False:
                #     key_press["p_key"] = True
                # elif event.key == K_p and key_press["p_key"]:
                #     key_press["p_key"] = False
            
            elif event.type == MOUSEBUTTONDOWN:
                if player.r_player.collidepoint(event.pos):
                    moving = True
                    print('player')
            elif event.type == MOUSEBUTTONUP:
                moving = False
            elif event.type == MOUSEMOTION and moving:
                player.r_player.move_ip(event.rel)
                

            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_a:
                    key_press["left"] = False
                if event.key == K_RIGHT or event.key == K_d:
                    key_press["right"] = False
                if event.key == K_UP or event.key == K_w:
                    key_press["up"] = False
                if event.key == K_DOWN or event.key == K_s:
                    key_press["down"] = False
                # if event.key == K_p:
                #     key_press["p_key"] = False
            # elif running == False:
            #     exit()

        # Movimiento de rebote
        # if key_press['p_key']:
        #         player_x -= player_speed
        #         if player_x <= 0:
        #             player_x += player_speed
        # if key_press['p_key']:
        #     if player_x + 32 <= W:
        #         player_x -= player_speed
        # if key_press['p_key']:
        #     if player_y >= 0:
        #         player_y -= player_speed
        # if  key_press['p_key']:
        #     if player_y +256 <= W:
        #         player_y += player_speed

        # print(stats)

        if key_press["left"]:  # == Si left es verdadero
            if player_x <= 0:
                direct = 'left'
            else:
                direct = 'left'
                player_x -= player_speed
        if key_press["right"]:
            if player_x + 32 >= W:
                direct = 'right'
            else:
                direct = 'right'
                player_x += player_speed
        if key_press["up"]:
            if player_y <= 0:
                direct = 'up'
            else:
                direct = 'up'
                player_y -= player_speed
        if key_press["down"]:
            if player_y + 256 >= W:
                # Arregla la medida del sprite a 64
                direct = 'down'
            else:
                direct = 'down'
                player_y += player_speed

        # Abrir menu items
        if key_press["TAB_key"]:
            # Dibujar el menu en medio
            screen.blit(menu_player, (((W//2)-w_menu_player/2), ((H//2)-h_menu_player/2)))


        if key_press["F4_key"]:
            run_time()

            # Muestra la ubicacion del juagor
            draw_text("Player_loc: x({:4.3f}), y({:4.3f})".format(player_x,
                       player_y), font, WHITE, screen, 20, 40)
            # Muestra el mouse
            draw_text("Mouse: x({:4.3f}), y({:4.3f})".format(mx, my),
                       font, WHITE, screen, 20, 60)

            draw_text('{} dias {:6.2f}'.format(str_time['dia'], tnow[0]), font, 'white', screen, 20, 80)
            # Muestra la hora real.
            draw_text('Hora: {}'.format(hora_real),
                       font, 'white', screen, 50+(W/2), 34)
            # Muestra el momento del dia 
            draw_text('{}'.format(str_time['moment_time']),
                       font, 'white', screen, 50+(W/2), 55)

            draw_text('{}'.format(vday),
                       font, 'white', screen, 50+(W/2), 75)



        time_control()
        # 3.- Se actualiza la pantalla
        pygame.display.flip()
        pygame.display.set_caption("Local Market » {:3.2f}".format(tnow[0]))
        # pygame.display.update()

if __name__ == '__main__':
    audio_effect('start')
    main_menu()
