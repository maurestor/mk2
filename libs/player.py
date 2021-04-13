import pygame
from pygame.locals import *
from .pygamextras import asset, H, W
from random import randrange

class Player(pygame.sprite.Sprite):

    image = pygame.image.load(asset('assets/img','player-anim.png'))

    sprites = []
    
    sprites.append(image.subsurface(0, 0, 32, 64))    # Stay_R0
    sprites.append(image.subsurface(32, 0, 32, 64))   # Stay_R1
    sprites.append(image.subsurface(64, 0, 32, 64))   # Walk_R0
    sprites.append(image.subsurface(96, 0, 32, 64))   # Walk_R1
    sprites.append(image.subsurface(256, 0, 32, 64))  # Stay_down0   <----
    sprites.append(image.subsurface(288, 0, 32, 64))  # Stay_down1
    sprites.append(image.subsurface(320, 0, 32, 64))  # Walk_down0
    sprites.append(image.subsurface(352, 0, 32, 64))  # Walk_down1
    sprites.append(image.subsurface(128, 0, 32, 64))  # Stay_up0
    sprites.append(image.subsurface(160, 0, 32, 64))  # Stay_up1
    sprites.append(image.subsurface(192, 0, 32, 64))  # Walk_up0
    sprites.append(image.subsurface(224, 0, 32, 64))  # Walk_up1
    sprites.append(pygame.transform.flip(sprites[0], True, False))# Stay_L0
    sprites.append(pygame.transform.flip(sprites[1], True, False))# Stay_L1
    sprites.append(pygame.transform.flip(sprites[2], True, False))# Walk_L0
    sprites.append(pygame.transform.flip(sprites[3], True, False))# Walk_L1

    gui_answer = []
    
    
    def __init__(self, location=[W//2, H//2], speed=3, W=W, H=H):
        pygame.sprite.Sprite.__init__(self)
        self.W, self.H = W, H
        self.movex = location[0]
        self.movey = location[1]

       
        self.rect = Rect(location[0], location[1], 32, 64) # self.image.get_rect()
        
        #Creando la gui
        self.collide_rect = Rect(location[0], location[1], 32, 32)
        self.collide_rect.bottomleft = self.rect.topright

        self.speed = speed
        self.current_sprite = 1 #constante de velocidad = 1000
        self.aleatorio = randrange(1, 900)

        self.frame = 0
        self.bg = [0, 0]

        self.vars = {'left': False, 'right': False, 'up': False, 'down': False, 'last_dir':'down', 'debug':False, 'location':[self.rect.x, self.rect.y]}

        # Cargando el sprite.

        

        self.spritesheet = self.sprites
    

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def debug(self, debug):
        if debug:
            return pygame.draw.rect(screen, 'gold', self.rect, 1)


    # implementar este metodo para reducir codigo en update
    def select_sub_sprite(self, val_a, val_b):
        self.sprites = self.spritesheet
        self.sprites = self.sprites[val_a:val_b]
        return self.sprites

    def control_player(self, event):
        """Por mejorar se detiene en algun punto, no se puede mover mas de una vez?
        hacia los vectores distintos"""
        if event.type == KEYDOWN:
            if event.key in (K_UP, K_w):
                self.vars['up'] = True
            if event.key in (K_DOWN, K_s):
                self.vars['down'] = True
            if event.key in (K_LEFT, K_a):
                self.vars['left'] = True 
            if event.key in (K_RIGHT, K_d): 
                self.vars['right'] = True
        elif event.type == KEYUP:
            if event.key in (K_UP, K_w):
                self.vars['up'] = False
            if event.key in (K_DOWN, K_s):
                self.vars['down'] = False 
            if event.key in (K_LEFT, K_a): 
                self.vars['left'] = False
            if event.key in (K_RIGHT, K_d): 
                self.vars['right'] = False


    def player_up(self):
        self.vars['last_dir'] = 'up'

    def player_down(self):
        self.vars['last_dir'] = 'down'

    def player_left(self):
        self.vars['last_dir'] = 'left'

    def player_right(self):
        self.vars['last_dir'] = 'right'



    def update(self, surface):

        # Gui draw
        pygame.draw.rect(surface, 'gold', (self.rect.x, self.rect.y-16, 32, 32), 1)

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
                self.select_sub_sprite(2,4)
            else:
                self.select_sub_sprite(2,4)
                self.vars['last_dir'] = 'right'
                # Movement background trought player
                self.bg[0] -= self.speed
        elif self.vars['last_dir'] == 'right':
            self.select_sub_sprite(0,2)

        if self.vars['up']:
            if not self.rect.y < 0+(self.H//8):
                self.vars['last_dir'] = 'up'
                self.control(y=-self.speed, x=0)
                self.select_sub_sprite(10,12)
            else:
                self.select_sub_sprite(10,12)
                self.vars['last_dir'] = 'up'
                #Moviendo el fondo
                self.bg[1] += self.speed
        elif self.vars['last_dir'] == 'up':
            self.select_sub_sprite(8,10)

        if self.vars['left']:
            if not self.rect.x < 0+(self.W//10):
                self.vars['last_dir'] = 'left'
                self.control(y=0, x=-self.speed)
                self.select_sub_sprite(14,16)
            else:
                self.select_sub_sprite(14,16)
                self.vars['last_dir'] = 'left'
                # Movement background trought player
                self.bg[0] += self.speed
        elif self.vars['last_dir'] == 'left':
            self.select_sub_sprite(12,14)


        # if pygame.sprite.groupcollide(player_group, store_group, False, False):
        #     debug(self.rect)
        # else:
        #     audio_effect('menu')


        self.rect.x = self.movex
        self.rect.y = self.movey
        self.vars['location'][0] = self.rect.x
        self.vars['location'][1] = self.rect.y

        

        # Constante de velocidad...
        self.current_sprite += self.aleatorio/10000  # aumente # de frames entre cada FPS

        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0

        
        self.image = self.sprites[int(self.current_sprite)-1] # si es entero cambiar frame
        
        # self.surface.blit(self.debug(), self.location)

    def gui_render(self, simbol, vector, lifetime):
        """Muestra el simbolo de la interfaz correspondiente
        
        Ejemplos:
        Pregunta ?
        Admiracion !

        """
        self.simbol = simbol
        self.vector = vector
        self.lifetime = lifetime
                #Si hay colision con el grupo tienda

