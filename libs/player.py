from datetime import timedelta
from typing import List, Tuple
import pygame
from pygame.draw import rect
from pygame.locals import *
import random
from .pygamextras import *
from .items import Items
from .bg_ui_elements import Badges

class YAwareGroup(pygame.sprite.Group):
    def by_y(self, spr):
        return spr.pos.y

    def draw(self, surface):
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sorted(sprites, key=self.by_y):
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
        self.lostsprites = []
        print(self.by_y)

class Actor(pygame.sprite.Sprite):
    def __init__(self, image, pos=(200,200), surface=screen):
        super().__init__()
        self.colors = TextColors()
        self.image = image
        self.pos = pygame.Vector2(pos)
        # self.rect = self.image.get_rect(center=self.pos)
        self.rect = Rect(pos[0], pos[1], 32, 64)  # self.image.get_rect()
        self.W, self.H = W, H
        # self.image = pygame.image.load(asset('assets/img', 'player-anim.png'))
        self.movex = pos[0]
        self.movey = pos[1]

        self.current_sprite = 1  # constante de velocidad = 1000
        self.aleatorio = random.randrange(500, 999)

        self.sprites = []
        self.character = character_selected()

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
        
        self.collide_rect = Rect(self.rect.midleft[0],self.rect.midleft[1], 32, 32)

        # Cargando el sprite.
        self.spritesheet = self.sprites

    def update(self):

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

