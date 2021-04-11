#!/usr/bin/python
# -*- coding:utf-8 -*-

import pygame
import os
import sys
import time
from pygame.locals import *
from pygamextras import poswin


pygame.init()
poswin(200, 200)
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
run = True


def asset(dir_asset='img/player.old.png'):
    """Busca la ruta absoluta de la carpeta \'assets\' en el OS actual
    
    `Params`:
    dir_asset: str

    Sin parametros se devuelve la imagen de un personaje del juego.
    """
    # Carga de archivos, buscar asset()
    source_dir_file = os.path.dirname(os.path.abspath(__file__))

    path_asset = os.path.join(source_dir_file, 'assets/', dir_asset)
    return path_asset


font = pygame.font.SysFont('arial', 18)
# font = pygame.font.Font('./comicoro.ttf', 16)


# reloj pygame
clock = pygame.time.Clock()
t0 = time.time()
plus_num = 0



def draw_text(text="sample", color='black', v2i=(10, 10), bg=None):
    dialogo = font.render(text, True, color, bg)
    screen.blit(dialogo, (v2i[0], v2i[1]))


class Gamer(pygame.sprite.Sprite):
    def __init__(self, image='player-anim.png', location=[W//2, H//2], speed=3):
        pygame.sprite.Sprite.__init__(self)
        self.vars = {'left': False, 'right': False, 'up': False, 'down': False,
                     'last_dir':'down'}

        self.movex = location[0]
        self.movey = location[1]

        # Can you load image
        self.image = pygame.image.load(asset(image))
        
        self.rect = Rect(location[0], location[1], 32, 64) # self.image.get_rect()
        self.speed = speed
        self.current_sprite = 0

        self.frame = 0


        # Cargando el sprite.
        self.sprites = []

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

        self.sprites.append(pygame.transform.flip(self.sprites[0], True, False))# Stay_L0
        self.sprites.append(pygame.transform.flip(self.sprites[1], True, False))# Stay_L1

        self.sprites.append(pygame.transform.flip(self.sprites[2], True, False))# Walk_L0
        self.sprites.append(pygame.transform.flip(self.sprites[3], True, False))# Walk_L1

        self.spritesheet = self.sprites
    def up(self):
        pass
    def down(self):
        pass
    def left(self):
        pass
    def right(self):
        pass

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    # implementar este metodo para reducir codigo en update
    def select_sub_sprite(self, val_a, val_b):
        self.sprites = self.spritesheet
        self.sprites = self.sprites[val_a:val_b]
        return self.sprites

    def update(self):

        if self.vars['down']:
            if not self.rect.y + self.rect.height > H-(H//10):
                self.vars['last_dir'] = 'down'
                self.control(y=self.speed, x=0)
                self.select_sub_sprite(6, 8)
            else:
                self.select_sub_sprite(6, 8)
                self.vars['last_dir'] = 'down'
        elif self.vars['last_dir'] == 'down':
            self.select_sub_sprite(4, 6)

        if self.vars['right']:
            if not self.rect.x + self.rect.width > W-(W//10):
                self.vars['last_dir'] = 'right'
                self.control(y=0, x=self.speed)
                self.select_sub_sprite(2,4)
            else:
                self.select_sub_sprite(2,4)
                self.vars['last_dir'] = 'right'
        elif self.vars['last_dir'] == 'right':
            self.select_sub_sprite(0,2)

        if self.vars['up']:
            if not self.rect.y < 0+(H//8):
                self.vars['last_dir'] = 'up'
                self.control(y=-self.speed, x=0)
                self.select_sub_sprite(10,12)
            else:
                self.select_sub_sprite(10,12)
                self.vars['last_dir'] = 'up'
        elif self.vars['last_dir'] == 'up':
            self.select_sub_sprite(8,10)

        if self.vars['left']:
            if not self.rect.x < 0+(W//10):
                self.vars['last_dir'] = 'left'
                self.control(y=0, x=-self.speed)
                self.select_sub_sprite(14,16)
            else:
                self.select_sub_sprite(14,16)
                self.vars['last_dir'] = 'left'
        elif self.vars['last_dir'] == 'left':
            self.select_sub_sprite(12,14)


        self.rect.x = self.movex
        self.rect.y = self.movey

        self.current_sprite += 0.1  # aumente # de frames entre cada FPS
        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)-1] # si es entero cambiar frame
        
        # screen.blit(self.image, self.location)
        

gamer = Gamer()
sprite_group = pygame.sprite.Group(gamer)


def main():
    global plus_num
    run = 1
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = 0
            elif event.type == KEYDOWN:
                # do_shortcut(event)
                if event.key == K_ESCAPE:
                    run = 0

                if event.key == K_UP or event.key == K_w:
                    gamer.vars['up'] = True
                if event.key == K_DOWN or event.key == K_s: 
                    gamer.vars['down'] = True 
                if event.key == K_LEFT or event.key == K_a: 
                    gamer.vars['left'] = True 
                if event.key == K_RIGHT or event.key == K_d: 
                    gamer.vars['right'] = True
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_w: 
                    gamer.vars['up'] = False
                if event.key == K_DOWN or event.key == K_s: 
                    gamer.vars['down'] = False 
                if event.key == K_LEFT or event.key == K_a: 
                    gamer.vars['left'] = False
                if event.key == K_RIGHT or event.key == K_d: 
                    gamer.vars['right'] = False


        screen.fill('darkgray')
        draw_text('Hola bienvenid@', 'black', (10, 10), 'lightgray')
        
        
        sprite_group.update()
        sprite_group.draw(screen)

        plus_num += 1        
        pygame.display.set_caption(f'Listo!!! {plus_num}')
        clock.tick(60)
        pygame.display.flip()
        # pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
