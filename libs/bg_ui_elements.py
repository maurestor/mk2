# from .player import Player
import pygame
from pygame.locals import *
from pygame.surface import Surface
from .pygamextras import *
from random import randrange
from .stores import Stores, StoreBg


class Background:
    def __init__(self):
        """Renderizando fondo, se mueve cuando el juagdor toca el border
        """

        # Asignado atributos del renderizado
        self.tile_floor = pygame.image.load(asset('assets/img', 'floor.png'))
        self.tile_store = pygame.image.load(asset('assets/img', 'store_only.png'))
        self.image = pygame.image.load(asset('assets/img', 'background_road.png')).convert_alpha()
        self.tile_bg = pygame.image.load(asset('assets/img', 'background_road.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.sprites = []
        self.sprites.append(self.image.subsurface(0, 0, 128, 128))
        

        self.store_group = pygame.sprite.Group()
        self.list_store = []
        self.list_imp = []
        self.list_store_bg = []
        self.store_pos = [0,0]

        self.mkt_vars = {'total':0}


        # Iniciando el renderizado

    def update(self, surf, pos=[0, 0]):


        # mask = pygame.image.load("/home/restor/Documents/game-develop/Python manuals/mask.png").convert_alpha()

        tw = self.tile_bg.get_width()
        th = self.tile_bg.get_height()

        background = pygame.Surface((W, H))
        for py in range(0, int(H//th) + 2):
            for px in range(0, int(W//tw) + 2):
                surf.blit(self.tile_bg, (px*(tw-1)+pos[0], py*(th-1)+pos[1]))

                if key_press['F4_key']:
                    mouse = pygame.mouse.get_pressed()
                    mousepos = pygame.mouse.get_pos()
                    mouserel = pygame.mouse.get_rel()
                    if mousepos:
                        if self.rect.collidepoint(mousepos):
                            pygame.draw.polygon(screen, 'chocolate1', [(
                                0+pos[0], 128+pos[1]), (100+pos[0], 128+pos[1]), (128+pos[0], 100+pos[1]), (28+pos[0], 100+pos[1])], 2)
                            moving = True
                    elif mouse[0] == False:
                        moving = False
        
        # Si hay colision con el cursor y esta cerca el jugador debe dibujarse

    def tiles(self, posone=[0, 0], colorized=False):
        '''Corregir bien este metodo

        Multiplos de 128 hacia abajo
        ejemplos:
        128, 64, 32, 16, (8, 4, 2, 1)

        Paterns
        Crear un generador dinamico de mapas

        Wall
        ----------
        xxxxxxxxxx
        x        x
        x        x
        x        x
        x        x
        x        x
        xxxxxxxxxx
        ----------

        Only One
        ----------


            x     




        ----------

        Window
xxxxxxxxxx
x   xx   x
x   xx   x
x   xx   x
x   xx   x
x   xx   x
xxxxxxxxxx
        ----------

        Noting
        ----------







        ----------

        Spiral
        xxxxxxxxxx
                 x
        xxxxxxxx x
        x      x x
        x xxxxxx x
        x        x
        xxxxxxxxxx
        ----------

        two
        ----------
          
          
x     x   
          
          
          
          
'''
        map_gral = """  x       
    z     
x y  zx   
    y     
  z       
          
          """
        map_gral = map_gral.splitlines()
        
        def store_type(tipo=None):
            '''Metodo de renderizado de tienda...'''
            self.store_pos = pygame.Vector2([x*128+posone[0], (y*128)+posone[1]])

            store = Stores([x*128+posone[0], (y*128)+posone[1]], tipo)
            self.store_group.add(store)

            store_bg = StoreBg([store.rect.x, store.rect.y])
            self.store_group.add(store_bg)
            
            # screen.blit(tile_floor, (x*128+posone[0], (y*128)+108+posone[1]))

            # screen.blit(tile_store, (x*128+posone[0], y*128+posone[1]))
            
            # Dibujar en los puntos marcados
            if colorized==True:
                if x == 0 or y == 0:
                    if 0 == y and x == 0:
                        pygame.draw.rect(
                            screen, colorized, ([x, y], [128, 128]), 1, 75)
                    elif y > 0:
                        pygame.draw.rect(
                            screen, colorized, ([x, y*128], [128, 128]), 1, 75)
                    elif x > 0:
                        pygame.draw.rect(
                            screen, colorized, ([x*128, y], [128, 128]), 1, 75)
                elif not 0 in (x, y):
                    pygame.draw.rect(
                        screen, colorized, ([x*128, y*128], [128, 128]), 1, 75)

            #Guardando las tiendas
            self.list_imp.append(self.store_pos)
            self.list_store.append(store)
            self.list_store_bg.append(store_bg)
            


        for y, line in enumerate(map_gral):
            for x, c in enumerate(line):
                # print(pos[0])
                # if c in (" ", "x"):
                #     screen.blit(tile_bg, ((x*128), (y*128)))
                if c == "x":
                    store_type(None)
                if c == 'y':
                    store_type('green')
                if c == "z":
                    store_type('dark_green')
                
        
                    

    def draw_(self):
        pass

    def cuadricula_posicion(self):
        pass


class Stats:
    def __init__(self):
        str_dia = str_time['dia']
        mx, my = pygame.mouse.get_pos()
        if key_press['F4_key']:

            # Muestra el mouse
            pos_mouse = TExtra(f"Mouse, X: {mx}, Y: {my}", (20, 60),
                   'black', 'black', 1, None, 'white', 5, 5, 5, 5)

            time_stat = TExtra(f'{str_dia} dias {tnow[0]:6.3f}', (20, 80),
                   'black', 'black', 1, None, 'white', 5, 5, 5, 5)

            # Muestra la hora real.
            time_real = TExtra(f'Hora: {hora_real}', (50+(W/2), 34),
                   'black', 'black', 1, None, 'white', 5, 5, 5, 5)

            # Muestra el momento del dia
            time_virt = TExtra('{}'.format(str_time['moment_time']), (50+(W/2),
                   55), 'black', 'black', 1, None, 'white', 5, 5, 5, 5)

            time_virt2 = TExtra(f'{vday}', (50+(W/2), 75), 'black',
                   'black', 1, None, 'white', 5, 5, 5, 5)


class Badges(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.aleatorio = random.randrange(1, 900)
        self.speed = 1
        self.current_sprite = 1  # constante de velocidad = 1000
        self.frame = 0
        self.location = (0, 0)
        self.image = pygame.image.load(asset('assets/img', 'gui_sprite.png'))
        self.rect = self.image.get_rect()
        self.deg = 0
        # self.rect = Player.rect.midtop[0]+8, Player.rect.midtop[1]-16

        self.sprites = []

        # Interrogation
        self.sprites.append(self.image.subsurface(0, 0, 16, 16))
        self.sprites.append(self.image.subsurface(16, 0, 16, 16))
        self.sprites.append(self.image.subsurface(0, 0, 16, 16))
        self.sprites.append(self.image.subsurface(32, 0, 16, 16))
        # Exclamation
        self.sprites.append(self.image.subsurface(0, 16, 16, 16))
        self.sprites.append(self.image.subsurface(16, 16, 16, 16))
        self.sprites.append(self.image.subsurface(0, 16, 16, 16))
        self.sprites.append(self.image.subsurface(32, 16, 16, 16))

        # MecaX Bill
        self.sprites.append(self.image.subsurface(0, 32, 20, 12))

        # Badge bad_badge
        self.sprites.append(self.image.subsurface(27, 48, 9, 6))
        # Badge regular_badge
        self.sprites.append(self.image.subsurface(18, 48, 9, 6))
        # Badge Normal_badge
        self.sprites.append(self.image.subsurface(9, 48, 9, 6))
        # Badge good_badge
        self.sprites.append(self.image.subsurface(0, 48, 9, 6))
        # Badge premium_badge
        self.sprites.append(self.image.subsurface(0, 48, 9, 6))
        # Badge lux_badge
        self.sprites.append(self.image.subsurface(0, 48, 9, 6))

        self.spritesheet = self.sprites

    def select_sub_sprite(self, val_a, val_b):
        """Vuelve a llenar de sprites espefcificos el ciclo para que se rendericen.

        simplified
        """
        self.sprites = self.spritesheet
        self.sprites = self.sprites[val_a:val_b]
        return self.sprites

    def update(self, plin_state, x, y):
        """Dibuja el icono relacionado

        Actions:
            interrogation, exclamation, bill

        Bandges:
            good, normal, regular, bad, premium, lux
        """

        # lista = {'interrogation', 'exclamation', 'bill', 'good_badge',
        #          'normal_badge', 'regular_badge', 'bad_badge', 'premium_badge', 'lux_badge'}

        if plin_state == 'interrogation':
            self.rect = Rect(x, y, 16, 16)
            self.select_sub_sprite(0, 4)

        elif plin_state == 'exclamation':
            # exclamation
            self.rect = Rect(x, y, 16, 16)
            self.select_sub_sprite(4, 8)

        if plin_state == 'bill':
            self.rect = Rect(x, y, 20, 12)
            self.select_sub_sprite(8, 9)

        # badges
        if plin_state == 'good_badge':
            # green good badge
            self.rect = Rect(x, y, 8, 5)
            self.select_sub_sprite(9, 10)
        elif plin_state == 'normal_badge':
            self.rect = Rect(x, y, 8, 5)
            self.select_sub_sprite(10, 11)
        elif plin_state == 'regular_badge':
            self.rect = Rect(x, y, 8, 5)
            self.select_sub_sprite(11, 12)
        elif plin_state == 'bad_badge':
            self.rect = Rect(x, y, 8, 5)
            self.select_sub_sprite(12, 13)
        elif plin_state == 'premium_badge':
            self.rect = Rect(x, y, 8, 5)
            self.select_sub_sprite(13, 14)
        elif plin_state == 'lux_badge':
            self.rect = Rect(x, y, 8, 5)
            self.select_sub_sprite(14, 15)

        # Constante de velocidad...
        self.current_sprite += 0.05  # aumente # de frames entre cada FPS

        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0

        # si es entero cambiar frame
        self.image = self.sprites[int(self.current_sprite)-1]
        self.deg += 5
        if self.deg > 360:
            self.deg = 0
        self.image = pygame.transform.rotate(self.image, self.deg)
        pygame.draw.rect(screen, 'blue', self.rect, 1)



class UserInterface():
    def __init__(self):
        pass

    def gui(self, tot_price, tot_items):
        '''Dibuja la interface de usuario general de estadisticas y conroles del mercado'''

        str_dia = str_time['dia']

        # pygame.draw.arc(screen, 'green', [W-100, 0, 250, 250], math.pi, 3*math.pi/2)

        pygame.draw.rect(screen, 'chartreuse4', [
                         W-202, 0, 302, 37], 0, 0, 5, 0, 15)
        pygame.draw.ellipse(screen, 'chartreuse4', [W-102, -102, 205, 205])
        pygame.draw.rect(screen, 'chartreuse3', [
                         W-200, 0, 300, 35], 0, 0, 5, 0, 15)
        pygame.draw.ellipse(screen, 'chartreuse3', [W-100, -100, 200, 200])

        virt_day = TExtra(f'Day: {str_dia}, time: {tnow[0]:4.1f}', [W-190, 16], 'black')
        total_price = TExtra(f'Total ${tot_price}', [W-190, 4], 'black')
        total_items = TExtra(f'#{tot_items} items', [W-90, 4], 'black')

