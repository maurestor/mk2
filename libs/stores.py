import pygame
from pygame.locals import *
from .pygamextras import *

class Store(pygame.sprite.Sprite):
    image = pygame.image.load(asset('assets/img','stores-anim.png'))

    def __init__(self, location=[], pid=1, multi=False):
        pygame.sprite.Sprite.__init__(self)
        if location == 'middle':
            location = (W//2,H//2)
            self.rect = Rect(location[0], location[1], 128, 128)
        else:
            self.rect = Rect(location[0], location[1], 128, 128)


        self.movex = location[0]
        self.movey = location[1]

        self.pid = pid
        self.location = location

        self.sprites = []
        self.sprites.append(self.image.subsurface(0, 0, 128, 128))    # Stay_R0
        self.sprites.append(self.image.subsurface(128, 0, 128, 128))   # Stay_R1
        self.current_sprite = 0
        self.frame = 0

        self.spritesheet = self.sprites
        
        self.vars = {'id':pid, 'type':'store', 'location':[location[0], location[1]]}
        

    def debug(self, debug):
        if debug:
            return pygame.draw.rect(screen, 'gold', self.rect, 1)

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y
    

    def update(self):
        self.rect.x = self.movex
        self.rect.y = self.movey
        self.vars['location'][0] = self.rect.x
        self.vars['location'][1] = self.rect.y

        # if pygame.sprite.groupcollide(player_group, store_group, False, False):
        #     debug(self.rect)
        # else:
        #     audio_effect('menu')

        self.current_sprite += 0.005  # aumente # de frames entre cada FPS
        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)-1] # si es entero cambiar frame


        

class MultiShop():
    pos_storex= 1; pos_storey = 1

    def __init__(self):
        """Crear varias tiendas"""
        # pos_storex= 1; pos_storey = 1

        pass
                
                # x += self.pos_storex; y += self.pos_storey