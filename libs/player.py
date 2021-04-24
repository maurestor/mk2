import pygame
from pygame.locals import *
import random
from .pygamextras import *


class Player(pygame.sprite.Sprite):
    def __init__(self, location=[W//2, H//2], speed=3, surface=screen, W=W, H=H, character='naranjas'):
        pygame.sprite.Sprite.__init__(self)
        self.W, self.H = W, H
        self.image = pygame.image.load(asset('assets/img', 'player-anim.png'))
        self.movex = location[0]
        self.movey = location[1]

        self.sprites = []
        self.character = character

        if self.character in ('green', 'verde'):
            # Personaje Verde
            self.sprites.append(self.image.subsurface(0, 0, 32, 64))    # Stay_R0
            self.sprites.append(self.image.subsurface(32, 0, 32, 64))   # Stay_R1
            self.sprites.append(self.image.subsurface(64, 0, 32, 64))   # Walk_R0
            self.sprites.append(self.image.subsurface(96, 0, 32, 64))   # Walk_R1
            self.sprites.append(self.image.subsurface(256, 0, 32, 64))  # Stay_down0   <----
            self.sprites.append(self.image.subsurface(288, 0, 32, 64))  # Stay_down1
            self.sprites.append(self.image.subsurface(320, 0, 32, 64))  # Walk_down0
            self.sprites.append(self.image.subsurface(352, 0, 32, 64))  # Walk_down1
            self.sprites.append(self.image.subsurface(128, 0, 32, 64))  # Stay_up0
            self.sprites.append(self.image.subsurface(160, 0, 32, 64))  # Stay_up1
            self.sprites.append(self.image.subsurface(192, 0, 32, 64))  # Walk_up0
            self.sprites.append(self.image.subsurface(224, 0, 32, 64))  # Walk_up1
            self.sprites.append(pygame.transform.flip(self.sprites[0], True, False))  # Stay_L0
            self.sprites.append(pygame.transform.flip(self.sprites[1], True, False))  # Stay_L1
            self.sprites.append(pygame.transform.flip(self.sprites[2], True, False))  # Walk_L0
            self.sprites.append(pygame.transform.flip(self.sprites[3], True, False))  # Walk_L1

        elif self.character in ('blue', 'azul'):
            # Personaje azul
            self.sprites.append(self.image.subsurface(0, 64, 32, 64))    
            self.sprites.append(self.image.subsurface(32, 64, 32, 64))   
            self.sprites.append(self.image.subsurface(64, 64, 32, 64))   
            self.sprites.append(self.image.subsurface(96, 64, 32, 64))   
            self.sprites.append(self.image.subsurface(256, 64, 32, 64))  
            self.sprites.append(self.image.subsurface(288, 64, 32, 64))  
            self.sprites.append(self.image.subsurface(320, 64, 32, 64))  
            self.sprites.append(self.image.subsurface(352, 64, 32, 64))  
            self.sprites.append(self.image.subsurface(128, 64, 32, 64))  
            self.sprites.append(self.image.subsurface(160, 64, 32, 64))  
            self.sprites.append(self.image.subsurface(192, 64, 32, 64))  
            self.sprites.append(self.image.subsurface(224, 64, 32, 64))  
            self.sprites.append(pygame.transform.flip(self.sprites[0], True, False))  
            self.sprites.append(pygame.transform.flip(self.sprites[1], True, False))  
            self.sprites.append(pygame.transform.flip(self.sprites[2], True, False))  
            self.sprites.append(pygame.transform.flip(self.sprites[3], True, False))  

        elif self.character in ('red', 'rojo'):
            # Personaje rojo
            self.sprites.append(self.image.subsurface(0, 128, 32, 64))    
            self.sprites.append(self.image.subsurface(32, 128, 32, 64))   
            self.sprites.append(self.image.subsurface(64, 128, 32, 64))   
            self.sprites.append(self.image.subsurface(96, 128, 32, 64))   
            self.sprites.append(self.image.subsurface(256, 128, 32, 64))  
            self.sprites.append(self.image.subsurface(288, 128, 32, 64))  
            self.sprites.append(self.image.subsurface(320, 128, 32, 64))  
            self.sprites.append(self.image.subsurface(352, 128, 32, 64))  
            self.sprites.append(self.image.subsurface(128, 128, 32, 64))  
            self.sprites.append(self.image.subsurface(160, 128, 32, 64))  
            self.sprites.append(self.image.subsurface(192, 128, 32, 64))  
            self.sprites.append(self.image.subsurface(224, 128, 32, 64))  
            self.sprites.append(pygame.transform.flip(self.sprites[0], True, False))  
            self.sprites.append(pygame.transform.flip(self.sprites[1], True, False))  
            self.sprites.append(pygame.transform.flip(self.sprites[2], True, False))  
            self.sprites.append(pygame.transform.flip(self.sprites[3], True, False))  

        elif self.character in ('orange', 'nanaranjas'):
            # Personaje naranja
            self.sprites.append(self.image.subsurface(0, 192, 32, 64))    
            self.sprites.append(self.image.subsurface(32, 192, 32, 64))   
            self.sprites.append(self.image.subsurface(64, 192, 32, 64))   
            self.sprites.append(self.image.subsurface(96, 192, 32, 64))   
            self.sprites.append(self.image.subsurface(256, 192, 32, 64))  
            self.sprites.append(self.image.subsurface(288, 192, 32, 64))  
            self.sprites.append(self.image.subsurface(320, 192, 32, 64))  
            self.sprites.append(self.image.subsurface(352, 192, 32, 64))  
            self.sprites.append(self.image.subsurface(128, 192, 32, 64))  
            self.sprites.append(self.image.subsurface(160, 192, 32, 64))  
            self.sprites.append(self.image.subsurface(192, 192, 32, 64))  
            self.sprites.append(self.image.subsurface(224, 192, 32, 64))  
            self.sprites.append(pygame.transform.flip(self.sprites[0], True, False))  
            self.sprites.append(pygame.transform.flip(self.sprites[1], True, False))  
            self.sprites.append(pygame.transform.flip(self.sprites[2], True, False))  
            self.sprites.append(pygame.transform.flip(self.sprites[3], True, False))  

        self.surface = surface
        self.rect = Rect(location[0], location[1], 32, 64)  # self.image.get_rect()
        self.collide_rect = Rect(self.rect.midleft[0],self.rect.midleft[1], 32, 32)

        # Creando la interfas del personaje
        self.playerui = PlayerUi()
        self.playerui_rect = self.playerui.rect
        self.playerui_rect = self.rect.bottomleft

        self.speed = speed
        self.current_sprite = 1  # constante de velocidad = 1000
        self.aleatorio = random.randrange(500, 999)

        self.frame = 0
        self.bg = [0, 0]

        self.vars = {'left': False, 'right': False, 'up': False, 'down': False,
                     'last_dir': 'down', 'debug': False, 'location': [self.rect.x, self.rect.y]}
        self.exis = {'otro datos':True, 'mas entradas':{'nuevos':True, 'otro':[25, 61, 25]}}

        # Cargando el sprite.
        self.spritesheet = self.sprites


    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def playerui_draw(self, badge):
        '''Creando el "grupo de sprites" dentro del Player sprite

        badge : nombre del badge desde ActionBadges
        '''
        playerui_group = pygame.sprite.Group(self.playerui)
        playerui_group.update(badge, self.rect.midtop[0]+8, self.rect.midtop[1]-16)
            # badge, self.rect.midtop[0]+8, self.rect.midtop[1]-16)
        playerui_group.draw(self.surface)

    def debug(self, badge_state='exclamation'):
        if key_press['F4_key']:
            pygame.draw.rect(self.surface, 'red',
                                (self.rect.x, self.rect.y, 32, 64), 1)
            
            # Cargando el sprite desde ActionBadges
            textra(f'pos: {self.rect.x}, {self.rect.y}', [self.rect.x, self.rect.y-20], 'deepskyblue')

        self.playerui_draw(badge_state)

    # implementar este metodo para reducir codigo en update

    def select_sub_sprite(self, val_a, val_b):
        self.sprites = self.spritesheet
        self.sprites = self.sprites[val_a:val_b]
        return self.sprites

    def update(self):

        if self.vars['down']:
            if not self.rect.y + self.rect.height > self.H-(self.H//10):
                self.player_down()
                self.control(y=self.speed, x=0)
                self.select_sub_sprite(6, 8)
            else:
                self.select_sub_sprite(6, 8)
                self.player_down()
                # Movement background trought player
                self.bg[1] -= self.speed

        elif self.vars['last_dir'] == 'down':
            self.select_sub_sprite(4, 6)

        if self.vars['right']:
            if not self.rect.x + self.rect.width > self.W-(self.W//10):
                self.vars['last_dir'] = 'right'
                self.control(y=0, x=self.speed)
                self.select_sub_sprite(2, 4)
            else:
                self.select_sub_sprite(2, 4)
                self.vars['last_dir'] = 'right'
                # Movement background trought player
                self.bg[0] -= self.speed
        elif self.vars['last_dir'] == 'right':
            self.select_sub_sprite(0, 2)

        if self.vars['up']:
            if not self.rect.y < 0+(self.H//8):
                self.vars['last_dir'] = 'up'
                self.control(y=-self.speed, x=0)
                self.select_sub_sprite(10, 12)
            else:
                self.select_sub_sprite(10, 12)
                self.vars['last_dir'] = 'up'
                # Moviendo el fondo
                self.bg[1] += self.speed
        elif self.vars['last_dir'] == 'up':
            self.select_sub_sprite(8, 10)

        if self.vars['left']:
            if not self.rect.x < 0+(self.W//10):
                self.vars['last_dir'] = 'left'
                self.control(y=0, x=-self.speed)
                self.select_sub_sprite(14, 16)
            else:
                self.select_sub_sprite(14, 16)
                self.vars['last_dir'] = 'left'
                # Movement background trought player
                self.bg[0] += self.speed
        elif self.vars['last_dir'] == 'left':
            self.select_sub_sprite(12, 14)

        self.rect.x = self.movex
        self.rect.y = self.movey
        self.vars['location'][0] = self.rect.x
        self.vars['location'][1] = self.rect.y

        # Constante de velocidad...
        # aumente # de frames entre cada FPS
        self.current_sprite += self.aleatorio/10000

        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0

        # si es entero cambiar frame
        self.image = self.sprites[int(self.current_sprite)-1]

    def gui_draw(self):
        """Muestra el simbolo de la interfaz correspondiente
        Ejemplos:
        Pregunta ?
        Admiracion !
        """
        pygame.sprite.Sprite.__init__(self)
        pass

    # def control_player(self, event):
    #     """Por mejorar se detiene en algun punto, no se puede mover mas de una vez?
    #     hacia los vectores distintos"""
    #     if event.type == KEYDOWN:
    #         if event.key in (K_UP, K_w):
    #             self.vars['up'] = True
    #         if event.key in (K_DOWN, K_s):
    #             self.vars['down'] = True
    #         if event.key in (K_LEFT, K_a):
    #             self.vars['left'] = True
    #         if event.key in (K_RIGHT, K_d):
    #             self.vars['right'] = True
    #     elif event.type == KEYUP:
    #         if event.key in (K_UP, K_w):
    #             self.vars['up'] = False
    #         if event.key in (K_DOWN, K_s):
    #             self.vars['down'] = False
    #         if event.key in (K_LEFT, K_a):
    #             self.vars['left'] = False
    #         if event.key in (K_RIGHT, K_d):
    #             self.vars['right'] = False

    def player_up(self):
        self.vars['last_dir'] = 'up'

    def player_down(self):
        self.vars['last_dir'] = 'down'

    def player_left(self):
        self.vars['last_dir'] = 'left'

    def player_right(self):
        self.vars['last_dir'] = 'right'


class PlayerUi(pygame.sprite.Sprite):
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
        # self.image = pygame.transform.rotate(self.image, self.deg)