class Player(Actor, Masking):
    def __init__(self, image, pos=[W//2, H//2], speed=3, surface=screen, W=W, H=H):
        # self.items = Items()
        
        super().__init__(image, pos, surface)
        Masking.__init__(self, [0,0])

        
        self.items = Items()


        # Creando la interfas del personaje
        self.badge = Badges()
        self.badge_rect = self.badge.rect
        self.badge_rect = self.rect.bottomleft

        self.speed = speed
        

        self.frame = 0
        self.bg = [0, 0]

        # pos-rect_list_dialogues
        self.prld = 0
        self.prld_x = 0
        self.prld_y = 0
        self.rect_btn_plus = [0,0]
        self.rect_btn_minu = [0,0]
        self.txt_rect = Rect(0,0,0,0)
        # self.newpos = []
        # self.colors= TextColors()
        self.rectn = self.rect
        self.slide_y = 10
        total = 0
        items = 0

        self.vars = {'left': False, 'right': False, 'up': False, 'down': False, 'last_dir': 'down', 'debug': False, 'location': [self.rect.x, self.rect.y]}

        self.vars['total_store'] = total
        self.vars['total_items'] = items

        


    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y


    def badge_draw(self, badge):
        '''Creando el "grupo de sprites" dentro del Player sprite

        badge : nombre del badge desde ActionBadges
        '''
        badge_group = pygame.sprite.Group(self.badge)
        badge_group.update(badge, self.rect.midtop[0]+8, self.rect.midtop[1]-16)
            # badge, self.rect.midtop[0]+8, self.rect.midtop[1]-16)
        badge_group.draw(self.surface)


    def interaction(self):

        if key_press['F4_key']:
            #Rect global
            pygame.draw.rect(self.surface, 'red', (self.rect.x, self.rect.y, 32, 64), 1)
            # colider
            pygame.draw.rect(screen, self.colors.colorize(), self.collide_rect, 1)
            
            # Cargando el sprite desde ActionBadges
            posplayer = TExtra(f'pos: {self.rect.x}, {self.rect.y}', [self.rect.x, self.rect.y-20], 'deepskyblue')


        # Badges loader
        
        # self.dialogue_box()


    def dialogue_box(self, size=[250,100]):
        # Render mask ##########################
        badge = ActionBadges()
        self.badge_draw(badge.drawbadge())
        
        mask = Masking(size)

        newline_space = 15
        items_number = len(self.items.list)
        self.items_height = (newline_space*items_number)-newline_space*2

        # self.cube.rotate('gold', [50,50, 100,100], mask.mask_surf)
        mask.mask_surf.set_alpha(230)
        pygame.draw.rect(mask.mask_surf, 'gray65', (0,0,250, 100), 0)

        total = 0
        items = 0
        # Renderizado desde Items
        for item in self.items.list:
            # colorized1 = self.colors.colorize(50, 255)
            # colorized2 = self.colors.colorize(0, 200)

            pygame.draw.rect(mask.mask_surf, 'green', (self.prld_x-39, self.prld_y, 12,12), 0, 3)
            pygame.draw.rect(mask.mask_surf, 'chocolate1', (self.prld_x-24, self.prld_y, 12,12), 0, 3)
            pygame.draw.rect(mask.mask_surf, 'green4', (self.prld_x-39, self.prld_y, 12,12), 2, 3)
            pygame.draw.rect(mask.mask_surf, 'chocolate3', (self.prld_x-24, self.prld_y, 12,12), 2, 3)
            # print(self.rect_btn_plus)
            item['name'] = item['name'].replace("_", " ")

            mont = item['cost'] * item['quantity']
            
            # pos-rect_list_dialogues
            self.prld_x = mask.mask_rect.x + 45
            self.prld_y = mask.mask_rect.y + (item["id"] * newline_space + self.slide_y)
            self.prld = (self.prld_x, self.prld_y)
            
            itemx = TExtra(
                f'{item["quantity"]}, {item["name"]} ${mont}', self.prld, 'gray1', surface=mask.mask_surf)
            
            self.txt_rect = itemx.texto_rect
            self.rect_btn_plus = (self.prld_x+self.rect.x-289, self.prld_y+self.rect.y-100)
            self.rect_btn_minu = (self.prld_x+self.rect.x-272, self.prld_y+self.rect.y-100)


            # print(txt_rect)
            boton_mas = DialogueButtons(mask.mask_surf, self.rect_btn_plus)
            if pygame.Rect.collidepoint(boton_mas.rect, mouse.get_pos()):
                item['quantity'] += 1
                # print(f'{item["name"]} (+)')

            boton_menos = DialogueButtons(mask.mask_surf, self.rect_btn_minu)
            if pygame.Rect.collidepoint(boton_menos.rect, mouse.get_pos()):
                if item['quantity'] > 0:
                    item['quantity'] -= 1
                # print(f'{item["name"]} (-)')

            mont = item['cost'] * item['quantity']
            total += mont
            items += item['quantity']

            # print(mont)

        self.vars['total_store'] = total
        self.vars['total_items'] = items


        tit_dialog = TExtra(f'Tienda X - Items ({self.vars["total_items"]}) Tot:${self.vars["total_store"]}', [5,0], 'gray1', bgcolor='gray50', surface=mask.mask_surf)
        #texto de ejemplo para poner texto
        # textra('Hola!!!', [mask.mask_rect.x+5, mask.mask_rect.y+15+self.slide_y], surface=mask.mask_surf)
        
        mask.draw(screen, (0,0), (self.rect.topright), (-size[0]-32, -size[1]))
        # mask.draw(screen, (0,0), (self.rect.right, self.rect.top-50))

        # Se debe establecer la posicion de mask_rect en el contexto/ambito 
        self.mask_rect.x = self.rect[0]-250
        self.mask_rect.y = self.rect[1]-100
        self.mask_rect.w = 250
        self.mask_rect.h = 100
        # self.mask_rect = self.rect
        pygame.draw.rect(screen, 'black', (self.mask_rect), 1)
        # print(self.rect, self.mask_rect)

        # Render mask ##########################

        # self.cube.rotate('blueviolet', [100,100,200,200], screen)



    def get_event(self, event):
        # Es mas recomendable utilizar
        # pygame.event.pump()
        # print(self.mask_rect)
    
        ''' Mecanismo de movimiento con el scroll/rueda del raton
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and self.mask_rect.collidepoint(event.pos):
                if self.slide_y > -self.items.items_height:
                    self.slide_y -= 10
                # print('arriba')
            elif event.button == 5 and self.mask_rect.collidepoint(event.pos):
                if self.slide_y < 10:
                    self.slide_y += 10
                # print('abajo')



    # implementar este metodo para reducir codigo en update
    def select_sub_sprite(self, val_a, val_b):
        self.sprites = self.spritesheet
        self.sprites = self.sprites[val_a:val_b]
        return self.sprites


    def update(self):
        '''Actualiza el sprite con las mecanicas genrrales del player
        '''
        
        # Mecanica de colision con las tiendas
        # if self.rect.colliderect():
            # print('Colisione')

        display_percent = 3
        
        if self.vars['down']:
            if not self.rect.y + self.rect.height > self.H-(self.H//display_percent):
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
            if not self.rect.x + self.rect.width > self.W-(self.W//display_percent):
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
            if not self.rect.y < 0+(self.H//display_percent):
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
            if not self.rect.x < 0+(self.W//display_percent):
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

        self.vars['location'][0] = self.rect.x = self.movex
        self.vars['location'][1] = self.rect.y = self.movey

        self.collide_rect[0] = self.movex
        self.collide_rect[1] = self.movey + 48
        self.collide_rect[3] = 16
        ## Borra
        # self.vars['location'][0] = self.rect.x
        #  = self.rect.y

        # Constante de velocidad...
        # aumente # de frames entre cada FPS
        self.current_sprite += self.aleatorio/10000

        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0

        # si es entero cambiar frame
        self.image = self.sprites[int(self.current_sprite)-1]


    def player_up(self):
        self.vars['last_dir'] = 'up'

    def player_down(self):
        self.vars['last_dir'] = 'down'

    def player_left(self):
        self.vars['last_dir'] = 'left'

    def player_right(self):
        self.vars['last_dir'] = 'right'


