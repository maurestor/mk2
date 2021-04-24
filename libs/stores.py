import pygame
from pygame.locals import *
from .pygamextras import *

class Stores(pygame.sprite.Sprite):

    def __init__(self, location=[0,0], pid=1, multi=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(asset('assets/img','stores-anim.png'))
        self.rect = self.image.get_rect(top=128)
        self.rect.w = 128
        # self.source_rect
        # self.rect.y = 128
        self.rect.x = location[0]
        self.rect.y = location[1]
        self.surface = screen
        
        # self.collide_rect = Rect(self.rect.left, self.rect.top + 128, self.rect.w, self.rect.h-96)
        
        self.pid = pid
        self.location = location

        self.sprites = []
        self.sprites.append(self.image.subsurface(0, 0, 128, 128))    # Stay_R0
        self.sprites.append(self.image.subsurface(128, 0, 128, 128))   # Stay_R1
        self.current_sprite = 0
        self.frame = 0

        self.spritesheet = self.sprites
        
        self.vars = {'id':pid, 'type':'store', 'location':[location[0], location[1]]}

    

    def debug(self):
        #Establecer rect despues de su asignacion NO MOVER!!!
        
        textra(f'pos: {self.rect.x}, {self.rect.y}', [self.rect.x, self.rect.y-20], 'deepskyblue')
        
        if key_press['F4_key']:
            pygame.draw.rect(screen, 'gold', (self.rect.x, self.rect.y, self.rect.w, self.rect.h), 1, 5)

        pygame.draw.rect(screen, 'red', [
                self.rect.x,
                self.rect.y,
                self.rect.w,
                self.rect.h],
                1, 5)
        
        # screen.blit(self.surface, [self.rect.x, self.rect.y+128])

    def control(self, x, y):
        """
        control player movement
        """
        self.rect.x += x
        self.rect.y += y


    def update(self):
        
        self.current_sprite += 0.005  # aumente # de frames entre cada FPS
        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)-1] # si es entero cambiar frame

        self.vars['location'][0] = self.rect.x
        self.vars['location'][1] = self.rect.y

    def draw_stores(self, number):
        for i in range(number):
            pass

class StoreBg(pygame.sprite.Sprite):
    '''Usar esta clase para colisionar '''
    def __init__(self, location=[0,0], pid=1, multi=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(asset('assets/img', 'floor.png'))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]+108
    
    def control(self, x, y):
        """
        control player movement
        """
        self.rect.x += x
        self.rect.y += y

    def debug(self):
        #Establecer rect despues de su asignacion NO MOVER!!!
        # self.collide_rect = self.rect
        # x = self.collide_rect.x
        # y = self.collide_rect.y+128
        # self.collide_rect.height = 32

        textra(f'pos: {self.rect.x}, {self.rect.y}', [self.rect.x, self.rect.y-20], 'deepskyblue')
        
        pygame.draw.rect(screen, 'red', [
                self.rect.x,
                self.rect.y,
                self.rect.w,
                self.rect.h],
                1, 5)
        
        # screen.blit(self.surface, [self.rect.x, self.rect.y+128])
    def update(self):
        pass