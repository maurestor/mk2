import pygame
from pygame.locals import *
from .pygamextras import *

class Stores(pygame.sprite.Sprite):

    def __init__(self, location=[0,0], pid=1, multi=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(asset('assets/img','stores-anim.png'))
        self.rect = self.image.get_rect()
        self.rect.w = 128
        self.rect.x = location[0]
        self.rect.y = location[1]
        

        self.collide_rect = Rect(self.rect.x, self.rect.y, 128, 32)
        self.collide_rect.x = self.rect.bottomleft[0]
        self.collide_rect.y = self.rect.bottomleft[1]
        
        # self.collide_rect.h = 64
        
        # self.rect = Rect(location[0], location[1], 128, 128)


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
        # store_group = pygame.sprite.Group(Stores())
        # return store_group
    
        

    # def debug(self, debug):
    #     if debug:
    #         return pygame.draw.rect(screen, 'gold', self.rect, 1)
    def debug(self):
        pygame.draw.rect(screen, 'gold', (self.rect.x, self.rect.y, self.rect.w, self.rect.h), 1, 5)
        pygame.draw.rect(screen, 'red', (self.collide_rect[0], self.collide_rect[1], 128, 32), 1, 5)

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

